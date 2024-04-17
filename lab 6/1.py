dic = {
    "Россия": "Москва",
"США": "Вашингтон",
"Франция": "Париж",
"Португалия": "Лиссабон"}
print(dic)
x = input("Введите название страны: ")
print("Столица ", x , " : ", dic[x])
sort_dic = dict(sorted(dic.items()))
print(sort_dic)