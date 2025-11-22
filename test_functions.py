"""
Тестирование основных функций системы компьютерной алгебры
"""

from polynomial import *

def test_natural():
    print("=== Тестирование натуральных чисел ===")
    
    a = Natural("123")
    b = Natural("45")
    
    print(f"a = {a}")
    print(f"b = {b}")
    
    print(f"Сравнение: {COM_NN_D(a, b)} (2 = a>b, 0 = a==b, 1 = a<b)")
    print(f"Проверка на ноль a: {NZER_N_B(a)}")
    print(f"a + 1 = {ADD_1N_N(a)}")
    print(f"a + b = {ADD_NN_N(a, b)}")
    print(f"a - b = {SUB_NN_N(a, b)}")
    print(f"a * b = {MUL_NN_N(a, b)}")
    print(f"a / b = {DIV_NN_N(a, b)}")
    print(f"a % b = {MOD_NN_N(a, b)}")
    print(f"НОД(a, b) = {GCF_NN_N(a, b)}")
    print(f"НОК(a, b) = {LCM_NN_N(a, b)}")
    print()

def test_integer():
    print("=== Тестирование целых чисел ===")
    
    a = Integer("15")
    b = Integer("-7")
    
    print(f"a = {a}")
    print(f"b = {b}")
    
    print(f"|a| = {ABS_Z_N(a)}")
    print(f"Знак a: {POZ_Z_D(a)} (2 = плюс, 0 = ноль, 1 = минус)")
    print(f"a * (-1) = {MUL_ZM_Z(a)}")
    print(f"a + b = {ADD_ZZ_Z(a, b)}")
    print(f"a - b = {SUB_ZZ_Z(a, b)}")
    print(f"a * b = {MUL_ZZ_Z(a, b)}")
    print(f"a / b = {DIV_ZZ_Z(a, b)}")
    print(f"a % b = {MOD_ZZ_Z(a, b)}")
    print()

def test_rational():
    print("=== Тестирование рациональных чисел ===")
    
    a = Rational("3/4")
    b = Rational("5/6")
    
    print(f"a = {a}")
    print(f"b = {b}")
    
    print(f"Сокращение a: {RED_Q_Q(a)}")
    print(f"a целое?: {INT_Q_B(a)}")
    print(f"a + b = {ADD_QQ_Q(a, b)}")
    print(f"a - b = {SUB_QQ_Q(a, b)}")
    print(f"a * b = {MUL_QQ_Q(a, b)}")
    print(f"a / b = {DIV_QQ_Q(a, b)}")
    print()

def test_polynomial():
    print("=== Тестирование многочленов ===")
    
    p1 = Polynomial([Rational(1), Rational(2), Rational(3)])
    p2 = Polynomial([Rational(1), Rational(1)])
    
    print(f"p1 = {p1}")
    print(f"p2 = {p2}")
    
    print(f"Степень p1: {DEG_P_N(p1)}")
    print(f"Старший коэф. p1: {LED_P_Q(p1)}")
    print(f"p1 + p2 = {ADD_PP_P(p1, p2)}")
    print(f"p1 - p2 = {SUB_PP_P(p1, p2)}")
    print(f"p1 * p2 = {MUL_PP_P(p1, p2)}")
    print(f"p1 / p2 = {DIV_PP_P(p1, p2)}")
    print(f"p1 % p2 = {MOD_PP_P(p1, p2)}")
    print(f"Производная p1: {DER_P_P(p1)}")
    print()

if __name__ == "__main__":
    print("Тестирование системы компьютерной алгебры\n")
    
    try:
        test_natural()
        test_integer()
        test_rational()
        test_polynomial()
        
        print("Все тесты успешно выполнены!")
        
    except Exception as e:
        print(f"Ошибка в тестах: {e}")
        import traceback
        traceback.print_exc()
