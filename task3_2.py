month = int(input('Введите номер месяца от 1 до 12'))
winter = (1, 2, 12)
spring = (3, 4, 5)
summer = (6, 7, 8)
fall = (9, 10, 11)
while month == 0 or month > 12:
    month = int(input('Что-то пошло не так. Попробуйте еще раз ввести число от 1 до 12'))
if month in winter:
    print('Номер месяца соответствует зиме')
elif month in spring:
    print('Номер месяца соответствует весне')
elif month in summer:
    print('Номер месяца соответствует лету')
else:
    print('Номер месяца соответствует осени')
