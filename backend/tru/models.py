from django.db import models

from tru.manager import TruManager


class Tru(models.Model):
    index = models.BigIntegerField(primary_key=True)
    id_cte = models.BigIntegerField(unique=True, blank=True, null=True)
    cte_name = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    kpgz_code = models.TextField(blank=True, null=True)
    characteristics = models.TextField(blank=True, null=True)

    objects = TruManager()

    class Meta:
        managed = False
        db_table = 'data_tru'

    def dynamics(self):
        return TruDynamics.objects.get(id_cte=self)


class TruProperty(models.Model):
    id_property = models.BigAutoField(primary_key=True)
    id_cte = models.ForeignKey(
        'tru.Tru', models.DO_NOTHING,
        db_column='id_cte', to_field='id_cte',
        related_name='properties'
    )
    prop_name = models.TextField()
    prop_value = models.TextField(blank=True, null=True)
    prop_id = models.BigIntegerField()
    prop_unit = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_tru_property'


class TruDynamics(models.Model):
    id_cte = models.OneToOneField(
        'tru.Tru', models.DO_NOTHING,
        db_column='id_cte', primary_key=True,
        related_name='dynamics'
    )
    dynamics = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'data_tru_dynamics'
