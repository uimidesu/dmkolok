"""
Модуль для работы с многочленами с рациональными коэффициентами
Многочлен представлен как список коэффициентов от младших степеней к старшим
Например: 2x^2 + 3x + 1 = [1, 3, 2] (коэффициенты при x^0, x^1, x^2)
"""

from rational import *


class Polynomial:
    """Класс для представления многочлена"""

    def __init__(self, coefficients):
        """
        Инициализация многочлена
        coefficients - список коэффициентов (Rational или числа) от младших к старшим степеням
        ИЛИ строка в формате "2x^2 + 3x + 1"
        """
        if isinstance(coefficients, str):
            self.coefficients = self._parse_polynomial(coefficients)
        else:
            if not coefficients:
                self.coefficients = [Rational(Integer(0), Natural([1]))]
            else:
                self.coefficients = []
                for coef in coefficients:
                    if isinstance(coef, Rational):
                        self.coefficients.append(coef.copy())
                    elif isinstance(coef, (int, str)):
                        self.coefficients.append(Rational(coef))
                    elif isinstance(coef, Integer):
                        self.coefficients.append(TRANS_Z_Q(coef))
                    else:
                        raise ValueError("Некорректный тип коэффициента")

        self._normalize()

    def _parse_polynomial(self, poly_str):
        """Парсинг строкового представления многочлена"""
        # Упрощаем строку: удаляем пробелы
        poly_str = poly_str.replace(' ', '')

        if poly_str == '0':
            return [Rational(0)]

        # Если строка не содержит 'x', это константа
        if 'x' not in poly_str:
            try:
                return [Rational(poly_str)]
            except:
                raise ValueError(f"Некорректный формат константы: {poly_str}")

        # Находим максимальную степень
        max_degree = self._find_max_degree(poly_str)

        # Инициализируем коэффициенты нулями
        coefficients = [Rational(0) for _ in range(max_degree + 1)]

        # Разбиваем на мономы по знакам + и -
        terms = []
        current_term = ""

        for i, char in enumerate(poly_str):
            if char in '+-' and i > 0:
                terms.append(current_term)
                current_term = char
            else:
                current_term += char

        if current_term:
            terms.append(current_term)

        # Обрабатываем каждый моном
        for term in terms:
            if not term:
                continue

            coef, degree = self._parse_term(term)
            coefficients[degree] = ADD_QQ_Q(coefficients[degree], coef)

        return coefficients

    def _find_max_degree(self, poly_str):
        """Находит максимальную степень в многочлене"""
        max_degree = 0

        # Ищем все вхождения x с показателями степени
        i = 0
        while i < len(poly_str):
            if poly_str[i] == 'x':
                # Определяем степень
                if i + 1 < len(poly_str) and poly_str[i + 1] == '^':
                    # Формат x^n
                    j = i + 2
                    while j < len(poly_str) and poly_str[j].isdigit():
                        j += 1
                    degree = int(poly_str[i + 2:j])
                    max_degree = max(max_degree, degree)
                    i = j
                else:
                    # Просто x (степень 1)
                    max_degree = max(max_degree, 1)
                    i += 1
            else:
                i += 1

        return max_degree

    def _parse_term(self, term):
        """Парсит отдельный моном"""
        # Определяем знак
        sign = 1
        if term[0] == '+':
            term = term[1:]
        elif term[0] == '-':
            sign = -1
            term = term[1:]

        if not term:
            return Rational(0), 0

        # Если терм не содержит x, это константа
        if 'x' not in term:
            try:
                coef = Rational(term)
                return MUL_QQ_Q(coef, Rational(sign)), 0
            except:
                raise ValueError(f"Некорректный коэффициент: {term}")

        # Разделяем коэффициент и x часть
        x_index = term.find('x')
        coef_part = term[:x_index]
        x_part = term[x_index:]

        # Обрабатываем коэффициент
        if not coef_part:
            coef = Rational(1)
        elif coef_part == '-':
            coef = Rational(-1)
        elif coef_part == '+':
            coef = Rational(1)
        else:
            try:
                coef = Rational(coef_part)
            except:
                raise ValueError(f"Некорректный коэффициент: {coef_part}")

        coef = MUL_QQ_Q(coef, Rational(sign))

        # Обрабатываем степень
        if x_part == 'x':
            degree = 1
        elif x_part.startswith('x^'):
            try:
                degree = int(x_part[2:])
            except:
                raise ValueError(f"Некорректная степень: {x_part}")
        else:
            raise ValueError(f"Некорректный формат монома: {term}")

        return coef, degree

    def _normalize(self):
        """Удаление ведущих нулевых коэффициентов"""
        while len(self.coefficients) > 1:
            last_coef = self.coefficients[-1]
            if POZ_Z_D(last_coef.numerator) == 0:
                self.coefficients.pop()
            else:
                break

    def __str__(self):
        """Строковое представление многочлена"""
        if not self.coefficients:
            return "0"

        terms = []
        for i in range(len(self.coefficients) - 1, -1, -1):
            coef = self.coefficients[i]

            if POZ_Z_D(coef.numerator) == 0:
                continue

            coef_str = str(coef)

            if i == 0:
                terms.append(coef_str)
            elif i == 1:
                if coef_str == "1":
                    terms.append("x")
                elif coef_str == "-1":
                    terms.append("-x")
                else:
                    terms.append(f"{coef_str}x")
            else:
                if coef_str == "1":
                    terms.append(f"x^{i}")
                elif coef_str == "-1":
                    terms.append(f"-x^{i}")
                else:
                    terms.append(f"{coef_str}x^{i}")

        if not terms:
            return "0"

        result = terms[0]
        for term in terms[1:]:
            if term.startswith("-"):
                result += " - " + term[1:]
            else:
                result += " + " + term

        return result

    def __repr__(self):
        return f"Polynomial({str(self)})"

    def copy(self):
        """Создание копии многочлена"""
        return Polynomial([c.copy() for c in self.coefficients])


