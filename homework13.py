S = 0
try:
    N = int(input("Введите количество посетителей, которых Вы хотите зарегистрировать: "))
except ValueError:
    print("Вы ввели некорректное количество посетителей")
else:
    if N <= 0:
        print("Вы ввели некорректное количество посетителей")
    else:
        for i in range(1, N + 1):
            age = int(input("Введите возраст посетителя конференции: "))
            if 1 <= age < 18:
                print("Вы проходите на конференцию бесплатно!")
            elif 18 <= age < 25:
                print("Стоимость билета составит 990 рублей")
                S = S + 990
            elif 25 <= age < 150:
                print("Стоимость билета составит 1390 рублей")
                S = S + 1390
            else:
                print("Вы ввели неправильный возраст!")
                break
    if N > 3:
        S = S - (S * 10 / 100)
    if S > 0 and N > 1:
        print("Общая сумма вашего заказа: ", S, " рублей")