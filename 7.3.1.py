# На вход программе подается натуральное число nnn, а затем nnn различных натуральных чисел, каждое на отдельной строке. 
# Напишите программу, которая выводит наибольшее и второе наибольшее число последовательности.

# Формат входных данных
# На вход программе подаются натуральное число n≥2n \ge 2n≥2, а затем nnn различных натуральных чисел, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести два наибольших числа, каждое на отдельной строке.


n = int(input())

the_big_num = 0
second_big_num = 0

for i in range(n):
    a = int(input())
    if a > the_big_num:
        second_big_num = the_big_num
        the_big_num = a
    elif a < the_big_num and a > second_big_num:
        second_big_num = a

print(the_big_num)
print(second_big_num)