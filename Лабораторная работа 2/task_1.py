money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months = 0  # Количество месяцев без долгов

while True:
    ostatok = spend - salary
    if ostatok > money_capital:
        break  # Выход из цикла при выполнении условия

    months += 1
    money_capital -= ostatok
    spend *= 1 + increase

print("Количество месяцев, которое можно протянуть без долгов:", months)
