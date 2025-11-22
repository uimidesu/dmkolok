"""
Система компьютерной алгебры - Desktop UI
Использует customtkinter
"""

import tkinter as tk
import customtkinter as ctk
from polynomial import *

class ModernAlgebraApp(ctk.CTk):
    """Главное окно приложения"""

    def __init__(self):
        super().__init__()

        # Настройка окна
        self.title("Система компьютерной алгебры")
        self.geometry("1400x900")

        # Установка темы
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Цветовая схема
        self.colors = {
            'primary': '#1f538d',
            'secondary': '#14375e',
            'accent': '#3b8ed0',
            'success': '#2cc985',
            'warning': '#f7b928',
            'error': '#e74856',
            'bg_dark': '#1a1a1a',
            'bg_medium': '#2b2b2b',
            'bg_light': '#3b3b3b',
            'text_primary': '#ffffff',
            'text_secondary': '#b0b0b0'
        }

        self.create_layout()

    def create_layout(self):
        """Создание главного интерфейса"""

        # Главный контейнер
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Боковая панель навигации
        self.create_sidebar()

        # Основная область контента
        self.main_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=30, pady=30)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)

        # Показываем справку по умолчанию
        self.show_help()

    def create_sidebar(self):
        """Создание боковой панели навигации"""
        sidebar = ctk.CTkFrame(self, width=300, corner_radius=0)
        sidebar.grid(row=0, column=0, sticky="nsew")
        sidebar.grid_rowconfigure(7, weight=1)

        # Логотип/Заголовок
        logo_frame = ctk.CTkFrame(sidebar, fg_color="transparent")
        logo_frame.grid(row=0, column=0, padx=30, pady=(40, 30))

        title_label = ctk.CTkLabel(
            logo_frame,
            text="АЛГЕБРА",
            font=ctk.CTkFont(size=32, weight="bold")
        )
        title_label.pack()

        subtitle_label = ctk.CTkLabel(
            logo_frame,
            text="Система компьютерной алгебры",
            font=ctk.CTkFont(size=13),
            text_color=self.colors['text_secondary']
        )
        subtitle_label.pack(pady=(5, 0))

        # Разделитель
        separator = ctk.CTkFrame(sidebar, height=2, fg_color=self.colors['bg_light'])
        separator.grid(row=1, column=0, sticky="ew", padx=30, pady=(0, 20))

        # Кнопки навигации
        nav_buttons = [
            ("Справка", self.show_help),
            ("Натуральные числа", self.show_natural),
            ("Целые числа", self.show_integer),
            ("Рациональные числа", self.show_rational),
            ("Многочлены", self.show_polynomial)
        ]

        self.nav_buttons = []
        for i, (text, command) in enumerate(nav_buttons):
            btn = ctk.CTkButton(
                sidebar,
                text=text,
                command=command,
                width=240,
                height=45,
                font=ctk.CTkFont(size=15),
                anchor="w",
                fg_color="transparent",
                hover_color=self.colors['bg_light'],
                corner_radius=8,
                border_width=0
            )
            btn.grid(row=i+2, column=0, padx=30, pady=3)
            self.nav_buttons.append(btn)

        # Нижняя секция
        bottom_frame = ctk.CTkFrame(sidebar, fg_color="transparent")
        bottom_frame.grid(row=8, column=0, padx=30, pady=30)

    def clear_main_frame(self):
        """Очистка основной области"""
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def highlight_nav_button(self, index):
        """Подсветка активной кнопки навигации"""
        for i, btn in enumerate(self.nav_buttons):
            if i == index:
                btn.configure(fg_color=self.colors['primary'])
            else:
                btn.configure(fg_color="transparent")

    def show_help(self):
        """Показать справку"""
        self.highlight_nav_button(0)
        self.clear_main_frame()

        # Заголовок
        header = ctk.CTkLabel(
            self.main_frame,
            text="Справочная система",
            font=ctk.CTkFont(size=36, weight="bold")
        )
        header.grid(row=0, column=0, sticky="w", pady=(0, 25))

        scroll_frame = ctk.CTkScrollableFrame(self.main_frame, fg_color="transparent")
        scroll_frame.grid(row=1, column=0, sticky="nsew")
        scroll_frame.grid_columnconfigure(0, weight=1)

        help_content = [
            ("Типы чисел", [
                ("Натуральные числа (N)", "Неотрицательные целые: 0, 1, 2, 3, ...\nПоддержка длинной арифметики"),
                ("Целые числа (Z)", "Положительные и отрицательные целые числа\nПример: -5, 0, 42"),
                ("Рациональные числа (Q)", "Дроби вида числитель/знаменатель\nПример: 3/4, -5/2, 7"),
                ("Многочлены (P)", "Многочлены с рациональными коэффициентами\nФормат: 1,2,3 = 3x² + 2x + 1")
            ]),
            ("Операции", [
                ("Натуральные числа", "Сравнение, сложение, вычитание, умножение, деление, НОД, НОК"),
                ("Целые числа", "Все арифметические операции с учетом знака, определение знака"),
                ("Рациональные числа", "Сложение, вычитание, умножение, деление дробей, сокращение"),
                ("Многочлены", "Все операции + производная, НОД многочленов")
            ])
        ]

        for section_title, items in help_content:
            section_frame = ctk.CTkFrame(scroll_frame, corner_radius=12, border_width=1)
            section_frame.grid(sticky="ew", pady=(0, 20))
            section_frame.grid_columnconfigure(0, weight=1)

            section_label = ctk.CTkLabel(
                section_frame,
                text=section_title,
                font=ctk.CTkFont(size=22, weight="bold"),
                anchor="w"
            )
            section_label.grid(row=0, column=0, sticky="w", padx=25, pady=(20, 15))

            for i, (title, desc) in enumerate(items):
                item_frame = ctk.CTkFrame(section_frame, fg_color="transparent")
                item_frame.grid(row=i+1, column=0, sticky="ew", padx=25, pady=(0, 15))

                title_label = ctk.CTkLabel(
                    item_frame,
                    text=title,
                    font=ctk.CTkFont(size=15, weight="bold"),
                    anchor="w"
                )
                title_label.pack(anchor="w")

                desc_label = ctk.CTkLabel(
                    item_frame,
                    text=desc,
                    font=ctk.CTkFont(size=13),
                    text_color=self.colors['text_secondary'],
                    anchor="w",
                    justify="left"
                )
                desc_label.pack(anchor="w", pady=(3, 0))

    def show_natural(self):
        """Показать интерфейс для натуральных чисел"""
        self.highlight_nav_button(1)
        self.clear_main_frame()

        self.create_calculation_interface(
            title="Натуральные числа",
            subtitle="N",
            default_val1="123",
            default_val2="45",
            operations=[
                ("Сравнение", "COM_NN_D"),
                ("Проверка на ноль", "NZER_N_B"),
                ("Добавить 1", "ADD_1N_N"),
                ("Сложение", "ADD_NN_N"),
                ("Вычитание", "SUB_NN_N"),
                ("Умножение", "MUL_NN_N"),
                ("Деление", "DIV_NN_N"),
                ("Остаток от деления", "MOD_NN_N"),
                ("НОД", "GCF_NN_N"),
                ("НОК", "LCM_NN_N")
            ],
            calculator=self.calculate_natural,
            num_type="natural"
        )

    def show_integer(self):
        """Показать интерфейс для целых чисел"""
        self.highlight_nav_button(2)
        self.clear_main_frame()

        self.create_calculation_interface(
            title="Целые числа",
            subtitle="Z",
            default_val1="15",
            default_val2="-7",
            operations=[
                ("Модуль", "ABS_Z_N"),
                ("Определение знака", "POZ_Z_D"),
                ("Умножить на -1", "MUL_ZM_Z"),
                ("Сложение", "ADD_ZZ_Z"),
                ("Вычитание", "SUB_ZZ_Z"),
                ("Умножение", "MUL_ZZ_Z"),
                ("Деление", "DIV_ZZ_Z"),
                ("Остаток от деления", "MOD_ZZ_Z")
            ],
            calculator=self.calculate_integer,
            num_type="integer"
        )

    def show_rational(self):
        """Показать интерфейс для рациональных чисел"""
        self.highlight_nav_button(3)
        self.clear_main_frame()

        self.create_calculation_interface(
            title="Рациональные числа",
            subtitle="Q",
            default_val1="3/4",
            default_val2="5/6",
            operations=[
                ("Сокращение дроби", "RED_Q_Q"),
                ("Проверка на целое", "INT_Q_B"),
                ("Сложение", "ADD_QQ_Q"),
                ("Вычитание", "SUB_QQ_Q"),
                ("Умножение", "MUL_QQ_Q"),
                ("Деление", "DIV_QQ_Q")
            ],
            calculator=self.calculate_rational,
            num_type="rational",
            input_hint="Формат: числитель/знаменатель (например: 3/4)"
        )

    def show_polynomial(self):
        """Показать интерфейс для многочленов"""
        self.highlight_nav_button(4)
        self.clear_main_frame()

        self.create_calculation_interface(
            title="Многочлены",
            subtitle="P",
            default_val1="1,2,3",
            default_val2="1,1",
            operations=[
                ("Сложение", "ADD_PP_P"),
                ("Вычитание", "SUB_PP_P"),
                ("Умножение многочлена на рац. число", "MUL_PQ_P"),
                ("Умножение многочлена на x^k, k-натуральное или 0", "MUL_Pxk_P"),
                ("Старший коэф. первого", "LED_P_Q"),
                ("Степень первого", "DEG_P_N"),
                ("Вынесение из многочлена НОК знаменателей коэффициентов и НОД числителей", "FAC_P_Q"),
                ("Умножение", "MUL_PP_P"),
                ("Деление", "DIV_PP_P"),
                ("Остаток от деления", "MOD_PP_P"),
                ("НОД многочленов", "GCF_PP_P"),
                ("Производная первого", "DER_P_P"),
                ("Преобразование многочлена — кратные корни в простые", "NMR_P_P")
            ],
            calculator=self.calculate_polynomial,
            num_type="polynomial",
            input_hint="Формат: '2x^3 + x - 5' или коэффициенты через запятую: '1,0,2'"
        )

    def create_calculation_interface(self, title, subtitle, default_val1, default_val2,
                                    operations, calculator, num_type, input_hint=""):
        """Создание универсального интерфейса для вычислений"""

        # Заголовок
        header_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        header_frame.grid(row=0, column=0, sticky="w", pady=(0, 25))

        header = ctk.CTkLabel(
            header_frame,
            text=title,
            font=ctk.CTkFont(size=36, weight="bold")
        )
        header.pack(side="left")

        subtitle_label = ctk.CTkLabel(
            header_frame,
            text=subtitle,
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color=self.colors['text_secondary']
        )
        subtitle_label.pack(side="left", padx=(15, 0))

        # Главный контейнер с сеткой 2 колонки
        content_frame = ctk.CTkFrame(self.main_frame, corner_radius=0, fg_color="transparent")
        content_frame.grid(row=1, column=0, sticky="nsew")
        content_frame.grid_columnconfigure(0, weight=1)
        content_frame.grid_columnconfigure(1, weight=1)
        content_frame.grid_rowconfigure(1, weight=1)

        # ЛЕВАЯ КОЛОНКА - Ввод данных и кнопка
        left_column = ctk.CTkFrame(content_frame, corner_radius=12, border_width=1)
        left_column.grid(row=0, column=0, rowspan=2, sticky="nsew", padx=(0, 15))
        left_column.grid_columnconfigure(0, weight=1)

        # Секция ввода
        input_section = ctk.CTkFrame(left_column, fg_color="transparent")
        input_section.grid(row=0, column=0, sticky="ew", padx=25, pady=(25, 20))
        input_section.grid_columnconfigure(0, weight=1)

        input_title = ctk.CTkLabel(
            input_section,
            text="Ввод данных",
            font=ctk.CTkFont(size=20, weight="bold"),
            anchor="w"
        )
        input_title.grid(row=0, column=0, sticky="w", pady=(0, 15))

        if input_hint:
            hint_label = ctk.CTkLabel(
                input_section,
                text=input_hint,
                font=ctk.CTkFont(size=12),
                text_color=self.colors['text_secondary'],
                anchor="w"
            )
            hint_label.grid(row=1, column=0, sticky="w", pady=(0, 20))

        # Поля ввода
        label1 = ctk.CTkLabel(
            input_section,
            text="Первое значение",
            font=ctk.CTkFont(size=14, weight="bold"),
            anchor="w"
        )
        label1.grid(row=2, column=0, sticky="w", pady=(0, 8))

        self.entry1 = ctk.CTkEntry(
            input_section,
            placeholder_text="Введите значение...",
            font=ctk.CTkFont(size=15),
            height=45,
            border_width=2
        )
        self.entry1.insert(0, default_val1)
        self.entry1.grid(row=3, column=0, sticky="ew", pady=(0, 20))

        label2 = ctk.CTkLabel(
            input_section,
            text="Второе значение",
            font=ctk.CTkFont(size=14, weight="bold"),
            anchor="w"
        )
        label2.grid(row=4, column=0, sticky="w", pady=(0, 8))

        self.entry2 = ctk.CTkEntry(
            input_section,
            placeholder_text="Введите значение...",
            font=ctk.CTkFont(size=15),
            height=45,
            border_width=2
        )
        self.entry2.insert(0, default_val2)
        self.entry2.grid(row=5, column=0, sticky="ew")

        # Кнопка вычисления
        calc_btn = ctk.CTkButton(
            left_column,
            text="ВЫЧИСЛИТЬ",
            command=lambda: calculator(num_type),
            height=55,
            font=ctk.CTkFont(size=16, weight="bold"),
            fg_color=self.colors['success'],
            hover_color=self.colors['accent'],
            corner_radius=10
        )
        calc_btn.grid(row=1, column=0, sticky="ew", padx=25, pady=25)

        # ПРАВАЯ ВЕРХНЯЯ - Операции
        operations_frame = ctk.CTkFrame(content_frame, corner_radius=12, border_width=1)
        operations_frame.grid(row=0, column=1, sticky="nsew", padx=(0, 0), pady=(0, 15))
        operations_frame.grid_columnconfigure(0, weight=1)

        op_title = ctk.CTkLabel(
            operations_frame,
            text="Выберите операцию",
            font=ctk.CTkFont(size=20, weight="bold"),
            anchor="w"
        )
        op_title.grid(row=0, column=0, sticky="w", padx=25, pady=(25, 15))

        # Радиокнопки для операций
        self.selected_operation = tk.StringVar(value=operations[3][1])

        radio_scroll = ctk.CTkScrollableFrame(
            operations_frame,
            fg_color="transparent",
            corner_radius=0
        )
        radio_scroll.grid(row=1, column=0, sticky="nsew", padx=25, pady=(0, 20))
        radio_scroll.grid_columnconfigure(0, weight=1)
        operations_frame.grid_rowconfigure(1, weight=1)

        for i, (op_name, op_code) in enumerate(operations):
            radio = ctk.CTkRadioButton(
                radio_scroll,
                text=op_name,
                variable=self.selected_operation,
                value=op_code,
                font=ctk.CTkFont(size=14),
                border_width_unchecked=2,
                border_width_checked=2
            )
            radio.grid(row=i, column=0, sticky="w", pady=6)

        # ПРАВАЯ НИЖНЯЯ - Результат
        result_frame = ctk.CTkFrame(content_frame, corner_radius=12, border_width=1)
        result_frame.grid(row=1, column=1, sticky="nsew")
        result_frame.grid_columnconfigure(0, weight=1)
        result_frame.grid_rowconfigure(1, weight=1)

        result_title = ctk.CTkLabel(
            result_frame,
            text="Результат вычисления",
            font=ctk.CTkFont(size=20, weight="bold"),
            anchor="w"
        )
        result_title.grid(row=0, column=0, sticky="w", padx=25, pady=(25, 15))

        self.result_text = ctk.CTkTextbox(
            result_frame,
            font=ctk.CTkFont(size=15),
            wrap="word",
            corner_radius=8,
            border_width=2
        )

        self.result_text.grid(row=1, column=0, sticky="nsew", padx=25, pady=(0, 25))
        self.result_text.configure(state="disabled")

    def calculate_natural(self, num_type):
        """Вычисление для натуральных чисел"""
        try:
            a = Natural(self.entry1.get())
            b = Natural(self.entry2.get())
            op = self.selected_operation.get()

            operations = {
                "COM_NN_D": lambda: {2: f"{a} > {b}", 0: f"{a} = {b}", 1: f"{a} < {b}"}[COM_NN_D(a, b)],
                "NZER_N_B": lambda: f"{a} " + ("не равно нулю" if NZER_N_B(a) else "равно нулю"),
                "ADD_1N_N": lambda: f"{a} + 1 = {ADD_1N_N(a)}",
                "ADD_NN_N": lambda: f"{a} + {b} = {ADD_NN_N(a, b)}",
                "SUB_NN_N": lambda: f"{a} - {b} = {SUB_NN_N(a, b)}",
                "MUL_NN_N": lambda: f"{a} × {b} = {MUL_NN_N(a, b)}",
                "DIV_NN_N": lambda: f"{a} ÷ {b} = {DIV_NN_N(a, b)}",
                "MOD_NN_N": lambda: f"{a} mod {b} = {MOD_NN_N(a, b)}",
                "GCF_NN_N": lambda: f"НОД({a}, {b}) = {GCF_NN_N(a, b)}",
                "LCM_NN_N": lambda: f"НОК({a}, {b}) = {LCM_NN_N(a, b)}"
            }

            result = operations[op]()
            self.show_result(result, success=True)

        except Exception as e:
            self.show_result(f"ОШИБКА: {str(e)}", success=False)

    def calculate_integer(self, num_type):
        """Вычисление для целых чисел"""
        try:
            a = Integer(self.entry1.get())
            b = Integer(self.entry2.get())
            op = self.selected_operation.get()

            operations = {
                "ABS_Z_N": lambda: f"|{a}| = {ABS_Z_N(a)}",
                "POZ_Z_D": lambda: f"Число {a} - " + {2: "положительное", 0: "ноль", 1: "отрицательное"}[POZ_Z_D(a)],
                "MUL_ZM_Z": lambda: f"{a} × (-1) = {MUL_ZM_Z(a)}",
                "ADD_ZZ_Z": lambda: f"{a} + ({b}) = {ADD_ZZ_Z(a, b)}",
                "SUB_ZZ_Z": lambda: f"{a} - ({b}) = {SUB_ZZ_Z(a, b)}",
                "MUL_ZZ_Z": lambda: f"{a} × ({b}) = {MUL_ZZ_Z(a, b)}",
                "DIV_ZZ_Z": lambda: f"{a} ÷ ({b}) = {DIV_ZZ_Z(a, b)}",
                "MOD_ZZ_Z": lambda: f"{a} mod ({b}) = {MOD_ZZ_Z(a, b)}"
            }

            result = operations[op]()
            self.show_result(result, success=True)

        except Exception as e:
            self.show_result(f"ОШИБКА: {str(e)}", success=False)

    def calculate_rational(self, num_type):
        """Вычисление для рациональных чисел"""
        try:
            a = Rational(self.entry1.get())
            b = Rational(self.entry2.get())
            op = self.selected_operation.get()

            operations = {
                "RED_Q_Q": lambda: f"Сокращение {a} = {RED_Q_Q(a)}",
                "INT_Q_B": lambda: f"{a} " + ("является целым числом" if INT_Q_B(a) else "не является целым числом"),
                "ADD_QQ_Q": lambda: f"{a} + {b} = {ADD_QQ_Q(a, b)}",
                "SUB_QQ_Q": lambda: f"{a} - {b} = {SUB_QQ_Q(a, b)}",
                "MUL_QQ_Q": lambda: f"{a} × {b} = {MUL_QQ_Q(a, b)}",
                "DIV_QQ_Q": lambda: f"{a} ÷ {b} = {DIV_QQ_Q(a, b)}"
            }

            result = operations[op]()
            self.show_result(result, success=True)

        except Exception as e:
            self.show_result(f"ОШИБКА: {str(e)}", success=False)

    def calculate_polynomial(self, num_type):
        """Вычисление для многочленов"""
        try:
            def parse_poly(s):
                # Пробуем распарсить как строковое представление
                # Если не получается, пробуем как список коэффициентов
                try:
                    return Polynomial(s)
                except:
                    # Старый формат: коэффициенты через запятую
                    coeffs = [c.strip() for c in s.split(',')]
                    return Polynomial([Rational(c) for c in coeffs])

            a = parse_poly(self.entry1.get())
            b = parse_poly(self.entry2.get())

            def parse_c(b):
                c = b.coefficients[0].numerator
                if POZ_Z_D(c) == 2:
                    c = c.abs_value.digits[-1]
                elif POZ_Z_D(c) == 1:
                    c = c.abs_value.digits[-1] * -1
                elif POZ_Z_D(c) == 0:
                    c = 0
                return c

            c = parse_c(b)
            op = self.selected_operation.get()

            operations = {
                "ADD_PP_P": lambda: f"P₁ = {a}\nP₂ = {b}\n\nP₁ + P₂ = {ADD_PP_P(a, b)}",
                "SUB_PP_P": lambda: f"P₁ = {a}\nP₂ = {b}\n\nP₁ - P₂ = {SUB_PP_P(a, b)}",
                "MUL_PQ_P": lambda: f"P₁ = {a}\nq = {b.coefficients[0]}\n\nP₁ × q = {MUL_PQ_P(a, b.coefficients[0])}",
                "MUL_Pxk_P": lambda: f"P₁ = {a}\nk = {c}\n\nP₁ × x^k = {MUL_Pxk_P(a, c)}",
                "FAC_P_Q": lambda: f"P₁ = {a}\n\nAnswer = {FAC_P_Q(a)}",
                "NMR_P_P": lambda: f"P₁ = {a}\n\nAnswer = {NMR_P_P(a)}",
                "MUL_PP_P": lambda: f"P₁ = {a}\nP₂ = {b}\n\nP₁ × P₂ = {MUL_PP_P(a, b)}",
                "DIV_PP_P": lambda: f"P₁ = {a}\nP₂ = {b}\n\nP₁ ÷ P₂ = {DIV_PP_P(a, b)}",
                "MOD_PP_P": lambda: f"P₁ = {a}\nP₂ = {b}\n\nP₁ mod P₂ = {MOD_PP_P(a, b)}",
                "DER_P_P": lambda: f"P₁ = {a}\n\nP₁' = {DER_P_P(a)}",
                "GCF_PP_P": lambda: f"P₁ = {a}\nP₂ = {b}\n\nНОД(P₁, P₂) = {GCF_PP_P(a, b)}",
                "DEG_P_N": lambda: f"P₁ = {a}\n\nСтепень P₁ = {DEG_P_N(a)}",
                "LED_P_Q": lambda: f"P₁ = {a}\n\nСтарший коэффициент P₁ = {LED_P_Q(a)}",
            }

            result = operations[op]()
            self.show_result(result, success=True)

        except Exception as e:
            self.show_result(f"ОШИБКА: {str(e)}", success=False)

    def show_result(self, message, success=True):
        """Отображение результата"""
        self.result_text.configure(state="normal")
        self.result_text.delete("1.0", "end")
        self.result_text.insert("1.0", message)
        self.result_text.configure(state="disabled")

        if success:
            self.result_text.configure(text_color=self.colors['success'])
        else:
            self.result_text.configure(text_color=self.colors['error'])


def main():
    """Запуск приложения"""
    app = ModernAlgebraApp()
    app.mainloop()


if __name__ == "__main__":
    main()
