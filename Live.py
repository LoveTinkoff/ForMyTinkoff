#-*- coding: utf8 -*-

fish = ['░░░░░░░░░░░░░░░░░▄▄▄▄░░░░░░░░░░░░░░░░░░░', '░░░░░░░░░░░░░░▄█████▀░░░░░░░░░░░░░░░░░░░', '░░░░░░░░░░░▄████████░░░░░░░░░░░░░░░░░░░░', '░░░░░░░░░░▄██████████░░░░░░░░░░░░░░░░░░░', '░░░░░░░░░░▀░▄▄▄▄▄▄▄░░░░░░░░░░░░░░░░░░░▄▄', '░░░░░░░░░████████████▄▄░░░░░░░░░░░░▄████', '░░░░▄████▄▀█████████████▄░░░░░░░░░████▀░', '░▄▄███████▄░██████████████▄░░░░░░█████▄░', '▄████▄░████░▀████████████████▄▄▄████████', '▀██████████░▄████████████████▀▀▀████████', '░▀▀███████▀░██████████████▀░░░░░░█████▀░', '░░░░▀████▀░█████████████▀░░░░░░░░░████▄░', '░░░░░░░░░▄███████████▀▀░░░░░░░░░░░░▀▀███', '░░░░░░░░░░▄░▀▀▀▀▀▀▀░░░░░░░░░░░░░░░░░░░░░', '░░░░░░░░░░▀██████████░░░░░░░░░░░░░░░░░░░', '░░░░░░░░░░░▀████████░░░░░░░░░░░░░░░░░░░░']
rock = ['░░░░░░░░░░░░░▄██▀░░░░░░▀██▄░░░░░░░░░░░░░', '░░░░░░░░░░░░▄██▀░░░░░░░░▀██▄░░░░░░░░░░░░', '░░▄▄▄█████░░██▀░░░░░░░░░░▄▄▄▄▄█████▄▄▄░░', '░██▀▀▀▀▀▀▀░▄██░▄█▀░░▄▄█████▀▀▀▀▀▀▀▀▀▀██░', '██▀░░░░░░░░██▀░░▄▄███▀▀▀░░░██░░░░░░░░▀██', '██▄░░░░░░░░▀░▄███▀▀░░░▀██▄░██░░░░░░░░▄██', '░██░░░░░░░▄███▀░░░░░░░░░░▀░██▄░░░░░░░██░', '░▀██▄░░▄▄██▀░░░░░░▄▄▄▄░░░░░███░▄▄░░▄██▀░', '░░░███▄░▀▀▄▄█░░░░██████░░░░███░███▄░▀░░░', '░░░░▀███▄░▀██░░░░██████░░░░███░░▀███▄░░░', '░░▄█▄░▀███▄░░░░░░▀████▀░░░░███░█▄░▀██▄░░', '░██▀░░░░░▀██▄▄░░░░░░░░░░░░░███░░░░░░▀██░', '▄██░░░░░░░░▀▀██▄▄░░░░░░▄▄█░██░░░░░░░░██▄', '██░░░░░░░░░█▄░▀▀███▄▄░░▀▀░░██░░░░░░░░░██', '▀██░░░░░░░░███░▄▄░▀▀████▄░███░░░░░░░░██▀', '░▀████████░░██░░▀░░░░░▀▀░░██░░████████▀░']
shrimp = ['░░░░░░░░░░░░░░░░░░░▄▄░░░░░░░░░░░░░░░░░░░', '░░░░░░░░░░░░░░░░░▄████▄░░░░░░░░░░░░░░░░░', '░░░░░░░░░░░░░░▄▄████████▄▄░░░░░░░░░░░░░░', '░░░░░░░░░▄▄▄████████████████▄▄▄░░░░░░░░░', '░░░░▄██████████████████████████████▄░░░░', '░░░░██████████▄░░░▀██▀░░░▄██████████░░░░', '░░░░█████████████▄░░░░▄█████████████░░░░', '░░░░▀██████░░████▀░░░░▀████░░██████▀░░░░', '░░░░░███████░▀██▀░░░░░░▀██▀░▄██████░░░░░', '░░░░░███████▄▄░░░░░░░░░░░░▄▄███████░░░░░', '░░░░░▀██████▀▀▀░░░░░░░░░░▀▀▀██████▀░░░░░', '░░░░░░████░░▄▄▄░░░░░░░░░░▄▄▄░░████░░░░░░', '░░░░░░░██░▄███▀░░░░░░░░░░▀███▄░██░░░░░░░', '░░░░░░░▀█████░▄█▄░░░░░░▄█▄░█████▀░░░░░░░', '░░░░░░░░▀███░░████████████░░███▀░░░░░░░░', '░░░░░░░░░▀██▄██████████████▄██▀░░░░░░░░░']
nothing = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
items = []
items.append(fish)
items.append(rock)
items.append(shrimp)
items.append(nothing)

