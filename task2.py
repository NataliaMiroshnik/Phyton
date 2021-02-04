data = list(input('Введите список элементов через пробел').split())
copy_data = data.copy()
index = 0
if len(data) % 2 == 0:
    while index < len(data):
        copy_data[index] = data[index + 1]
        copy_data[index + 1] = data [index]
        index +=2
    print(copy_data)
else:
    while index < len(data) - 1:
        copy_data[index] = data[index + 1]
        copy_data[index + 1] = data [index]
        index +=2
    print(copy_data)