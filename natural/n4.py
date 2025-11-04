from n1 import COM_NN_D

def ADD_NN_N(a, b):
    """
    Складывает a и b.
    Возвращает сумму.
    """
    n1, A1 = a
    n2, A2 = b

    if COM_NN_D(a, b) == 1: # если a < b (чтобы дальнейший код работал верно)
        a, b = b, a
        n1, n2 = n2, n1
        A1, A2 = A2, A1

    #Дополняем меньшее число нулями слева
    A2 = [0] * (n1 - n2) + A2

    result = []
    carry = 0

    for i in range(n1 - 1, -1, -1):
        total = A1[i] + A2[i] + carry
        result.append(total % 10)
        carry = total // 10

    if carry:
        result.append(carry)

    result.reverse()
    return (len(result), result)