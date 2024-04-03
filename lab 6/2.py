dic = {"АВЕИНОРСТ":1, "ДКЛМПУ":2, "БГЁЬЯ":3, "ЙЫ":4, "ЖЗХЦЧ":5, "ШЭЮ":8, "ФЩЪ":10}
x = input("Введите слово: ")
res = 0
for i in x:
    for name, val in dic.items():
        if name.count(i) > 0:
            res += val
print(res)
