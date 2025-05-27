def find_median(count, d):
    count_sum = 0
    if d % 2 == 1:
        median_pos = d // 2 + 1
        for i in range(201):
            count_sum += count[i]
            if count_sum >= median_pos:
                return i
    else:
        first = None
        second = None
        median_pos1 = d // 2
        median_pos2 = median_pos1 + 1
        for i in range(201):
            count_sum += count[i]
            if first is None and count_sum >= median_pos1:
                first = i
            if count_sum >= median_pos2:
                second = i
                break
        return (first + second) / 2

def activityNotifications(expenditure, d):
    notifications = 0
    count = [0] * 201

    for i in range(d):
        count[expenditure[i]] += 1

    for i in range(d, len(expenditure)):
        median = find_median(count, d)
        current_expense = expenditure[i]
        print(f"Dia {i+1}: gasto = {current_expense}, mediana = {median}")
        if current_expense >= 2 * median:
            print("🔔 Notificação enviada!")
            notifications += 1
        # Atualiza contagem
        count[expenditure[i - d]] -= 1
        count[expenditure[i]] += 1

    return notifications

def main():
    # Dados fixos do exemplo
    gastos = [2, 3, 4, 2, 3, 6, 8, 4, 5]
    d = 5
    print("Gastos:", gastos)
    print("Dias para média:", d)
    resultado = activityNotifications(gastos, d)
    print("Total de notificações:", resultado)

if __name__ == '__main__':
    main()
