# Даны две различные клетки шахматной доски. Напишите программу, которая определяет, может ли слон попасть с первой клетки на вторую одним ходом. 
# Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. 
# Программа должна вывести «YES», если из первой клетки ходом слона можно попасть во вторую или «NO» в противном случае.

# Формат входных данных
# На вход программе подаётся четыре числа от 1 до 8.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

# Примечание. Шахматный слон ходит по диагоналям.

column_old, string_old, column_new, string_new = int(input()), int(input()), int(input()), int(input())
if (column_new - string_new == column_old - string_old) or (column_new + string_new == column_old + string_old):
    print('YES')
elif column_new == column_old or string_new == string_old:
    print('YES')
elif (column_new == column_old + 1 or column_new == column_old - 1 or column_new == column_old) and (string_new == string_old + 1 or string_new == string_old - 1 or string_new == string_old):
    print('YES')
else:
    print('NO')