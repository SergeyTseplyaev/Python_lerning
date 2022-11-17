# Палиндром 🌶️

# Напишите функцию is_palindrome(text), которая принимает в качестве аргумента строку text и возвращает значение True если указанный текст является 
# палиндромом и False в противном случае.

# Примечание 1. Палиндром – это строка, которая читается одинаково в обоих направлениях

# Примечание 2. При проверке считайте большие и маленькие буквы одинаковыми, а также игнорируйте пробелы, а также символы , . ! ? -.


alfavit_rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alfavit_en = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# объявление функции
def is_palindrome(text):

    new_text = ''
    # заполняем новый список только буквами в нижнем регистре
    for i in range(len(text)):
        if text[i] in alfavit_en or text[i] in alfavit_rus:
            new_text += text[i].lower()
    # если инвертированная строка равна изначальной строке, то возвращаем True
    if new_text == new_text[::-1]:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))