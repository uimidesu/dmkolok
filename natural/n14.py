from n8 import MUL_NN_N
from n13 import GCF_NN_N

from n1 import COM_NN_D  #для сравнения в цикле

def LCM_NN_N(a, b):
    """
    Вычисляет НОК(a, b).
    Если a или b = 0 → возвращаем 0.

    Алгоритм
    --------
    1. Вычисляем g = НОД(a, b).
    2. Вычисляем p = a * b.
    3. Делим p / g: повторно вычитаем g из p, считая количество вычитаний.
    """
    # Нулевые случаи
    n1, A = a
    n2, B = b
    if n1 == 1 and a[1][0] == 0 or n2 == 1 and b[1][0] == 0:
        return (1, [0])

    g = GCF_NN_N(a, b)
    p = MUL_NN_N(a, b)

    result = (1, [0])

    temp = p
    while COM_NN_D(temp, g) in (0, 2):  #temp >= g
        # temp = temp - g
        temp_n, temp_A = temp
        g_n, g_A = g
        g_A = [0] * (temp_n - g_n) + g_A if temp_n > g_n else g_A

        borrow = 0
        new_A = []
        for i in range(temp_n - 1, -1, -1):
            diff = temp_A[i] - g_A[i] - borrow if i < len(g_A) else temp_A[i] - borrow
            if diff < 0:
                diff += 10
                borrow = 1
            else:
                borrow = 0
            new_A.append(diff)
        new_A.reverse()
        while len(new_A) > 1 and new_A[0] == 0:
            new_A.pop(0)
        temp = (len(new_A), new_A)

        #result += 1
        res_n, res_A = result
        i = res_n - 1
        carry = 1
        while carry and i >= 0:
            if res_A[i] < 9:
                res_A[i] += 1
                carry = 0
            else:
                res_A[i] = 0
                i -= 1
        if carry:
            res_A.insert(0, 1)
            res_n += 1
        result = (res_n, res_A)

    return result