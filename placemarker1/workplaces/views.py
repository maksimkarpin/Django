from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Workplace
from .forms import WorkplaceForm  # предположим, что форма уже создана


def workplace_list(request):
    workplaces = Workplace.objects.all()
    return render(request, 'workplaces/workplace_list.html', {'workplaces': workplaces})


def workplace_create(request):
    if request.method == 'POST':
        form = WorkplaceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Рабочее место успешно создано')
            return redirect('workplaces')
    else:
        form = WorkplaceForm()
    return render(request, 'workplaces/workplace_form.html', {'form': form})


def workplace_edit(request, pk):
    workplace = get_object_or_404(Workplace, pk=pk)

    if request.method == 'POST':
        form = WorkplaceForm(request.POST, instance=workplace)
        if form.is_valid():
            form.save()
            return redirect('workplace_list')
    else:
        form = WorkplaceForm(instance=workplace)

    return render(request, 'workplaces/workplace_form.html', {'form': form})

def workplace_update(request, pk):
    workplace = get_object_or_404(Workplace, pk=pk)
    if request.method == 'POST':
        form = WorkplaceForm(request.POST, instance=workplace)
        if form.is_valid():
            form.save()
            messages.success(request, 'Рабочее место успешно обновлено')
            return redirect('workplace_list')
    else:
        form = WorkplaceForm(instance=workplace)
    return render(request, 'workplaces/workplace_form.html', {'form': form})


def workplace_delete(request, pk):
    workplace = get_object_or_404(Workplace, pk=pk)

    if request.method == 'POST':
        workplace.delete()
        return redirect('workplace_list')

    return render(
        request,
        'workplaces/workplace_confirm_delete.html',
        {'workplace': workplace}
    )

def workplace_occupied(request):
    workplaces = Workplace.objects.filter(status='occupied')
    return render(request, 'workplaces/workplace_occupied.html', {'workplaces': workplaces})


def workplace_add(request):
    if request.method == 'POST':
        form = WorkplaceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('workplace_list')
    else:
        form = WorkplaceForm()

    return render(request, 'workplaces/workplace_form.html', {'form': form})


def workplace_edit(request, pk):
    workplace = get_object_or_404(Workplace, pk=pk)

    if request.method == 'POST':
        form = WorkplaceForm(request.POST, instance=workplace)
        if form.is_valid():
            form.save()
            return redirect('workplace_list')
    else:
        form = WorkplaceForm(instance=workplace)

    return render(request, 'workplaces/workplace_form.html', {'form': form})





