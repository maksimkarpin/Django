from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm, EmployeeSkillForm
from .forms import SkillForm, Skill
from.forms import EmployeeCreationForm
from .forms import EmployeeUpdateForm
from django.forms import formset_factory



SkillFormSet = formset_factory(SkillForm, extra=3)

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})


def employee_create(request):
    employee_form = EmployeeCreationForm()
    SkillFormSet = formset_factory(EmployeeSkillForm, extra=1)
    skill_forms = SkillFormSet()
    skills = Skill.objects.all()

    if request.method == 'POST':
        employee_form = EmployeeCreationForm(request.POST)
        skill_forms = SkillFormSet(request.POST)

        if employee_form.is_valid() and skill_forms.is_valid():
            employee = employee_form.save()

            for skill_form in skill_forms:
                if skill_form.is_valid():
                    skill_instance = skill_form.save(commit=False)
                    skill_instance.employee = employee
                    skill_instance.save()

            return redirect('employees_list')

    return render(request,
        'employees/employee_form.html',
        {
            'employee_form': employee_form,
            'skill_forms': skill_forms,
            'skills': skills
        }
    )

def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employees_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/employee_form.html', {'form': form})


def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == 'POST':
        employee.delete()
        return redirect('employees_list')

    return render(
        request,
        'employees/employee_confirm_delete.html',
        {'employee': employee}
    )
def skill_create(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('skill_form')
    else:
        form = SkillForm()
    return render(request, 'employees/skill_form.html', {'form': form})


def employee_edit(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == 'POST':
        form = EmployeeUpdateForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employees_list')
    else:
        form = EmployeeUpdateForm(instance=employee)

    return render(
        request,
        'employees/employee_form.html',
        {'form': form}
    )


def skill_list(request):
    skills = Skill.objects.all()
    return render(request, 'employees/skill_list.html', {'skills': skills})


def skill_add(request):
    form = SkillForm()

    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('skill_list')

    return render(request, 'employees/skill_form.html', {'form': form})


def skill_edit(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    form = SkillForm(instance=skill)

    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('skill_list')

    return render(request, 'employees/skill_form.html', {'form': form})


def skill_delete(request, pk):
    skill = get_object_or_404(Skill, pk=pk)

    if request.method == 'POST':
        skill.delete()
        return redirect('skill_list')

    return render(request, 'employees/skill_confirm_delete.html', {'skill': skill})
