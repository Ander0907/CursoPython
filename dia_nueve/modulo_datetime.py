from datetime import datetime

# time sirve para obtener la hora, date para obtener la fecha
# mi_dia = datetime.date(2025,10,17)

# ctime sirve para obtener un formato distinto
# print(mi_dia.ctime())

# nacimiento = date(1995, 3, 5)
# fallecimiento = date(2024, 1, 2)

# vida = fallecimiento - nacimiento
# print(vida)

despierta = datetime(2022, 10, 5, 7, 20) 
duerme = datetime(2022, 10, 5, 23, 25)

vigilia = duerme - despierta