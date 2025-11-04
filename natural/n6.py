def MUL_ND_N(a, d):
    """
    Умножает число на цифру d.
    Изменяет список на месте.
    """
    if not 0 <= d <= 9:
        raise ValueError("MUL_ND_N: d - должно быть цифрой")

    n, A = a
    if d == 0:
        return (1, [0])

    result = []
    carry = 0 #перенос

    for i in range(n - 1, -1, -1):
        total = A[i] * d + carry
        result.append(total % 10)
        carry = total // 10

    while carry:
        result.append(carry % 10)
        carry //= 10

    result.reverse()
    return (len(result), result)