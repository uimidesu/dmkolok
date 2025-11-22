"""
Модуль для работы с рациональными числами (дробями)
Рациональное число представлено как пара (числитель: Integer, знаменатель: Natural)
"""

from integer import *


class Rational:
    """Класс для представления рационального числа (дроби)"""
    
    def __init__(self, numerator, denominator=None):
        """
        Инициализация рационального числа
        numerator - числитель (Integer, int или строка)
        denominator - знаменатель (Natural, int или строка)
        """
        if denominator is None:
            if isinstance(numerator, str):
                if '/' in numerator:
                    parts = numerator.split('/')
                    if len(parts) != 2:
                        raise ValueError("Некорректный формат дроби")
                    numerator = parts[0].strip()
                    denominator = parts[1].strip()
                else:
                    denominator = "1"
            else:
                denominator = 1
        
        if isinstance(numerator, Integer):
            self.numerator = numerator.copy()
        elif isinstance(numerator, (int, str)):
            self.numerator = Integer(numerator)
        else:
            raise ValueError("Некорректный тип числителя")
        
        if isinstance(denominator, Natural):
            self.denominator = denominator.copy()
        elif isinstance(denominator, int):
            if denominator <= 0:
                raise ValueError("Знаменатель должен быть положительным")
            self.denominator = Natural(denominator)
        elif isinstance(denominator, str):
            self.denominator = Natural(denominator)
            if not NZER_N_B(self.denominator):
                raise ValueError("Знаменатель не может быть нулём")
        else:
            raise ValueError("Некорректный тип знаменателя")
        
        if not NZER_N_B(self.denominator):
            raise ValueError("Знаменатель не может быть нулём")
    
    def __str__(self):
        """Строковое представление дроби"""
        if str(self.denominator) == "1":
            return str(self.numerator)
        return f"{str(self.numerator)}/{str(self.denominator)}"
    
    def __repr__(self):
        return f"Rational({str(self)})"
    
    def copy(self):
        """Создание копии дроби"""
        return Rational(self.numerator.copy(), self.denominator.copy())


# Q-1: Сокращение дроби
def RED_Q_Q(a: Rational) -> Rational:
    """Сокращение дроби"""
    num_abs = ABS_Z_N(a.numerator)
    denom = a.denominator.copy()
    
    gcd = GCF_NN_N(num_abs, denom)
    
    new_numerator = DIV_ZZ_Z(a.numerator, TRANS_N_Z(gcd))
    new_denominator = DIV_NN_N(denom, gcd)
    
    return Rational(new_numerator, new_denominator)


# Q-2: Проверка сокращенного дробного на целое
def INT_Q_B(a: Rational) -> bool:
    """
    Проверка сокращенной дроби на целое
    Возвращает: True если рациональное число является целым, иначе False
    """
    return str(a.denominator) == "1"


# Q-3: Преобразование целого в дробное
def TRANS_Z_Q(a: Integer) -> Rational:
    """Преобразование целого в дробное"""
    return Rational(a.copy(), Natural([1]))


# Q-4: Преобразование сокращенного дробного в целое
def TRANS_Q_Z(a: Rational) -> Integer:
    """Преобразование сокращенной дроби в целое (если знаменатель равен 1)"""
    if not INT_Q_B(a):
        raise ValueError("Дробь не является целым числом")
    return a.numerator.copy()


# Q-5: Сложение дробей
def ADD_QQ_Q(a: Rational, b: Rational) -> Rational:
    """Сложение дробей"""
    lcm = LCM_NN_N(a.denominator, b.denominator)
    
    factor_a = DIV_NN_N(lcm, a.denominator)
    factor_b = DIV_NN_N(lcm, b.denominator)
    
    num_a = MUL_ZZ_Z(a.numerator, TRANS_N_Z(factor_a))
    num_b = MUL_ZZ_Z(b.numerator, TRANS_N_Z(factor_b))
    
    result_numerator = ADD_ZZ_Z(num_a, num_b)
    result_denominator = lcm
    
    result = Rational(result_numerator, result_denominator)
    return RED_Q_Q(result)


# Q-6: Вычитание дробей
def SUB_QQ_Q(a: Rational, b: Rational) -> Rational:
    """Вычитание дробей"""
    lcm = LCM_NN_N(a.denominator, b.denominator)
    
    factor_a = DIV_NN_N(lcm, a.denominator)
    factor_b = DIV_NN_N(lcm, b.denominator)
    
    num_a = MUL_ZZ_Z(a.numerator, TRANS_N_Z(factor_a))
    num_b = MUL_ZZ_Z(b.numerator, TRANS_N_Z(factor_b))
    
    result_numerator = SUB_ZZ_Z(num_a, num_b)
    result_denominator = lcm
    
    result = Rational(result_numerator, result_denominator)
    return RED_Q_Q(result)


# Q-7: Умножение дробей
def MUL_QQ_Q(a: Rational, b: Rational) -> Rational:
    """Умножение дробей"""
    result_numerator = MUL_ZZ_Z(a.numerator, b.numerator)
    result_denominator = MUL_NN_N(a.denominator, b.denominator)
    
    result = Rational(result_numerator, result_denominator)
    return RED_Q_Q(result)


# Q-8: Деление дробей
def DIV_QQ_Q(a: Rational, b: Rational) -> Rational:
    """Деление дробей (делитель отличен от нуля)"""
    if POZ_Z_D(b.numerator) == 0:
        raise ValueError("Деление на ноль")
    
    result_numerator = MUL_ZZ_Z(a.numerator, TRANS_N_Z(b.denominator))
    
    b_num_abs = ABS_Z_N(b.numerator)
    result_denominator = MUL_NN_N(a.denominator, b_num_abs)
    
    result = Rational(result_numerator, result_denominator)
    
    if b.numerator.sign == 1:
        result.numerator = MUL_ZM_Z(result.numerator)
    
    return RED_Q_Q(result)
