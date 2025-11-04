from n1 import COM_NN_D

def SUB_NN_N(a, b):
    """
    Вычитает b из a (a >= b).
    Возвращает разность.
    """
    if COM_NN_D(a, b) == 1:
        raise ValueError("SUB_NN_N: a < b")

    n1, A1 = a
    n2, A2 = b
    A2 = [0] * (n1 - n2) + A2

    result = []
    borrow = 0 #заём впереди стоящего разряда

    for i in range(n1 - 1, -1, -1):
        diff = A1[i] - A2[i] - borrow
        if diff < 0:
            diff += 10
            borrow = 1
        else:
            borrow = 0
        result.append(diff)

    result.reverse()

    while len(result) > 1 and result[0] == 0:
        result.pop(0)

    return (len(result), result)