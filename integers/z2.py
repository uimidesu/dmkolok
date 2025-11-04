def SGN_Z_D(z):
    """
    Возвращает:
         1 - если z > 0
         0 - если z = 0
        -1 - если z < 0
    """
    sign, n, A = z
    if n == 1 and A[0] == 0:
        return 0
    return 1 if sign == 0 else -1