''' 
    Здравствуйте, проект я тестировал в Pycharm и очень долго дебажил вывод псевдографикой.
    Рекомендуемые настройки шрифта консоли для видимоти результата:
    Size: 4
    Line spacing: 0.6
    Как их поменять:
        File -> Settings... -> Editor -> Color Scheme -> Console Font
'''

def result(a):
    for i in range(8):  # бежим по строкам
        pr = []
        for j in range(8): # бежим по столбцам
            pr.append(a[i][j]) # сохраняем i - ую строку
        for i1 in range(0, 16): # выводим сначала все первые строки обитателей из этой строки, затем все вторые и т.д.
            for elem in pr: # бежим по текущей строке и в зависимости значения выводим обитателя
                if elem == 3: # чтобы симмитричность была идеальна (т.к. пробелы слишком худые, как символ) ...
                    print("{:^90}".format(items[elem][i1]), end = ' ') # ...пробелов нужно больше, чтобы сделать свободный сектор океана
                else:
                    print("{:^50}".format(items[elem][i1]), end = ' ') # выводим i1 - ую строку нужного обитателя
            print() # переходим на новыую строку, чтобы написать i1 + 1 - ые строки наших обитателей
        print() # переходим на следующий глобальные ряд обитателей
        print()
        print()
        print()

def clear():
    print("\n" * 50)

def NextGenetation(a):
    b = [[-1]* 10 for i in range(10)] # создаем клон массива a в рамке из -1, чтобы не было выходов за границу
    for i in range(8):
        for j in range(8):
            b[i + 1][j + 1] = a[i][j]
    next = [] # будем потиньхоньку заполнять наше следующее поле
    for i in range(1, 9):
        pr = []
        for j in range(1, 9):
            friends = [] # массив соседей данной клетки
            friends.append(b[i][j - 1])
            friends.append(b[i][j + 1])
            friends.append(b[i - 1][j])
            friends.append(b[i + 1][j])
            friends.append(b[i - 1][j - 1])
            friends.append(b[i - 1][j + 1])
            friends.append(b[i + 1][j - 1])
            friends.append(b[i + 1][j + 1]) # далее ифаем то, что сказано в условии
            if b[i][j] == 0: # рыба
                cnt = friends.count(0)
                if cnt > 3 or cnt < 2:
                    pr.append(3)
                elif cnt == 2 or cnt == 3:
                    pr.append(0)
            elif b[i][j] == 2: # креветка
                cnt = friends.count(2)
                if cnt > 3 or cnt < 2:
                    pr.append(3)
                elif cnt == 2 or cnt == 3:
                    pr.append(2)
            elif b[i][j] == 1: # камень
                pr.append(1)
            elif b[i][j] == 3: # свободная клетка
                if friends.count(0) == 3:
                    pr.append(0)
                elif friends.count(2) == 3:
                    pr.append(2)
                else:
                    pr.append(3)
        next.append(pr)
    return next


import random, time

field = [[random.randint(0, 3) for i in range(8)] for j in range(8)] # случайно зарождение первого поколения

while(1):
    result(field)
    field = NextGenetation(field)
    time.sleep(5)
    clear()

