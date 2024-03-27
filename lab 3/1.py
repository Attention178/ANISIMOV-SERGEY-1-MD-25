def my_del(x):
    try:
        res = 300/x
    except ValueError:
        print("Введите число")
    except ZeroDivisionError:
        print("На 0 делить нельзя")
    else:
        return res


x = int(input())
print(my_del(x))
