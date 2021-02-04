month = int(input('Введите номер месяца от 1 до 12'))
seasons ={ 'зима': (12, 1, 2),
            'весна': (3, 4, 5),
            'лето': (6, 7, 8),
            'осень': (9, 10,11)
        }
while month == 0 or month > 12:
    month = int(input('Что-то пошло не так. Попробуйте еще раз ввести число от 1 до 12'))
for key in seasons.keys():
    if month in seasons[key]:
        print('Номер месяца соответствует сезону - ', key)