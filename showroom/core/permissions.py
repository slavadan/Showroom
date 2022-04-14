from rest_framework import permissions


class IsCustomerUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_customer


class IsCarShowroomUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_showroom


class IsSupplierUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_supplier
