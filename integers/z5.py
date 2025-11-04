def TRANS_Z_N(z):
    """
    Только для z >= 0. Возвращает натуральное.
    """
    sign, n, A = z
    if sign == 1:
        raise ValueError("TRANS_Z_N: число отрицательное")
    return (n, A)