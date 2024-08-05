from django.db import models

Constants = {
    'LEVEL_CHOICES': [
        (1, 'Level 1'),
        (2, 'Level 2'),
        (3, 'Level 3'),
        (4, 'Level 4'),
        (5, 'Level 5'),
    ]
}


class Subdivision(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Position(models.Model):
    LEVEL_CHOICES = Constants['LEVEL_CHOICES']

    name = models.CharField(max_length=100)
    level = models.PositiveSmallIntegerField(choices=LEVEL_CHOICES, verbose_name='Position Level')
    superior_position = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                                          related_name='sub_positions')
    subdivision = models.ForeignKey(Subdivision, on_delete=models.CASCADE, related_name='positions', null=True)

    def __str__(self):
        return f"{self.name} (Level {self.level})"


class Employee(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    subdivision = models.ForeignKey(Subdivision, on_delete=models.CASCADE)
    salary = models.IntegerField()
    employment_date = models.DateField()
