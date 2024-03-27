def a():
    x = [0,1,2,3,4]
    num = int(input("Введите число: "))
    if num in x:
        return ("Поздравляю, вы угадали число!")
    else:
        return ("Нет такого числа!")
print(a())