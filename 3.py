x = input("Введите слово, чтобы првоерить его на редкость ")
b = 0
for a in x:
    if a == "ф":
        b = 1
        break
if b ==1:
    print("ВАУУУ, ТАКОЕ РЕДКОЕ СЛОВО")
else:
    print("ХавАХА ЭТО НЕ РЕДКОЕ СЛОВО")