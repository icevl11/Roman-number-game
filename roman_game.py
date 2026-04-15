import roman
from random import randint
from time import sleep
def guess_from_roman(random_number):
    try:
        user_number=int(input(f"Введи это римское число {roman.toRoman(random_number)} цифрами:"))
        if user_number<1:
            print("Ты не угадал поскольку римское число не может быть меньше 1")
        elif user_number>3999:
            print("Ты не угадал поскольку стандартное римское число не может быть больше 3999")
        elif user_number==random_number:
            print(f"Да ты угадал верно число действительно было {random_number}")
        else:
            print(f"Нет ты неверно угадал число было {random_number}")
    except ValueError:
        print("Ошибка требуется ввести целое число")
def guess_to_roman(random_number):
    try:
        user_roman=input(f"Введи это число {random_number} римскими цифрами:")
        checking=roman.fromRoman(user_roman)
        if checking==random_number:
            print(f"Да ты угадал верно римское число действительно было {roman.toRoman(random_number)}")
        else:
            print(f"Нет ты неверно угадал римское число было {roman.toRoman(random_number)}")
    except roman.InvalidRomanNumeralError:
        print("У тебя неправильный синтаксис римского числа")
print("Привет! В этой игре ты будешь переводить римские числа в обычные и наоборот.")
while True:
    sleep(1)
    print("Выбирай:")
    print("1.Перевод из римской системы в число")
    print("2.Перевод числа в римские цифры")
    print("3.Выйти")
    user_choise=input()
    if user_choise=="1":
        random_number=randint(1,3999)
        guess_from_roman(random_number)
    elif user_choise=="2":
        random_number=randint(1,3999)
        guess_to_roman(random_number)
    elif user_choise=="3":
        break
    else:
        print("Пожалуйста введи цифру одного из трех вариантов")