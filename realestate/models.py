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


class LivingRoom(models.Model):
    SOFASTYPES = (
        ('Chesterfield (Classic)', 'Chesterfield (Classic)'),
        ('Mid-Century (Modern)', 'Mid-Century (Modern)'),
        ('Lawson (Transitional)', 'Lawson (Transitional)')
    )

    TVTYPES = (
        ('OLED', 'OLED'),
        ('LED', 'LED'),
        ('Plasma', 'Plasma')
    )

    CHAIRTYPES = (
        ('Egg', 'Egg'),
        ('Wingback', 'Wingback'),
        ('Chaise Lounge', 'Chaise Lounge')
    )

    sofas = models.CharField(
        max_length=200, choices=SOFASTYPES, blank=True, null=True, default=None)

    televisions = models.CharField(
        max_length=200, choices=TVTYPES, blank=True, null=True, default=None)

    chairs = models.CharField(
        max_length=200, choices=CHAIRTYPES, blank=True, null=True, default=None)

    def __str__(self):
        return self.sofas


class BedRoom(models.Model):
    BEDSIZE = (
        ('Twin', 'Twin'),
        ('Full', 'Full'),
        ('Queen', 'Queen'),
    )

    DRESSERSTYPES = (
        ('Horizontal', 'Horizontal'),
        ('Vertical', 'Vertical'),
        ('Gentlemen Chest', 'Gentlemen Chest')
    )

    DESKTYPES = (
        ('Modern', 'Modern'),
        ('Small', 'Small'),
        ('Corner', 'Corner')
    )

    beds = models.CharField(
        max_length=200, choices=BEDSIZE, blank=True, null=True, default=None)

    dressers = models.CharField(
        max_length=200, choices=DRESSERSTYPES, blank=True, null=True, default=None)

    desks = models.CharField(
        max_length=200, choices=DESKTYPES, blank=True, null=True, default=None)

    def __str__(self):
        return self.beds
