"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
class MyZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    n = int(input("У нас 50 литров сока. Сколько человек будет на банкете? "))
    if n == 0:
        raise MyZeroDivisionError("На ноль делить нельзя")
except MyZeroDivisionError as e:
    print(e)
else:
    print(f"Каждому достанется по {50 / n} литров сока")
