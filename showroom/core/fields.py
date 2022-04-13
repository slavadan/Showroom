from django.db import models
from django.utils.functional import cached_property
from .validators import positive_validator


class PositiveDecimalField(models.DecimalField):

    @cached_property
    def validators(self):
        return super().validators + [positive_validator]
