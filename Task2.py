# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все
# конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"
from random import randint, random

def players(play):
    first_name = input("\nВведите имя первого игрока: ")
    if play == 1:
        second_name = input("Введите имя бота игрока: ") + ' (bot)'
    else:
        second_name = input("Введите имя второго игрока: ")

    print(f"\nПривет {first_name} и {second_name}")
    player = [first_name, second_name]

    if randint(0,1) != 0:
        player[0], player[1] = player[1], player[0]
    return player

def game(player):
    candies = 100
    count_first = 0
    count_second = 0
    flag = player[0]

    print(f'\nПравила игры...\nНа столе лежит {candies} конфет.\nИгрок за один ход может забрать не более чем 28 конфет\nВсе конфеты оппонента достаются сделавшему последний ход.\n')
    print(f"Благодаря жеребьевке игрок {player[0]} ходит первым.\n")

    while candies > 0:
        if '(bot)' in flag:
            taken_sweets = candies if candies < 29 else 28
            if candies < 57 and candies > 29:
                taken_sweets = 28 - (57 - candies) if random() < 0.7 else 28 - (56 - candies)
            print(f'Бот забирает {taken_sweets} конфет.')
        else:    
            taken_sweets = int(input(f'Игрок {flag} ходит: '))
        
        if taken_sweets > 28 or taken_sweets < 0 or taken_sweets > candies:
            print("Вы ввели неверное значение!!!\nПовторите заново!!!\n")
            continue
        
        candies -= taken_sweets
        if flag == player[0]:
            count_first += taken_sweets
            flag = player[1]
        else:
            count_second += taken_sweets
            flag = player[0]
        print(f'Осталось {candies} конфет.\n')
    
    if flag == player[1]:
        return f'Игрок {player[0]} выиграл. Собрав конфет в количестве {count_first}, а аппонент собрал {count_second}.'
    else:
        return f'Игрок {player[1]} выиграл. Собрав конфет в количестве {count_second}, а аппонент собрал {count_first}.'

print("Добрый день. Добро пожаловать в нашу игру.")
player = int(input("Укажите пожалуйста. Игра на двоих (цифра 2). Игра против бота (цифра 1): "))
print(game(players(player)))
