def f(num):
    num = ['1','2','3','4','5']
Enter = input("Введите число")
if Enter in f:
    print("Вы угадали число!")
else:
    print("Вы не угадали число :(((")

def f2(x):
    num =['1','2','2','3','4']
for x in f2:
    if f2.count(x)>1:
        print(x)
def f3(week):
    week =("Понедельник","Вторник","Среда","Четверг","Пятница","Субота","Воскресенье")
    f3 = int(input("Сколько выходных в неделю вы хотите?"))
        weekend = week[7-f3:7]
        workday = week[0:7-x]
        return("Выходные дни:", weekend)
        return("Рабочие дни:", workday)
