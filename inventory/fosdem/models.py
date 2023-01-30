from django.db import models

# Create your models here.


class Box(models.Model):
    number = models.CharField(max_length=256)
    notes = models.TextField(blank=True)
    items = models.ManyToManyField('Item', through='Inventory')

    def __str__(self):
        return '{0}'.format(self.number)


class Item(models.Model):
    name = models.CharField(max_length=1024)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=1024)
    boxes = models.ManyToManyField(Box, through='Transport')

    def __str__(self):
        return self.name


class Inventory(models.Model):
    box = models.ForeignKey(Box, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    must_have = models.IntegerField(default=1)
    have = models.IntegerField(default=0)

    def __str__(self):
        return 'Box {0} has {1} {2} and should have {3}'.format(
            self.box.number,
            self.have,
            self.item.name,
            self.must_have
        )


class Transport(models.Model):
    box = models.ForeignKey(Box, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    direction = models.CharField(max_length=256, default='storage')

    def __str__(self):
        return 'Box {0} is stored in {1} ({2})'.format(
            self.box.number,
            self.location.name,
            self.direction
        )
