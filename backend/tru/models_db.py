# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DataTruProperty(models.Model):
    id_property = models.BigAutoField(primary_key=True)
    id_cte = models.ForeignKey('DataTru', models.DO_NOTHING, db_column='id_cte', to_field='id_cte')
    prop_name = models.TextField()
    prop_value = models.TextField(blank=True, null=True)
    prop_id = models.BigIntegerField()
    prop_unit = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_tru_property'
