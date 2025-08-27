try:
    from employees.models import Employee
except ImportError:
    from .employees.models import Employee
from django.db import models



class Workplace(models.Model):
    employee = models.OneToOneField(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='workplace',
        verbose_name="Сотрудник"
    )

    number = models.IntegerField(verbose_name="Номер места")

    TYPE_CHOICES = [
        ("Разработчик", "Разработчик"),
        ("Тестировщик", "Тестировщик")
    ]

    type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        default=TYPE_CHOICES[0][0],
        verbose_name="Тип"
    )

    status = models.CharField(
        max_length=10,
        choices=[
            ('occupied', 'Занято'),
            ('free', 'Свободно')
        ],
        default='free'
    )

    additional_info = models.TextField(
        blank=True,
        null=True,
        verbose_name="Дополнительная информация"
    )

    def __str__(self):
        return f"Место {self.number}"

    @property
    def department(self):
        if self.employee:
            return self.employee.department
        return None
