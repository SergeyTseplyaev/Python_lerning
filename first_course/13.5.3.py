# Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое значение пароля password и возвращает значение True если пароль является надежным и False в противном случае.

# Пароль является надежным если:

#     его длина не менее 88 символов; 
#     он содержит как минимум одну заглавную букву (верхний регистр); 
#     он содержит как минимум одну строчную букву (нижний регистр);
#     он содержит хотя бы одну цифру.


def is_password_good(password):

    # переменные для подсчета кол-ва больших букв, маленьких букв и чисел
    counter_big = 0
    counter_little = 0
    counter_num = 0

    if len(password) < 8:   # сразу отбрасываем варианты строк длинной меньше 8-ми символов
        return False
    else:
        # в цикле перебираем все элементы строки и определяем, являются ли они большой буквой, маленькой буквой или числом
        # для ускорения работы программы, добавенно условие, что если в одной из меременных уже есть значение, то мы не тратим время на перезапись переменной
        for i in range(len(password)):
            if counter_big <= 1 and password[i] == password[i].upper() and password[i] not in '0123456789':
                counter_big += 1
            elif counter_little <= 1 and password[i] == password[i].lower() and password[i] not in '0123456789':
                counter_little += 1
            elif counter_num <= 1 and password[i] in '0123456789':
                counter_num += 1
        # если все условия пройдены, то возвращаем True
        if counter_num == 0 or counter_big == 0 or counter_little == 0:
            return False
        else:
            return True

txt = input()

print(is_password_good(txt))