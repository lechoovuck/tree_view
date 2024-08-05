from django.shortcuts import render
from .models import Subdivision, Position, Employee


def main(request):
    subdiv = Subdivision.objects.all().values_list('id', 'name', named=True)
    positions = Position.objects.all().values_list('subdivision_id', 'id', 'name', named=True)
    employees = Employee.objects.all().values_list('subdivision_id', 'position_id', 'name', 'surname', 'salary', named=True)
    return render(request, 'mainapp/index.html', context={
        'subdiv': subdiv,
        'positions': positions,
        'employees': employees,
    })
