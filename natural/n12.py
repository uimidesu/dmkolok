from n9 import SUB_NDN_N
from n11 import DIV_NN_N

def MOD_NN_N(a, b):
    """
    a mod b = a - (a // b) * b
    Умножение q * b реализовано через q-разовое SUB_NDN_N(..., b, 1)
    """
    coef = DIV_NN_N(a, b)
    per = a

    # q * b
    q_value = 0
    for d in coef[1][::-1]:  # с младшего
        q_value = q_value * 10 + d

    for _ in range(q_value):
        try:
            per = SUB_NDN_N(per, b, 1)
        except:
            break

    return per