from django.db import models


class Consumer(models.Model):
    """Потребитель"""
    id_consumer = models.BigAutoField(primary_key=True)
    cons_inn = models.TextField()
    cons_kpp = models.TextField()
    cons_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'data_consumer'


class Contract(models.Model):
    id_contract = models.BigIntegerField(primary_key=True)
    contract = models.TextField(blank=True, null=True)
    pub_date = models.DateTimeField(blank=True, null=True)
    contract_date = models.DateTimeField(blank=True, null=True)
    contract_price = models.FloatField(blank=True, null=True)
    cte = models.TextField(blank=True, null=True)
    id_supplier = models.ForeignKey(
        'contract.Supplier', models.DO_NOTHING, db_column='id_supplier',
        blank=True, null=True,
        related_name='my_contracts'
    )
    # TODO: наверное тут ФК
    sup_username = models.TextField()
    sup_username_d = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True
    )
    id_consumer = models.ForeignKey(
        'contract.Consumer', models.DO_NOTHING, db_column='id_consumer',
        related_name='consumer_contracts'
    )

    class Meta:
        managed = False
        db_table = 'data_contract'


class Supplier(models.Model):
    """Поставщик"""
    id_sup = models.BigAutoField(primary_key=True)
    sup_username = models.OneToOneField(
        to='users.User',
        to_field='username',
        on_delete=models.PROTECT,
        related_name='supplier'
    )
    sup_inn = models.TextField()
    sup_kpp = models.TextField()
    sup_name = models.TextField()
    sup_type = models.TextField()


    class Meta:
        managed = False
        db_table = 'data_supplier'
        unique_together = (('sup_inn', 'sup_kpp', 'sup_name'),)

    @property
    def sup_username_id(self):
        return self.sup_username
