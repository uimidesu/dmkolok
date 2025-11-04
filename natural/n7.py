def MUL_Nk_N(a, k):
    """
    Умножает число на 10^k.
    Добавляет k нулей в конец.
    """
    if k < 0:
        raise ValueError("MUL_Nk_N: k < 0")
    if k == 0:
        return a

    n, A = a
    A.extend([0] * k)
    return (n + k, A)