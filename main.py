try:
    ticket_count = int(input("Введите кол-во билетов: "))
    if ticket_count <= 0:
        raise ValueError
    tickets = {}
    for i in range(ticket_count):
        age = int(input(f"Введите возраст посетителя для {i + 1} билета: "))
        coast = None
        if 0 <= age < 18:
            coast = 0
        elif 18 <= age < 25:
            coast = 990
        elif age >= 25:
            coast = 1390
        else:
            raise ValueError
        tickets.update({age: coast})
    tickets_sum = sum(tickets.values())
    if ticket_count > 3:
        tickets_sum *= 0.9
        print(f"Сумма к оплате с учётом скидки 10% : {tickets_sum} руб.")
    else:
        print(f"Сумма к оплате : {tickets_sum} руб.")
except ValueError:
    print("Вы ввели некорректное значение. Запустите программу снова и введите другое значение")
