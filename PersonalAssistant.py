while True:
    print("\nВыбирай опцию: "
          "\n1. Конвертер температур"
          "\n2. Калькулятор"
          "\n3. Проверка на палиндром"
          "\n4. Определение четности"
          "\n5. Сумма цифр")

    choice_user = int(input("\nНапишите номер опции -> "))

    match choice_user:
        case 1:
            print(
                "\nПрограмма запрашивает у тебя, какую температуру ты хочешь конвертировать, и выполнит соответствующий расчет.")

            while True:
                print("\nВыбирай температуру:\n1.Фаренгейта\n2.Кельвин\n3.Цельсия\n4.Назад")
                from_degree = int(input("\nВыбери какую температуру ты хочешь конвертировать -> "))

                if from_degree == 4:
                    break
                else:
                    who_degree = int(input(f"Напишите значение температуры -> "))

                match from_degree:
                    case 1:
                        result_for_celsius = (who_degree - 32) * (5 / 9)
                        result_for_kelvin = ((who_degree - 32) * (5 / 9)) + 273.15
                        print(f"\nФаренгейта: {who_degree} = Цельсия: {round(result_for_celsius, 4)}")
                        print(f"Фаренгейта: {who_degree} = Кельвин: {round(result_for_kelvin, 3)}")
                    case 2:
                        result_for_fahrenheit = (who_degree - 273.15) * (9 / 5) + 32
                        result_for_celsius_kelvin = (who_degree - 273.15)
                        print(f"\nКельвин: {who_degree} = Фаренгейта: {round(result_for_fahrenheit, 2)}")
                        print(f"Кельвин: {who_degree} = Цельсия: {round(result_for_celsius_kelvin, 2)}")
                    case 3:
                        result_for_kelvin_celsius = (who_degree + 273.15)
                        result_for_fahrenheit_celsius = (who_degree * (9 / 5)) + 32
                        print(f"\nЦельсия: {who_degree} = Кельвин: {round(result_for_kelvin_celsius, 2)}")
                        print(f"Цельсия: {who_degree} = Фаренгейта: {round(result_for_fahrenheit_celsius, 2)}")
                    case 4:
                        break
        case 2:
            print("\nТы можешь выполнять основные арифметические операции.")

            number_first = int(input("\nВведите первое число -> "))
            number_second = int(input("Введите второе число -> "))

            while True:
                print("\nВыбирай операцию:\n1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление\n5. Назад")
                choice_operation = int(input("\nНапишите цифру операции -> "))

                match choice_operation:
                    case 1:
                        print(f"\nСложение: {number_first} + {number_second} = {number_first + number_second}")
                    case 2:
                        print(f"Вычитание: {number_first} - {number_second} = {number_first - number_second}")
                    case 3:
                        print(f"Умножение: {number_first} * {number_second} = {number_first * number_second}")
                    case 4:
                        print(f"Деление: {number_first} / {number_second} = {number_first // number_second}")
                    case 5:
                        break
        case 3:
            print("\nТы можешь ввести строку, и программа проверит, является ли строка палиндромом.")

            text_user = input("Введите любой текст: ")
            text_user_lower = text_user.lower()
            print(f"Ваш текст является ли палиндромом: {text_user_lower == text_user_lower[::-1]}")
        case 4:
            print("\nПрограмма позволяет пользователю вводить числа и определяет их четность")

            number_user = int(input("\nВведите любое число: "))

            if number_user % 2 == 0:
                print('\nВаше число: Четное')
            if number_user % 2 != 0:
                print('\nВаше число: Нечетное')
        case 5:
            print("\nТы можешь ввести число, и программа выведет сумму его цифр.")

            numbers_user = int(input('\nНапиши любое число: '))

            summ = 0

            while numbers_user > 0:
                num = numbers_user % 10
                summ = summ + num
                numbers_user = numbers_user // 10

            print("Сумма:", summ)
