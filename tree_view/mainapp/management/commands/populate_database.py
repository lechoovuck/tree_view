import random
from django.core.management.base import BaseCommand
from mainapp.models import Subdivision, Position, Employee, Constants

import datetime as dt


def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + dt.timedelta(seconds=random_second)


class Command(BaseCommand):
    help = 'Populate the database with subdivisions, positions, and employees'

    def handle(self, *args, **kwargs):
        self.create_subdivisions()
        self.create_positions()
        self.create_employees()
        self.stdout.write(self.style.SUCCESS('Successfully populated the database'))

    def create_subdivisions(self):
        subdivisions = [f'Subdivision {i}' for i in range(1, 6)]
        Subdivision.objects.bulk_create([Subdivision(name=name) for name in subdivisions])
        self.stdout.write(self.style.SUCCESS('Successfully created subdivisions'))

    def create_positions(self):
        subdivisions = Subdivision.objects.all().values_list('id', flat=True)

        for subdivision in subdivisions:
            superior_position = None
            for level, _ in Constants['LEVEL_CHOICES']:
                position = Position.objects.create(
                    name=f'Position {subdivision}-{level}',
                    level=level,
                    subdivision_id=subdivision,
                    superior_position=superior_position
                )
                superior_position = position
        self.stdout.write(self.style.SUCCESS('Successfully created positions'))

    def create_employees(self):
        positions = Position.objects.all().values_list('id', 'subdivision_id', named=True)

        d1 = dt.datetime.strptime('1/1/2014 1:30 PM', '%m/%d/%Y %I:%M %p')
        d2 = dt.datetime.strptime('1/1/2024 4:50 AM', '%m/%d/%Y %I:%M %p')

        employees = []

        for i in range(50000):
            employee_position = random.choice(positions)

            employees.append(Employee(
                name=f'{i} name',
                surname=f'{i} surname',
                patronymic=f'{i} patronymic',
                position_id=employee_position.id,
                subdivision_id=employee_position.subdivision_id,
                salary=random.randrange(40000, 300000, 10000),
                employment_date=random_date(d1, d2).date()
            ))

        try:
            Employee.objects.bulk_create(employees)
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error creating employees: {e}'))

        self.stdout.write(self.style.SUCCESS('Successfully created employees'))
