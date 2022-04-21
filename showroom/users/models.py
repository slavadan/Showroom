from django.contrib.auth.models import User
from django.db import models


# Create your models here
class ShowroomUser(User):
    is_supplier = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_showroom = models.BooleanField(default=False)

    def __str__(self):
        template = '{0.username} {0.email}'
        return template.format(self)
