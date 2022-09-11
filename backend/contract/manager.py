from django.db import models
from django.db.models import Sum


class ConsumerManager(models.Manager):

    def with_sum_contracts(self):
        return self.annotate(
            contract_sum=Sum('consumer_contracts__contract_price')
        )

    def tru_all_consumers_sale(self, id_cte):
        from django.db import connection
        query = f"""
        SELECT 
        id_cte,
            con.id_consumer,
            con.cons_name || ' ('||con.cons_inn||'/'||con.cons_kpp||')' as name, 
            sum(quantity) as quantity, 
            sum(amount) as amount
        FROM 
            public.data_contract_element dce join 
            data_contract dc on dc.id_contract=dce.id_contract 
            join data_consumer con on dc.id_consumer=con.id_consumer
        where id_cte={id_cte}
        group by id_cte, con.id_consumer, con.cons_name || ' ('||con.cons_inn||'/'||con.cons_kpp||')';
        """
        with connection.cursor() as cursor:
            cursor.execute(query)
            result_list = []
            for row in cursor.fetchall():
                p = {
                    "id_consumer": row[0],
                    "name": row[1],
                    "quantity": row[2],
                    "amount": row[3],
                }
                result_list.append(p)
        return result_list
