# coding=windows-1251
from random import randint


def attack(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        return (f'{char_name} ����� ���������� ����, ������ '
                f'{5 + randint(3, 5)}')
    if char_class == 'mage':
        return (f'{char_name} ����� ���������� ����, ������ '
                f'{5 + randint(5, 10)}')
    if char_class == 'healer':
        return (f'{char_name} ����� ���������� ����, ������ '
                f'{5 + randint(-3, -1)}')
    return ''


def defence(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        return (f'{char_name} ���������� {10 + randint(5, 10)} ��. �����')
    if char_class == 'mage':
        return (f'{char_name} ���������� {10 + randint(-2, 2)} ��. �����')
    if char_class == 'healer':
        return (f'{char_name} ���������� {10 + randint(2, 5)} ��. �����')
    return ''


def special(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        return (f'{char_name} �������� ����������� ������ '
                f'������������� {80 + 25}�')
    if char_class == 'mage':
        return (f'{char_name} �������� ����������� ������ ������ {5 + 40}�')
    if char_class == 'healer':
        return (f'{char_name} �������� ����������� ������ ������� {10 + 30}�')
    return ''


def start_training(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        print(f'{char_name}, �� ������� � ������� ������ �������� ���.')
    if char_class == 'mage':
        print(f'{char_name}, �� ��� � ������������ ���������� ������.')
    if char_class == 'healer':
        print(f'{char_name}, �� ������ � �������, ��������� �������� ����.')
    print('������������ ��������� ������ ��������.')
    print('����� ���� �� ������: attack � ����� ��������� ����������, '
          'defence � ����� ����������� ����� ���������� ��� '
          'special � ����� ������������ ���� ���������.')
    print('���� �� ������ �������������, ����� ������� skip.')
    cmd = None
    while cmd != 'skip':
        cmd: str = input('����� �������: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return '���������� ��������.'


def choice_char_class() -> str:
    approve_choice: str = ''
    char_class: str = ''
    while approve_choice != 'y':
        char_class: str = input('����� �������� ���������, '
                                '�� �������� ������ ������: ������� � warrior,'
                                '��� � mage, ������ � healer: ')
        if char_class == 'warrior':
            print('������� � ������� ���� �������� ���. '
                  '�������, ���������� � ��������.')
        if char_class == 'mage':
            print('��� � ���������� ���� �������� ���. '
                  '�������� ������� �����������.')
        if char_class == 'healer':
            print('������ � �������������� �����������. '
                  '������� ���� �� �������, ���� � �����.')
        approve_choice: str = input('����� (Y), ����� ����������� �����, '
                                    '��� ����� ������ ������, '
                                    '����� ������� ������� ��������� ').lower()
    return char_class


def main():
    print('����������� ����, �������� �����������!')
    print('������ ��� ������ ����...')
    char_name = input('...������ ����: ')
    print(f'����������, {char_name: str}! '
          '������ ���� ������������ � 80, ����� � 5 � ������ � 10.')
    print('�� ������ ������� ���� �� ��� ����� ����:')
    print('�������, ���, ������')
    char_class  = choice_char_class()
    print(start_training(char_name, char_class))


main()
