import random
import math


def tasks():
    print(
        """
        Ты зашел в задачник "Сложение и Вычитание

        Твой задача решить примеры, которые я дам!

        Чтобы остановить: "0"
        """
    )
    while True:
        strings = ['+', '-']

        bot_random_first_num = random.randint(1, 10000)
        bot_random_second_num = random.randint(1, 10000)
        bot_random_choice = random.choice(strings)
        print(f"{bot_random_first_num} {bot_random_choice} {bot_random_second_num} = ?")

        answer_bot = 0

        if bot_random_choice == "+":
            answer_bot = bot_random_first_num + bot_random_second_num
        elif bot_random_choice == "-":
            answer_bot = bot_random_first_num - bot_random_second_num

        answer_user = int(input("Введите ответ: "))

        if answer_user == 0:
            break

        if answer_user == answer_bot:
            print("Правильно\n")
        else:
            print("Неправильно\n")


def primeNumber():
    print(
        """
        Ты зашел, где можно узнать просто число или нет.

        Твой задача вводить число!

        Чтобы остановить: "0"
        """
    )

    while True:
        number_user = int(input("Введите число: "))

        if number_user == 0:
            break

        if number_user > 1:
            is_prime = True
            for i in range(2, int(number_user ** 0.5) + 1):
                if number_user % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print("Ваше число простое\n")
            else:
                print("Ваше число не простое\n")
        else:
            print("Ваше число не простое\n")


def squareRoot():
    print(
        """
        Ты зашел, где можно узнать квадратный корень.

        Твой задача вводить число!

        Чтобы остановить: "0"
        """
    )

    while True:
        square_user = int(input("Введите число: "))

        print(f"Корень числа {square_user} = {math.sqrt(square_user)}\n")

        if square_user == 0:
            break


while True:

    print(
                    """
                    Добро пожаловать
                    
                    Меня зовут, Аверий!
                    Я тебе помогу подтянуть знания
                    
                    Выбери что тебе нужно:
                    
                    1. Задачи на сложение и вычитание 
                    2. Простое число
                    3. Квадратный корень
                    """
    )

    choice_user = int(input("Напиши цифру: "))

    match choice_user:
        case 1:
            tasks()
        case 2:
            primeNumber()
        case 3:
            squareRoot()