# P-1: Сложение многочленов
def ADD_PP_P(a: Polynomial, b: Polynomial) -> Polynomial:
    """Сложение многочленов"""
    max_len = max(len(a.coefficients), len(b.coefficients))
    result_coefficients = []
    
    for i in range(max_len):
        coef_a = a.coefficients[i] if i < len(a.coefficients) else Rational(0)
        coef_b = b.coefficients[i] if i < len(b.coefficients) else Rational(0)
        
        result_coefficients.append(ADD_QQ_Q(coef_a, coef_b))
    
    return Polynomial(result_coefficients)


# P-2: Вычитание многочленов
def SUB_PP_P(a: Polynomial, b: Polynomial) -> Polynomial:
    """Вычитание многочленов"""
    max_len = max(len(a.coefficients), len(b.coefficients))
    result_coefficients = []
    
    for i in range(max_len):
        coef_a = a.coefficients[i] if i < len(a.coefficients) else Rational(0)
        coef_b = b.coefficients[i] if i < len(b.coefficients) else Rational(0)
        
        result_coefficients.append(SUB_QQ_Q(coef_a, coef_b))
    
    return Polynomial(result_coefficients)


# P-3: Умножение многочлена на рациональное число
def MUL_PQ_P(p: Polynomial, q: Rational) -> Polynomial:
    """Умножение многочлена на рациональное число"""
    result_coefficients = []
    
    for coef in p.coefficients:
        result_coefficients.append(MUL_QQ_Q(coef, q))
    
    return Polynomial(result_coefficients)


# P-4: Умножение многочлена на x^k
def MUL_Pxk_P(p: Polynomial, k: int) -> Polynomial:
    """Умножение многочлена на x^k"""

    if k < 0:
        raise ValueError("k должно быть неотрицательным")

    if k == 0:
        return p.copy()

    result_coefficients = [Rational(0) for _ in range(k)] + [c.copy() for c in p.coefficients]
    return Polynomial(result_coefficients)


# P-5: Старший коэффициент многочлена
def LED_P_Q(p: Polynomial) -> Rational:
    """Старший коэффициент многочлена"""
    return p.coefficients[-1].copy()


# P-6: Степень многочлена
def DEG_P_N(p: Polynomial) -> int:
    """Степень многочлена"""
    return len(p.coefficients) - 1


