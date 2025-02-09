import random
import math


def guessTheNumber():
    print(
        """
        Добро пожаловать в игру "Угадай число"
        Ваша задача отгадать число, которое
        загадал наш бот - Аверий!

        Диапазон от 1 до 100 

        Бот - Аверий: "Привет я загадал число = **"
        """
    )

    number_bot_random = random.randint(1, 99)

    while True:
        number_user = int(input("Введите вашу догадку: "))

        if number_user > number_bot_random:
            print("Ваше число больше загаданного, берите меньше!")
        elif number_user == number_bot_random:
            print(f"Ура вы угадали, Аверий загадал - {number_bot_random}")
            break
        elif number_user < number_bot_random:
            print("Ваше число меньше загаданного, берите выше!")


def sortingList():
    print(
        """
        Добро пожаловать в игру "Сортировка списка"
        Ваша задача написать любые цифры / числа.
        И бот - Аверий, поможет сортировать ваши 
        числа.

        Чтобы закончить писать числа, напишите "0" 
        """
    )

    numbers_list = []

    while True:
        enter_numbers = int(input("Введите цифры / числа: "))

        numbers_list.append(enter_numbers)

        if enter_numbers == 0:
            print(f"Ваш список - {numbers_list}")
            print(f"Сортированный список: {sorted(numbers_list)}")
            break


def factorial():
    print(
        """
        Добро пожаловать в игру "Факториал"
        Ваша задача написать любое число.
        И бот - Аверий, поможет найти 
        факториал вашего числа!
        """
    )

    factorial_user = int(input("Введите любое число: "))
    print(f"Факториал числа {factorial_user} равен {math.factorial(factorial_user)}")


def fibonacciNumbers():
    print(
        """
        Добро пожаловать в игру "Числа Фибоначчи"
        Ваша задача написать число!

        Бот найдет числа Фибоначчи!
        """
    )

    fibonacci_numbers = int(input("Введите число: "))

    fib_sequence = [0, 1]

    while fib_sequence[-1] < fibonacci_numbers:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)

    fib_sequence = [num for num in fib_sequence if num <= fibonacci_numbers]

    print("Числа Фибоначчи до", fibonacci_numbers, ":", fib_sequence)


while True:
    print(
                """
                Выберите, во что будем играть:
                
                1. Угадай число
                2. Сортировка списка
                3. Факториал
                4. Числа Фибоначчи 
                5. Выход
                """
    )

    choice_game = int(input("Напишите цифру: "))

    match choice_game:
        case 1:
            guessTheNumber()
        case 2:
            sortingList()
        case 3:
            factorial()
        case 4:
            fibonacciNumbers()
        case 5:
            print("Всего доброго!")
            break
