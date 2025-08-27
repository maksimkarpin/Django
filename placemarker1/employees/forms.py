from django import forms
from django.forms import DateInput
from .models import Employee, Skill
from django.forms import formset_factory
from .models import EmployeeSkill
from django.contrib.auth.forms import UserCreationForm

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'first_name',
            'last_name',
            'middle_name',
            'department',
            'email',
            'phone',
            'hire_date',
            'gender',
            'description',
            'skills'
        ]
        widgets = {
            'hire_date': DateInput(attrs={'type': 'date'}),
            'skills': forms.CheckboxSelectMultiple
        }

    skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )
class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'description']


class EmployeeCreationForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name',
                  'last_name',
                  'email',
                  'phone',
                  'hire_date',
                  'department',
                  'description']
        widgets = {
            'hire_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.skill_forms = formset_factory(SkillForm, extra=3)()

    def save(self, commit=True):
        employee = super().save(commit=False)
        user = super().save(commit=False)

        if commit:
            employee.save()
            return employee

        base_username = f"{user.first_name.lower()}_{user.last_name.lower()}"
        username = base_username
        counter = 1


        while Employee.objects.filter(username=username).exists():
            username = f"{base_username}_{counter}"
            counter += 1

        user.username = username
        user.set_unusable_password()

        if commit:
            user.save()
        return user

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if Employee.objects.filter(username=username).exists():
            raise forms.ValidationError("Пользователь с таким именем уже существует")
        return username

class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'phone', 'hire_date', 'department']
        widgets = {
            'hire_date': forms.DateInput(attrs={'type': 'date'}),  # Добавляем календарь
        }

class EmployeeSkillForm(forms.ModelForm):
    class Meta:
        model = EmployeeSkill
        fields = ['skill', 'level']
        widgets = {
            'level': forms.NumberInput(attrs={'min': 1, 'max': 10})
        }

EmployeeSkillFormSet = formset_factory(EmployeeSkillForm, extra=3)
