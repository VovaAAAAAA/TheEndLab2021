from prettytable import PrettyTable

from data import dt, th
columns = len(th)
table = PrettyTable(th)

dt_data = dt[:]
while dt_data:
    columns = 5
    table.add_rows(dt_data[:columns])
    dt_data = dt_data[columns:]
table1 = str(table) 
f = open('new_file.txt', 'w', encoding='utf-8')
f.write(table1 )
f.close()

def opentabble_2():
    ("new_file.txt")