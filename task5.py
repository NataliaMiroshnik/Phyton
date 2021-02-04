my_list = [7, 5, 3, 3, 2]
my_list += [int(i) for i in input('введите натуральное число').split()]
my_list= sorted(my_list)
print(my_list[::-1])