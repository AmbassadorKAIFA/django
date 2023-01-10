from django.db import models


class Table(models.Model):
    number = models.IntegerField()
    num_seats = models.IntegerField()
    shape = models.BooleanField()
    x_coord = models.IntegerField()
    y_coord = models.IntegerField()
    width = models.DecimalField(max_digits=3, decimal_places=2)
    high = models.DecimalField(max_digits=3, decimal_places=2)
    radius = models.IntegerField(null=True, blank=True)
    date = models.DateField()
    booking = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.number} | {self.num_seats} | {self.shape} | {self.x_coord} | {self.y_coord} | {self.width} | {self.high} | {self.radius} | {self.date} | {self.booking} '


class Orders(models.Model):
    name = models.CharField(max_length=90)
    table_num = models.IntegerField()
    email = models.CharField(max_length=90)
    date = models.DateTimeField()