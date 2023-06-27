# coding=windows-1251
import math

message: str = ('Добро пожаловать в самую лучшую программу для вычисления '
                'квадратного корня из заданного числа')
print(message)


def calculate_square_root(number) -> float:
    """Вычисляет квадратный корень."""
    return math.sqrt(number)


def calc(your_number) -> None:
    """Проверяет число и выводит ответ."""
    if your_number <= 0:
        return your_number
    return print('Мы вычислили квадратный корень из введённого вами числа.'
                 f'Это будет: {calculate_square_root(your_number)}')


calc(float(25.5))
