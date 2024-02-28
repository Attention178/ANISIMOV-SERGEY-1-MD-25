import random
p=0
c=0
while True:
    x = random.randint(1,11)
    y = random.randint(1,11)
    res = int(input(f"{x}+{y}="))
    if res == x+y:
            p+=1
            print("Правильно")
    else:
        c+=1
        print("Ответ не верный")
        if c == 3:
            print("Игра окончена . Кол-во правилных ответ = ", p)
            break