from django.db import models

# Create your models here.


class KitchenRoom(models.Model):
    COUNTERTOP = (
        ('Granite', 'Granite'),
        ('Quartz', 'Quartz'),
        ('Wood', 'Wood')
    )

    ROOMSHAPE = (
        ('Linear (Two Parallel Lines)', 'Linear (Two Parallel Lines)'),
        ('L-shaped', 'L-shaped'),
        ('U-shaped', 'U-shaped')
    )

    REFRIGERATORSTYLE = (
        ('Side-By-Side', 'Side-By-Side'),
        ('Bottom-Freezer', 'Bottom-Freezer'),
        ('Top-Freezer', 'Top-Freezer')
    )

    counter_top = models.CharField(
        max_length=200, choices=COUNTERTOP, blank=True, null=True, default=None)

    room_shape = models.CharField(
        max_length=200, choices=ROOMSHAPE, blank=True, null=True, default=None)

    refrigerator_style = models.CharField(
        max_length=200, choices=REFRIGERATORSTYLE, blank=True, null=True, default=None)

    def __str__(self):
        return self.counter_top
