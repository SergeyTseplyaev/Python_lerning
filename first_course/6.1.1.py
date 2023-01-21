# Напишите программу, которая упорядочивает три числа от большего к меньшему.

# Формат входных данных
# На вход программе подается три целых числа, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести три числа, каждое на отдельной строке, упорядоченных от большего к меньшему.

a, b, c = int(input()), int(input()), int(input())
print(max(a, b, c))
print(a + b + c - min(a, b, c) - max(a, b, c))
print(min(a, b, c))

# мое решение:
# a, b, c = int(input()), int(input()), int(input())
# print(max(a, b, c))
# if a == b or a == c:
#     print(a)
# elif b == a or b == c:
#     print(b)
# elif c == a or c == b:
#     print(b)
# else:
#     if max(a, b, c) > a > min(a, b, c):
#         print(a)              
#     elif max(a, b, c) > b > min(a, b, c):
#         print(b)                        
#     elif max(a, b, c) > c > min(a, b, c):       
#         print(c)        
# print(min(a, b, c))
       
