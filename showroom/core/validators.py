from django.core.exceptions import ValidationError


def positive_validator(value):
    if value < 0:
        raise ValidationError(
            f'{value} is not positive',
            params={'value': value}
        )


def year_validator(value):
    if value < 1986:
        raise ValidationError(
            f'{value} year is not valid',
            params={'value': value}
        )
