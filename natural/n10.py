from n1 import COM_NN_D
from n7 import MUL_Nk_N

def DIV_NN_Dk(a, b):
    """
    Возвращает (q, k), где q — первая цифра частного, k — позиция.
    """
    n1, A = a
    n2, B = b

    if n2 == 1 and B[0] == 0:
        raise ValueError("Нельзя делить на ноль")

    k = max(0, n1 - n2)

    # Пробуем q от 9 до 0
    for q in range(9, -1, -1):
        # q * b вручную
        temp = []
        carry = 0
        for i in range(n2 - 1, -1, -1):
            total = B[i] * q + carry
            temp.append(total % 10)
            carry = total // 10
        while carry:
            temp.append(carry % 10)
            carry //= 10
        temp.reverse()
        temp = (len(temp), temp)

        candidate = MUL_Nk_N(temp, k)

        if COM_NN_D(candidate, a) != 1:  #если candidate <= a
            return q, k

    return 0, k  # a < b