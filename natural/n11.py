from n9 import SUB_NDN_N
from n10 import DIV_NN_Dk

def DIV_NN_N(a, b):
    n1, A = a
    n2, B = b

    if n2 == 1 and b[1][0] == 0:
        raise ValueError("Нельзя делить на ноль")

    if n1 < n2:
        return (1, [0])

    result = []
    per = (0, [])

    for i in range(n1):
        #Добавляем цифру
        per = (per[0] + 1, [A[i]] + per[1])

        #Убираем ведущие нули
        while per[0] > 1 and per[1][0] == 0:
            per = (per[0] - 1, per[1][1:])

        # Если per < b
        is_less = per[0] < n2
        if not is_less and per[0] == n2:
            is_less = True
            for j in range(n2):
                if per[1][j] != b[1][j]:
                    is_less < b[1][j]
                    break
            else:
                is_less = False

        if is_less:
            if result:
                result.append(0)
            continue

        q, _ = DIV_NN_Dk(per, b)
        result.append(q)

        # Вычитаем q * b через SUB_NDN_N
        try:
            per = SUB_NDN_N(per, b, q)
        except ValueError:
            per = (1, [0])

    while len(result) > 1 and result[0] == 0:
        result.pop(0)

    return (len(result), result)