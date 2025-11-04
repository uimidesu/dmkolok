def COM_NN_D(a, b):
    """
    Сравнивает два натуральных числа.
    Возвращает:
        2 — если a > b
        0 — если a == b
        1 — если a < b
    """
    n1, A1 = a
    n2, A2 = b

    #Убираем ведущие нули
    while n1 > 1 and A1[n1-1] == 0:
        n1 -= 1
    while n2 > 1 and A2[n2-1] == 0:
        n2 -= 1

    #Сравниваем числа по номеру старшей позиции
    if n1 > n2:
        return 2
    if n1 < n2:
        return 1

    # Сравниваем цифры
    for i in range(n1 - 1, -1, -1):
        if A1[i] > A2[i]:
            return 2
        if A1[i] < A2[i]:
            return 1
        
    return 0