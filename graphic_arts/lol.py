# coding=windows-1251
import math

message: str = ('����� ���������� � ����� ������ ��������� ��� ���������� '
                '����������� ����� �� ��������� �����')
print(message)


def calculate_square_root(number) -> float:
    """��������� ���������� ������."""
    return math.sqrt(number)


def calc(your_number) -> None:
    """��������� ����� � ������� �����."""
    if your_number <= 0:
        return your_number
    return print('�� ��������� ���������� ������ �� ��������� ���� �����.'
                 f'��� �����: {calculate_square_root(your_number)}')


calc(float(25.5))
