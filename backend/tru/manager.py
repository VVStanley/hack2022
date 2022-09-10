from django.db import models


class TruManager(models.Manager):

    def get_tru_with_my_sales(self, id_supplier):
        from django.db import connection
        query = f"""
            select 
                my_sells.id_cte,
                dynamics,
                sum_all,
                my_sum_amount,
                case when sum_all/my_sum_amount>1 then sum_all/my_sum_amount *100 -100 else 0 end as growth_perspective, 
                cte_name,
                category,
                cons_cnt
            from (select
                "data_tru_dynamics"."id_cte",
                "data_tru_dynamics"."dynamics",
                "data_tru_dynamics"."sum_all",
                "contract_element"."my_sum_amount",
                "data_tru"."cte_name", 
                "data_tru"."category"
            from
                "data_tru_dynamics"
            right join (
            select
                "data_contract_element"."id_cte",
                SUM("data_contract_element"."amount") as "my_sum_amount"
            from
                "data_contract_element"
            where
                "data_contract_element"."id_contract" in (
                select
                    U0."id_contract"
                from
                    "data_contract" U0
                where
                    U0."id_supplier" = {id_supplier})
            group by
                "data_contract_element"."id_cte"
            order by
                "data_contract_element"."id_cte" asc
            ) as "contract_element" on "contract_element"."id_cte" = "data_tru_dynamics"."id_cte" 
            left join (
                select "dt"."id_cte", "dt"."cte_name", "dt"."category" from "data_tru" as "dt" 
            ) as "data_tru"
            on "contract_element"."id_cte" = "data_tru"."id_cte" 
            where
                "data_tru_dynamics"."id_cte" in (
                select
                    V0."id_cte"
                from
                    "data_contract_element" V0
                where
                    V0."id_contract" in (
                    select
                        U0."id_contract"
                    from
                        "data_contract" U0
                    where
                        U0."id_supplier" = {id_supplier}))) my_sells  left join
                        
                (SELECT id_cte,count(id_consumer) as cons_cnt
                FROM public.data_contract_element dce join data_contract dc on dc.id_contract=dce.id_contract group by id_cte) cons		on cons.id_cte=my_sells.id_cte
                        order by sum_all desc
                    """
        with connection.cursor() as cursor:
            cursor.execute(query)
            result_list = []
            for row in cursor.fetchall():
                p = {
                    "id_cte": row[0],
                    "dynamics": row[1],
                    "sum_all": row[2],
                    "my_sum_amount": row[3],
                    "growth_perspective": row[4],
                    "cte_name": row[5],
                    "category": row[6],
                    "cons_cnt": row[7]
                }
                result_list.append(p)
        return result_list
