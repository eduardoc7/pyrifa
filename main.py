import random


my_list_from_file = []
my_list_with_integers = []

with open('mylist.txt', 'r') as file:
    for line in file:
        if not line.strip():
            continue  # This skips blank lines
        line = line.split()  # to deal with blank
        my_list_from_file.append(line)

for values in my_list_from_file:
    for values_integers in values:
        my_list_with_integers.append(values_integers)

numeros_sortear = int(input("quantos numeros a pessoa compro: "))
if len(my_list_with_integers) >= numeros_sortear:
    numeros_sorteados = random.sample(
        my_list_with_integers, numeros_sortear)
    print(f'seus números de rifa: *{numeros_sorteados}*')

    for n in numeros_sorteados:
        my_list_with_integers.remove(n)

    with open('mylist.txt', 'w') as file:
        for n in my_list_with_integers:
            file.write(n + '\n')
else:
    print("lista vazia! os numeros a serem sorteados acabaram!")
