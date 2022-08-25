""" from datetime import datetime

my_time = datetime.now()
my_day = my_time.date.today()

if __name__ == '__main__':
    print(my_time)
    print(my_day)
    print(f'{my_day.year}-{my_day.month}-{my_day.day}')

# date format
print(my_day.strftime('%Y-%m-%d')) # American format
print(my_day.strftime('%d %B %Y')) # Latin American format """

from datetime import datetime
from pytz import timezone

bogota_time = datetime.now(timezone('America/Bogota'))
print(bogota_time.strftime('%Y-%m-%d %H:%M:%S'))
print(type(True))