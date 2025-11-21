"""
Модуль для работы с натуральными числами (длинная арифметика)
Натуральное число представлено как список цифр от младших к старшим разрядам
Например: 123 = [3, 2, 1]
"""


class Natural:
    """Класс для представления натурального числа"""

    def __init__(self, value):
        """Инициализация натурального числа из строки или числа"""
        if isinstance(value, str):
            value = value.strip()
            if not value or not value.isdigit():
                raise ValueError("Некорректный ввод")
            self.digits = [int(d) for d in reversed(value)]
        elif isinstance(value, int):
            if value < 0:
                raise ValueError("Натуральное число не может быть отрицательным")
            self.digits = [int(d) for d in reversed(str(value))]
        elif isinstance(value, list):
            self.digits = value.copy()
        else:
            raise ValueError("Неподдерживаемый тип данных")

        self._normalize()

    def _normalize(self):
        """Удаление ведущих нулей"""
        while len(self.digits) > 1 and self.digits[-1] == 0:
            self.digits.pop()

    def __str__(self):
        """Строковое представление числа"""
        return ''.join(str(d) for d in reversed(self.digits))

    def __repr__(self):
        return f"Natural({str(self)})"

    def copy(self):
        """Создание копии числа"""
        return Natural(self.digits.copy())


# N-1: Сравнение натуральных чисел
def COM_NN_D(a: Natural, b: Natural) -> int:
    """
    Сравнение натуральных чисел
    Возвращает: 2 если a > b, 0 если a == b, 1 если a < b
    """
    if len(a.digits) > len(b.digits):
        return 2
    if len(a.digits) < len(b.digits):
        return 1

    for i in range(len(a.digits) - 1, -1, -1):
        if a.digits[i] > b.digits[i]:
            return 2
        if a.digits[i] < b.digits[i]:
            return 1

    return 0


# N-2: Проверка на ноль
def NZER_N_B(a: Natural) -> bool:
    """
    Проверка на ноль
    Возвращает: True если число не равно нулю, False если равно нулю
    """
    return not (len(a.digits) == 1 and a.digits[0] == 0)


# N-3: Добавление 1 к натуральному числу
def ADD_1N_N(a: Natural) -> Natural:
    """Добавление 1 к натуральному числу"""
    result = a.copy()
    carry = 1

    for i in range(len(result.digits)):
        result.digits[i] += carry
        if result.digits[i] < 10:
            carry = 0
            break
        result.digits[i] = 0

    if carry:
        result.digits.append(1)

    return result


# N-4: Сложение натуральных чисел
def ADD_NN_N(a: Natural, b: Natural) -> Natural:
    """Сложение натуральных чисел"""
    max_len = max(len(a.digits), len(b.digits))
    result_digits = []
    carry = 0

    for i in range(max_len):
        digit_a = a.digits[i] if i < len(a.digits) else 0
        digit_b = b.digits[i] if i < len(b.digits) else 0

        total = digit_a + digit_b + carry
        result_digits.append(total % 10)
        carry = total // 10

    if carry:
        result_digits.append(carry)

    return Natural(result_digits)


# N-5: Вычитание из первого большего натурального числа второго меньшего или равного
def SUB_NN_N(a: Natural, b: Natural) -> Natural:
    """Вычитание натуральных чисел (a >= b)"""
    if COM_NN_D(a, b) == 1:
        raise ValueError("Первое число должно быть больше или равно второму")

    result_digits = a.digits.copy()
    borrow = 0

    for i in range(len(b.digits)):
        result_digits[i] -= b.digits[i] + borrow

        if result_digits[i] < 0:
            result_digits[i] += 10
            borrow = 1
        else:
            borrow = 0

    i = len(b.digits)
    while borrow and i < len(result_digits):
        result_digits[i] -= borrow
        if result_digits[i] < 0:
            result_digits[i] += 10
            borrow = 1
        else:
            borrow = 0
        i += 1

    return Natural(result_digits)


