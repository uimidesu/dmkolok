from n1 import COM_NN_D
from n5 import SUB_NN_N
from n6 import MUL_ND_N

def SUB_NDN_N(a, b, d):
    """
    Вычисляет a - (b * d), если результат  0.
    Иначе — ValueError.
    """
    if not 0 <= d <= 9:
        raise ValueError("SUB_NDN_N: d - должно быть цифрой")

    temp = MUL_ND_N(b, d)
    if COM_NN_D(a, temp) == 1:  # a < b*d
        raise ValueError("SUB_NDN_N: результат отрицательный")

    return SUB_NN_N(a, temp)