# Работа со словарями:
my_dict = {'Vasya': 'ул. Озёрная 21', 'Petya': 'ул. Югославская 32', 'Masha': 'ул. Ордженикидзе 12'}
print(my_dict)
print(my_dict['Vasya'])
print(my_dict.get('Glasha'))
my_dict.update({'Sasha': 'ул. Строителей 15', 'Georgy': 'ул. Ленина 56'})
a = my_dict.pop('Petya')
print(a)
print(my_dict)
# Работа с множествами:
my_set = {1, 1, 1, 1, 1, 'Яблоко', 'Яблоко', 'Яблоко', 42.314, 42.314}
print(my_set)
my_set.add(13)
my_set.add((5, 6, 1.6))
my_set.discard('Яблоко')
print(my_set)