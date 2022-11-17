# Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num и возвращает первое простое число большее числа num.

# Примечание 1. Используйте функцию is_prime() из предыдущей задачи.


def is_prime(num):
    counter = 0

    for i in range(1, num + 1):
        if num % i == 0:
            counter += 1

    if counter > 2 or counter < 2:
        return False
    elif counter == 2:
        return True

def get_next_prime(num):
    for i in range(num + 1, num + 1001):
        while is_prime(i):
            return i   # после return функция (а вместе с ней и цикл) заканциваются!!!

n = int(input())

print(get_next_prime(n))