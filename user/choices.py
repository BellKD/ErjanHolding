from django.db.models import TextChoices

class MyUserRoleEnum(TextChoices):
    STANDARD_USER = 'standard_user','Обычный пользователь'
    MANAGER = 'manager','Менеджер'
    ACCOUNTANT = 'accountant','Бухгалтер'


