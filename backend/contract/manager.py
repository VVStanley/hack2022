from django.db import models
from django.db.models import Sum


class ContractManager(models.Manager):

    def data_for_map(self):
        from django.db import connection
        query = """
        SELECT 
            sum(contract_price) as sum_cost, 
            region_name
        FROM public.data_contract join data_region 
        on substring(cons_inn::text,1,2)=region_code::text group by region_name order by sum_cost desc
        """
        with connection.cursor() as cursor:
            cursor.execute(query)
            result_list = []
            for row in cursor.fetchall():
                p = {
                    "sum_cost": row[0],
                    "region_name": row[1]
                }
                result_list.append(p)
        return result_list


class ConsumerManager(models.Manager):

    def with_sum_contracts(self):
        return self.annotate(
            contract_sum=Sum('consumer_contracts__contract_price')
        )

    def data_sale_consumers(self, id_consumer, id_supplier):
        from django.db import connection
        query = f"""
        select 
            dce1.id_cte,
            cte_name, 
            sum(quantity) as quantity, 
            sum(amount) as amount, 
            count (*) as contracts_cnt  
        from data_contract dc1 join 
        data_contract_element dce1 on dc1.id_contract =dce1.id_contract join
        data_tru dt1 on dt1.id_cte=dce1.id_cte

        where dce1.id_cte not in (select dce.id_cte from data_contract dc join data_contract_element dce on dc.id_contract =dce.id_contract join
        data_tru dt on dt.id_cte=dce.id_cte where id_supplier={id_supplier} and dce.id_cte is not null) 
        and dc1.id_consumer={id_consumer} group by id_consumer,dce1.id_cte, cte_name order by amount desc
        """
        with connection.cursor() as cursor:
            cursor.execute(query)
            result_list = []
            for row in cursor.fetchall():
                p = {
                    "id_cte": row[0],
                    "cte_name": row[1],
                    "quantity": row[2],
                    "amount": row[3],
                    "contracts_cnt": row[4],
                }
                result_list.append(p)
        return result_list

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
