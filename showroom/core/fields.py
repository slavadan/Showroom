from django.db import models
from django.utils.functional import cached_property
from django.core.exceptions import ValidationError


def positive_validator(value):
    if value < 0:
        raise ValidationError(
            f'{value} is not positive',
            params={'value': value}
        )


class PositiveDecimalField(models.DecimalField):

    @cached_property
    def validators(self):
        return super().validators + [positive_validator]
