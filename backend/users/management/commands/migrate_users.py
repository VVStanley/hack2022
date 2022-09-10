import multiprocessing

from django.core.management.base import BaseCommand

from users.models import DataSupplier, User


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    @staticmethod
    def worker(data_user):
        user, _ = User.objects.get_or_create(
            username=data_user.sup_username,
            defaults={
                "naming": data_user.sup_name,
                "inn": data_user.sup_inn,
                "kpp": data_user.sup_kpp,
                "sup_type": data_user.sup_type,
            }
        )
        user.set_password('11111')
        user.save()
        print(user.id, 'yes')

    def handle(self, *args, **options):
        users = DataSupplier.objects.exclude(sup_username__in=User.objects.values_list('username'))

        p = multiprocessing.Pool(15)
        xs = p.map(self.worker, users)
