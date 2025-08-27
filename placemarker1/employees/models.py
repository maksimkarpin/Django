from django.db import models
from django.contrib.auth.models import AbstractUser

class Skill(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название навыка")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")

    def __str__(self):
        return self.name



class EmployeeSkill(models.Model):
    employee = models.ForeignKey(
        'Employee',
        related_name='employee_skills',
        on_delete=models.CASCADE
    )
    skill = models.ForeignKey(
        'Skill',
        related_name='employee_skills',
        on_delete=models.CASCADE
    )
    level = models.PositiveIntegerField(
        verbose_name="Уровень владения",
        choices=[(i, i) for i in range(1, 11)]
    )

    def __str__(self):
        return f"{self.skill.name} - {self.level}/10"

class Employee(AbstractUser):
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'middle_name', 'department']

    GENDER_CHOICES = [
        ('male', 'Мужской'),
        ('female', 'Женский')
    ]

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        verbose_name="Пол",
        default='male'
    )

    middle_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Отчество"
    )

    department = models.CharField(
        max_length=100,
        verbose_name="Отдел"
    )

    position = models.CharField(
        max_length=100,
        verbose_name="Должность",
        blank=True,
        null=True
    )

    phone = models.CharField(
        max_length=20,
        verbose_name="Номер телефона",
        blank=True,
        null=True
    )

    hire_date = models.DateField(
        verbose_name="Дата приема на работу",
        blank=True,
        null=True
    )

    skills = models.ManyToManyField(
        Skill,
        through='EmployeeSkill',
        related_name='employees',
        blank=True
    )

    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание"
    )
    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="Имя пользователя"
    )

    def __str__(self):
        return f"{self.last_name} {self.first_name}"




