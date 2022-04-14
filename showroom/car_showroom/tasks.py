from rest_framework.authtoken.admin import User
from django.core.mail import send_mail
from .models import CarShowroom, Transaction, SupplierSellCar, ShowroomSellCar, Customer
from sales.models import SupplierSale, CarShowroomSale
from django.db.models import Q, F
from showroom.celery import app


@app.task
def showroom_buy_cars():
    for showroom in CarShowroom.objects.all():
        showroom_query = showroom.buy_query

        find_suppliers_cars = (
            Q(car__model__startswith=showroom_query.get('name')) &
            Q(car__max_speed__exact=showroom_query.get('max_speed')) &
            Q(car__engine_power__exact=showroom_query.get('engine_power')) &
            Q(car__color__startswith=showroom_query.get('color')) &
            Q(car__type__startswith=showroom_query.get('type'))
        )

        supplier_cars = SupplierSellCar.objects.filter(
            find_suppliers_cars
        ).order_by('-supplier__sale__percent')
        showroom_cars = ShowroomSellCar.objects.filter(showroom__name__iexact=showroom.name)

        for supplier_car in supplier_cars:

            price = supplier_car.price

            if SupplierSale.objects.filter(cars__pk=supplier_car.car.id).exists():
                sale = SupplierSale.objects.get(cars__pk=supplier_car.car.id)
                price -= (price * sale.percent / 100)

            if price > showroom.balance:
                continue

            showroom.balance -= price

            showroom_cars.update_or_create(
                car=supplier_car.car,
                showroom=showroom,
                supplier=supplier_car.supplier,
                defaults={
                    'count': F('count') + 1
                }
            )

            showroom.save()


@app.task
def customer_buy_cars():
    for customer in Customer.objects.all():
        customer_query = customer.buy_query
        buy_count = customer_query.get('count')

        find_showrooms_cars = (
            Q(car__brand__startswith=customer_query.get('brand')) &
            Q(car__model__iexact=customer_query.get('model')) &
            Q(car__max_speed__exact=customer_query.get('max_speed')) &
            Q(car__engine_power__exact=customer_query.get('engine_power')) &
            Q(car__color__startswith=customer_query.get('color')) &
            Q(car__type__startswith=customer_query.get('type')) &
            Q(car__year__exact=customer_query.get('year'))
        )

        showroom_cars = ShowroomSellCar.objects.filter(
            find_showrooms_cars
        ).order_by('-showroom__sale__percent')

        for car_showroom in showroom_cars:

            if buy_count <= 0:
                break

            total_price = 0
            price = car_showroom.price
            can_buy = 0

            if CarShowroomSale.objects.filter(cars__pk=car_showroom.car.id).exists():
                sale = CarShowroomSale.objects.get(cars__pk=car_showroom.car.pk)
                price = (total_price * sale.percent / 100)

            if buy_count > car_showroom.count:
                total_price += price * car_showroom.count
                buy_count -= car_showroom.count
                can_buy += car_showroom.count
            else:
                total_price += buy_count * price
                can_buy += buy_count

            if total_price > customer.balance:
                while total_price > customer.balance:
                    can_buy -= 1
                    total_price = price * can_buy

            if can_buy <= 0:
                continue

            customer.balance -= total_price
            Transaction(
                price=total_price,
                count=can_buy,
                car=car_showroom.car,
                car_showroom=car_showroom.showroom
            ).save()

            car_showroom.count -= can_buy
            car_showroom.save()
            customer.save()