# N-6: Умножение натурального числа на цифру
def MUL_ND_N(a: Natural, d: int) -> Natural:
    """Умножение натурального числа на цифру (0-9)"""
    if not 0 <= d <= 9:
        raise ValueError("d должно быть цифрой от 0 до 9")

    if d == 0:
        return Natural([0])

    result_digits = []
    carry = 0

    for digit in a.digits:
        product = digit * d + carry
        result_digits.append(product % 10)
        carry = product // 10

    if carry:
        result_digits.append(carry)

    return Natural(result_digits)


# N-7: Умножение натурального числа на 10^k
def MUL_Nk_N(a: Natural, k: int) -> Natural:
    """Умножение натурального числа на 10^k"""
    if k < 0:
        raise ValueError("k должно быть неотрицательным")

    if k == 0:
        return a.copy()

    result_digits = [0] * k + a.digits.copy()
    return Natural(result_digits)


# N-8: Умножение натуральных чисел
def MUL_NN_N(a: Natural, b: Natural) -> Natural:
    """Умножение натуральных чисел"""
    result = Natural([0])

    for i, digit in enumerate(b.digits):
        temp = MUL_ND_N(a, digit)
        temp = MUL_Nk_N(temp, i)
        result = ADD_NN_N(result, temp)

    return result


# N-9: Вычитание из натурального другого натурального, умноженного на цифру
def SUB_NDN_N(a: Natural, b: Natural, d: int) -> Natural:
    """Вычитание из a произведения b*d"""
    product = MUL_ND_N(b, d)

    if COM_NN_D(a, product) == 1:
        raise ValueError("Результат вычитания отрицательный")

    return SUB_NN_N(a, product)


# N-10: Вычисление первой цифры деления
def DIV_NN_Dk(a: Natural, b: Natural) -> tuple:
    """
    Вычисление первой цифры деления a на b
    Возвращает: (цифра, позиция k)
    """
    if not NZER_N_B(b):
        raise ValueError("Деление на ноль")

    cmp = COM_NN_D(a, b)
    if cmp == 1:
        return (0, 0)

    k = len(a.digits) - len(b.digits)
    divisor = MUL_Nk_N(b, k)

    if COM_NN_D(a, divisor) == 1:
        k -= 1
        if k < 0:
            return (0, 0)
        divisor = MUL_Nk_N(b, k)

    digit = 0
    temp = a.copy()
    while COM_NN_D(temp, divisor) != 1:
        digit += 1
        temp = SUB_NN_N(temp, divisor)

    return (digit, k)


# N-11: Неполное частное от деления
def DIV_NN_N(a: Natural, b: Natural) -> Natural:
    """Неполное частное от деления a на b"""
    if not NZER_N_B(b):
        raise ValueError("Деление на ноль")

    cmp = COM_NN_D(a, b)
    if cmp == 1:
        return Natural([0])
    if cmp == 0:
        return Natural([1])

    quotient_digits = [0] * (len(a.digits) - len(b.digits) + 1)
    remainder = a.copy()

    while COM_NN_D(remainder, b) != 1:
        digit, k = DIV_NN_Dk(remainder, b)
        if digit == 0:
            break
        quotient_digits[k] = digit

        temp = MUL_ND_N(b, digit)
        temp = MUL_Nk_N(temp, k)
        remainder = SUB_NN_N(remainder, temp)

    return Natural(quotient_digits)


# N-12: Остаток от деления
def MOD_NN_N(a: Natural, b: Natural) -> Natural:
    """Остаток от деления a на b"""
    if not NZER_N_B(b):
        raise ValueError("Деление на ноль")

    quotient = DIV_NN_N(a, b)
    product = MUL_NN_N(quotient, b)
    remainder = SUB_NN_N(a, product)

    return remainder


# N-13: НОД натуральных чисел
def GCF_NN_N(a: Natural, b: Natural) -> Natural:
    """НОД натуральных чисел (алгоритм Евклида)"""
    a_copy = a.copy()
    b_copy = b.copy()

    while NZER_N_B(b_copy):
        temp = MOD_NN_N(a_copy, b_copy)
        a_copy = b_copy
        b_copy = temp

    return a_copy


# N-14: НОК натуральных чисел
def LCM_NN_N(a: Natural, b: Natural) -> Natural:
    """НОК натуральных чисел"""
    gcd = GCF_NN_N(a, b)
    product = MUL_NN_N(a, b)
    lcm = DIV_NN_N(product, gcd)

    return lcm