# P-7: Вынесение из многочлена НОК знаменателей и НОД числителей
def FAC_P_Q(p: Polynomial) -> Rational:
    """Вынесение из многочлена НОК знаменателей коэффициентов и НОД числителей"""
    if not p.coefficients:
        return Rational(1)
    
    denominators = [c.denominator for c in p.coefficients]
    numerators = [ABS_Z_N(c.numerator) for c in p.coefficients if NZER_N_B(ABS_Z_N(c.numerator))]
    
    if not numerators:
        return Rational(1)
    
    lcm_denom = denominators[0].copy()
    for denom in denominators[1:]:
        lcm_denom = LCM_NN_N(lcm_denom, denom)
    
    gcd_num = numerators[0].copy()
    for num in numerators[1:]:
        gcd_num = GCF_NN_N(gcd_num, num)
    
    return Rational(TRANS_N_Z(gcd_num), lcm_denom)


# P-8: Умножение многочленов
def MUL_PP_P(a: Polynomial, b: Polynomial) -> Polynomial:
    """Умножение многочленов"""
    result_degree = DEG_P_N(a) + DEG_P_N(b)
    result_coefficients = [Rational(0) for _ in range(result_degree + 1)]
    
    for i, coef_a in enumerate(a.coefficients):
        for j, coef_b in enumerate(b.coefficients):
            product = MUL_QQ_Q(coef_a, coef_b)
            result_coefficients[i + j] = ADD_QQ_Q(result_coefficients[i + j], product)
    
    return Polynomial(result_coefficients)


# P-9: Частное от деления многочлена на многочлен
def DIV_PP_P(a: Polynomial, b: Polynomial) -> Polynomial:
    """Частное от деления многочлена на многочлен при делении с остатком"""
    if POZ_Z_D(LED_P_Q(b).numerator) == 0:
        raise ValueError("Деление на нулевой многочлен")
    
    deg_a = DEG_P_N(a)
    deg_b = DEG_P_N(b)
    
    if deg_a < deg_b:
        return Polynomial([Rational(0)])
    
    remainder = a.copy()
    quotient_coefficients = [Rational(0) for _ in range(deg_a - deg_b + 1)]
    
    for i in range(deg_a - deg_b, -1, -1):
        if DEG_P_N(remainder) < deg_b:
            break
        
        lead_rem = LED_P_Q(remainder)
        lead_div = LED_P_Q(b)
        
        coef = DIV_QQ_Q(lead_rem, lead_div)
        quotient_coefficients[i] = coef
        
        term = MUL_PQ_P(b, coef)
        term = MUL_Pxk_P(term, i)
        
        remainder = SUB_PP_P(remainder, term)
    
    return Polynomial(quotient_coefficients)


# P-10: Остаток от деления многочлена на многочлен
def MOD_PP_P(a: Polynomial, b: Polynomial) -> Polynomial:
    """Остаток от деления многочлена на многочлен при делении с остатком"""
    quotient = DIV_PP_P(a, b)
    product = MUL_PP_P(quotient, b)
    remainder = SUB_PP_P(a, product)
    
    return remainder


# P-11: НОД многочленов
def GCF_PP_P(a: Polynomial, b: Polynomial) -> Polynomial:
    """НОД многочленов (алгоритм Евклида)"""
    a_copy = a.copy()
    b_copy = b.copy()
    
    while DEG_P_N(b_copy) > 0 or POZ_Z_D(LED_P_Q(b_copy).numerator) != 0:
        temp = MOD_PP_P(a_copy, b_copy)
        a_copy = b_copy
        b_copy = temp
    
    return a_copy


# P-12: Производная многочлена
def DER_P_P(p: Polynomial) -> Polynomial:
    """Производная многочлена"""
    if DEG_P_N(p) == 0:
        return Polynomial([Rational(0)])
    
    result_coefficients = []
    
    for i in range(1, len(p.coefficients)):
        coef = p.coefficients[i]
        new_coef = MUL_QQ_Q(coef, Rational(i))
        result_coefficients.append(new_coef)
    
    return Polynomial(result_coefficients)


# P-13: Преобразование многочлена — кратные корни в простые
def NMR_P_P(p: Polynomial) -> Polynomial:
    """Преобразование многочлена — кратные корни в простые"""
    derivative = DER_P_P(p)
    gcd = GCF_PP_P(p, derivative)
    result = DIV_PP_P(p, gcd)

    return result


