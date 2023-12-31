import datetime as dt

from django.core.exceptions import ValidationError


def validate_username(value):
    '''Валидатор юзера.'''

    if value.lower() == 'user':
        raise ValidationError(
            ('Имя пользователя не может быть <user>'),
            params={'value': value},
        )


def validate_year(value):
    '''Валидатор даты.'''

    year = dt.date.today().year
    if not (value <= year):
        raise ValidationError('Дата указана некорректно')
    return value


def validate_ingredients(self, value):
    '''Валидатор ингридиентов.'''
    if not value:
        raise ValidationError('Добавьте ингридиенты')
    for amount in value:
        if amount['amount'] <= 0:
            raise ValidationError(
                'Колличество ингридиентов должго быть больше 0')
    return value
