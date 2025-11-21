"""
Модуль для работы с целыми числами
Целое число представлено как пара (знак, натуральное число)
знак: 0 - плюс, 1 - минус
"""

from natural import *


class Integer:
    """Класс для представления целого числа"""

    def __init__(self, value, sign=0):
        """
        Инициализация целого числа
        value - может быть строкой, числом или Natural
        sign - 0 для положительных, 1 для отрицательных
        """
        if isinstance(value, str):
            value = value.strip()
            if value.startswith('-'):
                self.sign = 1
                value = value[1:]
            elif value.startswith('+'):
                self.sign = 0
                value = value[1:]
            else:
                self.sign = 0

            self.abs_value = Natural(value)
        elif isinstance(value, int):
            if value < 0:
                self.sign = 1
                self.abs_value = Natural(-value)
            else:
                self.sign = 0
                self.abs_value = Natural(value)
        elif isinstance(value, Natural):
            self.sign = sign
            self.abs_value = value
        else:
            raise ValueError("Неподдерживаемый тип данных")

        if not NZER_N_B(self.abs_value):
            self.sign = 0

    def __str__(self):
        """Строковое представление числа"""
        if self.sign == 1 and NZER_N_B(self.abs_value):
            return f"-{str(self.abs_value)}"
        return str(self.abs_value)

    def __repr__(self):
        return f"Integer({str(self)})"

    def copy(self):
        """Создание копии числа"""
        return Integer(self.abs_value.copy(), self.sign)


# Z-1: Абсолютная величина числа
def ABS_Z_N(a: Integer) -> Natural:
    """Абсолютная величина целого числа, результат - натуральное"""
    return a.abs_value.copy()


# Z-2: Определение положительности числа
def POZ_Z_D(a: Integer) -> int:
    """
    Определение знака числа
    Возвращает: 2 - положительное, 0 - ноль, 1 - отрицательное
    """
    if not NZER_N_B(a.abs_value):
        return 0
    if a.sign == 0:
        return 2
    return 1


# Z-3: Умножение целого на (-1)
def MUL_ZM_Z(a: Integer) -> Integer:
    """Умножение целого на (-1)"""
    if not NZER_N_B(a.abs_value):
        return Integer(Natural([0]), 0)

    new_sign = 0 if a.sign == 1 else 1
    return Integer(a.abs_value.copy(), new_sign)


# Z-4: Преобразование натурального в целое
def TRANS_N_Z(a: Natural) -> Integer:
    """Преобразование натурального в целое"""
    return Integer(a.copy(), 0)


# Z-5: Преобразование целого неотрицательного в натуральное
def TRANS_Z_N(a: Integer) -> Natural:
    """Преобразование целого неотрицательного в натуральное"""
    if a.sign == 1:
        raise ValueError("Число должно быть неотрицательным")
    return a.abs_value.copy()


# Z-6: Сложение целых чисел
def ADD_ZZ_Z(a: Integer, b: Integer) -> Integer:
    """Сложение целых чисел"""
    a_pos = POZ_Z_D(a)
    b_pos = POZ_Z_D(b)

    if a_pos == 0:
        return b.copy()
    if b_pos == 0:
        return a.copy()

    a_abs = ABS_Z_N(a)
    b_abs = ABS_Z_N(b)

    if a.sign == b.sign:
        result_abs = ADD_NN_N(a_abs, b_abs)
        return Integer(result_abs, a.sign)
    else:
        cmp = COM_NN_D(a_abs, b_abs)

        if cmp == 0:
            return Integer(Natural([0]), 0)
        elif cmp == 2:
            result_abs = SUB_NN_N(a_abs, b_abs)
            return Integer(result_abs, a.sign)
        else:
            result_abs = SUB_NN_N(b_abs, a_abs)
            return Integer(result_abs, b.sign)


# Z-7: Вычитание целых чисел
def SUB_ZZ_Z(a: Integer, b: Integer) -> Integer:
    """Вычитание целых чисел"""
    b_negated = MUL_ZM_Z(b)
    return ADD_ZZ_Z(a, b_negated)


# Z-8: Умножение целых чисел
def MUL_ZZ_Z(a: Integer, b: Integer) -> Integer:
    """Умножение целых чисел"""
    a_pos = POZ_Z_D(a)
    b_pos = POZ_Z_D(b)

    if a_pos == 0 or b_pos == 0:
        return Integer(Natural([0]), 0)

    a_abs = ABS_Z_N(a)
    b_abs = ABS_Z_N(b)

    result_abs = MUL_NN_N(a_abs, b_abs)

    result_sign = 0 if a.sign == b.sign else 1

    return Integer(result_abs, result_sign)


# Z-9: Частное от деления целого на целое
def DIV_ZZ_Z(a: Integer, b: Integer) -> Integer:
    """Частное от деления целого на целое"""
    if POZ_Z_D(b) == 0:
        raise ValueError("Деление на ноль")

    a_abs = ABS_Z_N(a)
    b_abs = ABS_Z_N(b)

    quotient_abs = DIV_NN_N(a_abs, b_abs)

    if not NZER_N_B(quotient_abs):
        return Integer(Natural([0]), 0)

    result_sign = 0 if a.sign == b.sign else 1

    if result_sign == 1:
        remainder = MOD_NN_N(a_abs, b_abs)
        if NZER_N_B(remainder):
            quotient_abs = ADD_1N_N(quotient_abs)

    return Integer(quotient_abs, result_sign)


# Z-10: Остаток от деления целого на целое
def MOD_ZZ_Z(a: Integer, b: Integer) -> Integer:
    """Остаток от деления целого на целое"""
    if POZ_Z_D(b) == 0:
        raise ValueError("Деление на ноль")

    quotient = DIV_ZZ_Z(a, b)
    product = MUL_ZZ_Z(quotient, b)
    remainder = SUB_ZZ_Z(a, product)

    return remainder
