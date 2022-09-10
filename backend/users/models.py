from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    naming = models.CharField(max_length=250)
    inn = models.CharField(max_length=40)
    kpp = models.CharField(max_length=40)
    sup_type = models.CharField(max_length=40)

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return self.naming


class DataSupplier(models.Model):
    id_sup = models.BigAutoField(primary_key=True)
    sup_username = models.TextField()
    sup_inn = models.TextField()
    sup_kpp = models.TextField()
    sup_name = models.TextField()
    sup_type = models.TextField()

    class Meta:
        managed = False
        db_table = 'data_supplier'
        unique_together = (('sup_inn', 'sup_kpp', 'sup_name'),)