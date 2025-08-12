from django.db import models
from django.utils import timezone


class Employee(models.Model):
    POSITION_CHOICES = [
        ('Тестировщик', 'Тестировщик'),
        ("Разработчик", 'Разработчик'),

    ]
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    middle_name = models.CharField(max_length=100, verbose_name="Отчество")
    position = models.CharField(
        max_length=20,
        choices=POSITION_CHOICES,
        verbose_name="Должность"
    )
    department = models.CharField(max_length=200, verbose_name="Отдел")
    email = models.EmailField(verbose_name="Email")
    hire_date = models.DateField(verbose_name="Дата приема", default=timezone.now)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

