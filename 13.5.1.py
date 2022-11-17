# Напишите функцию is_prime(num), которая принимает в качестве аргумента натуральное число и возвращает значение 
# True если число является простым и False в противном случае.


def is_prime(num):
    counter = 0

    for i in range(1, num + 1):
        if num % i == 0:
            counter += 1

    if counter > 2 or counter < 2:
        return False
    elif counter == 2:
        return True

# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))