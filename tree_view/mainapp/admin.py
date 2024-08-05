from django.contrib import admin
from .models import Subdivision, Position, Employee


class SubdivisionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'level')
    fields = ('name', 'level', 'subdivisions')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'patronymic', 'position', 'subdivision', 'salary', 'employment_date')
    fields = ('name', 'surname', 'patronymic', 'position', 'subdivision', 'salary', 'employment_date')


# Register the models with their respective ModelAdmin classes
admin.site.register(Subdivision, SubdivisionAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Employee, EmployeeAdmin)
