from prettytable import PrettyTable

from data import dt

x = PrettyTable()

x.field_names = ["Код", "Ринок", "Дата","Картопля","Капуста","Цибуля","Середня ціна"]

for i in range(0, len(dt)):
    x.add_rows(
        [
            dt[i]
        ]
    )

def openTabble():
    print('\nАНАЛИЗ ЗМІНИ ЦІН')
    print(x)