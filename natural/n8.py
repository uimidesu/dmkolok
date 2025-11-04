from n4 import ADD_NN_N
from n6 import MUL_ND_N
from n7 import MUL_Nk_N

def MUL_NN_N(a, b):
    """
    Умножает a на b.
    """
    n1, A = a
    n2, B = b
    result = (1, [0])  # 0

    for i in range(n2):
        digit = B[n2 - 1 - i]
        temp = MUL_ND_N(a, digit)        # a * digit
        temp = MUL_Nk_N(temp, i)         # сдвиг на 10^i
        result = ADD_NN_N(result, temp)

    return result