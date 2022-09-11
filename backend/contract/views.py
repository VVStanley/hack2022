from django.shortcuts import render
from django.views import View
from django.templatetags.static import static
from contract.models import Contract
from project import settings


class MapView(View):

    template_name = 'map.html'

    map = {
        'Белгородская область': 'fregion,RU-BEL,Белгородскаяобласть,651,{}',
        'Брянская область': 'fregion,RU-BRY,Брянскаяобласть,875,{}',
        'Владимирская область': 'fregion,RU-VLA,Владимирскаяобласть,1283,{}',
        'Воронежская область': 'fregion,RU-VOR,Воронежскаяобласть,1172,{}',
        'Ивановская область': 'fregion,RU-IVA,Ивановскаяобласть,1097,{}',
        'Калужская область': 'fregion,RU-KLU,Калужскаяобласть,1225,{}',
        'Костромская область': 'fregion,RU-KOS,Костромскаяобласть,371,{}',
        'Курская область': 'fregion,RU-KRS,Курскаяобласть,556,{}',
        'Липецкая область': 'fregion,RU-LIP,Липецкаяобласть,673,{}',
        'Москва': 'fregion, RU-MOW,Москва,151313,{}',
        'Московская область': 'fregion,RU-MOS,Московскаяобласть,25961,{}',
        'Орловская область': 'fregion,RU-ORL,Орловскаяобласть,548,{}',
        'Рязанская область': 'fregion,RU-RYA,Рязанскаяобласть,1080,{}',
        'Смоленская область': 'fregion,RU-SMO,Смоленскаяобласть,964,{}',
        'Тамбовская область': 'fregion,RU-TAM,Тамбовскаяобласть,736,{}',
        'Тверская область': 'fregion,RU-TVE,Тверскаяобласть,1212,{}',
        'Тульская область': 'fregion,RU-TUL,Тульскаяобласть,1564,{}',
        'Ярославская область': 'fregion,RU-YAR,Ярославскаяобласть,1157,{}',
        'Центральный округ': 'fdistrict,Central,Центральныйокруг,54493,{}',
    }

    def get(self, request):
        queryset_data = Contract.objects.data_for_map()

        for item in queryset_data:
            if item['region_name'] in self.map:
                self.map[item['region_name']] = (
                    self.map[item['region_name']].format(
                        round(item['sum_cost'], 2)
                    )
                )

        for key, value in self.map.items():
            if '{}' in value:
                self.map[key] = value.format('0')

        with open(settings.BASE_DIR / 'static/zak4.csv', 'w') as f:
            f.write('Rtype,RegionCode,RegionName,CarAccidents,Deaths\n')
            f.write('federation,Russian Federation,Российская Федерация,203597,27991\n')

            for key, value in self.map.items():
                f.write(value + '\n')
        return render(request, self.template_name)