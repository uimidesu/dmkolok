def MUL_ZM_Z(z):
    """
    Меняет знак на противоположный.
    """
    sign, n, A = z

    if n == 1 and A[0] == 0:
        return z
    return (1 - sign, n, A.copy())