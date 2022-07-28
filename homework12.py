per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("Введите сумму, которую хотите положить в банк под проценты: "))
sum_1 = round(money*(per_cent['ТКБ'])/100)
sum_2 = round(money*(per_cent['СКБ'])/100)
sum_3 = round(money*(per_cent['ВТБ'])/100)
sum_4 = round(money*(per_cent['СБЕР'])/100)
deposit = [sum_1, sum_2, sum_3, sum_4]
x = deposit.index(max(deposit))
print("Самые выгодные для Вас условия - в банке %s" % list(per_cent)[x])
print("Максимальная сумма, которую Вы cможете заработать за 1 год —", max(deposit), "рублей")
