# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DataContractElement(models.Model):
    id_element = models.BigAutoField(primary_key=True)
    id_contract = models.ForeignKey('DataContract', models.DO_NOTHING, db_column='id_contract')
    id_cte = models.ForeignKey('DataTru', models.DO_NOTHING, db_column='id_cte', to_field='id_cte', blank=True, null=True)
    quantity = models.FloatField()
    amount = models.FloatField()

    class Meta:
        managed = False
        db_table = 'data_contract_element'
