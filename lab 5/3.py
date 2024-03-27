week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
x = int(input("Сколько выходных на неделе вы хотите? "))
hol = week[7-x:7]
rab = week[0:7-x]
print("Выходные дни:" , hol)
print("Рабочие дни:" ,rab)