from django.db import models
try:
    from employees.models import Employee
except ImportError:
    from .employees.models import Employee

class Workplace(models.Model):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='workplaces',
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
        default='office',
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



    def __str__(self):
        return f"Место {self.number}"

    @property
    def department(self):
        if self.employee:
            return self.employee.department
        return None