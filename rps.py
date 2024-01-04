#  Реализуйте серию из n игр "Камень, ножницы, бумага" с компьютером. В результате выведите статистику:
#  сколько игр выиграл пользователь, сколько раз каждого вида ходов было выбрано.
#  Дополните игру анализом компьютера ваших ходов и выбор наиболее подходящего против вас хода.
import random
try:
    games = int(input("Введите количество игр: "))
    win = 0
    lose = 0
    draw = 0
    paper = 0
    rock = 0
    scissors = 0

    while games <= 0:
        print("ошибка, введено число меньше или равное нулю 0: ")
        games = int(input("Введите количество игр: "))

    for i in range(1, games+1):
        print("камень= 1")
        print("ножницы= 2")
        print("бумага= 3")
        print("     ")
        P1 =int(input("Введте ход: "))
        while P1 <= 0 or P1 > 3:
            print("ошибка, хода не существует")
            P1 =int(input("Введте ход: "))
        P2 = random.randint(1, 3)
        if rock >= 3:
            P2 = 3
        elif paper >= 3:
            P2 = 2
        elif scissors >= 3:
            P2 = 1
        print("Компьютер выбрал: ", P2)
        if P1 == P2:
            print("ничья")
            draw += 1
        # камень
        if P1 == 1 and P2 == 3:
            print("проигрыш")
            lose += 1
        elif P1 == 1 and P2 == 2:
            print("выигрыш")
            win += 1
            rock += 1
        # бумага
        if P1 == 3 and P2 == 2:
            print("проигрыш")
            lose += 1
        elif P1 == 3 and P2 == 1:
            print("выигрыш")
            win += 1
            paper += 1
        # ножницы
        if P1 == 2 and P2 == 1:
            print("проигрыш")
            lose += 1
        elif P1 == 2 and P2 == 3:
            print("выигрыш")
            win += 1
            scissors += 1
        print("")
        #статистика
    print("__статистика__")
    print("количество побед", win)
    print("количество неудач", lose)
    print("количество ничей", draw)
except ValueError:
    print("введено не число ")


