from django.db import models
import datetime
class Car(models.Model):
    name = models.CharField(max_length=200, default='Марка')
    model = models.CharField(max_length=200, default='Модель')
    info = models.TextField(default='Текст объявления')
    year = models.IntegerField(default=2012)
    motor = models.CharField(max_length=200, default='2.8 Бензин')
    price = models.DecimalField(default=2000000, decimal_places = 1, max_digits = 15)
    color = models.CharField(max_length=200, default='Черный')
    mileage = models.IntegerField(default=0)
    drive = models.IntegerField(default=0)
    wheel = models.IntegerField(default=0)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True, default=0)
    date = models.DateTimeField()
    phone = models.CharField(max_length=12, default='Номер')
    city = models.CharField(max_length=50, default='Город')
    def __str__(self):
        return (self.name + " " + self.model + ", " + str(self.price) + " тг")

class Comment(models.Model):
    comment = models.TextField(default='')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True, default=0)
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    date = models.DateTimeField()
    def __str__(self):
        return (str(self.user) + ": " + self.comment)

class Picture(models.Model):
    image = models.ImageField(blank=True, upload_to='images/', help_text='150x150px', verbose_name='Ссылка картинки')
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    main = models.BooleanField(default=False)
    def __str__(self):
        return (str(self.image))

