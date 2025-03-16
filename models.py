from django.db import models
class Data(models.Model):
    oldData = models.TextField('Исходные данные')
    sortData = models.TextField('Отсортированные данные')

# Create your models here.
