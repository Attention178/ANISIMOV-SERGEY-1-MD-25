def is_happy(x):
    string_x = str(x)
    half1 = string_x[:len(string_x) // 2]
    half2 = string_x[len(string_x) // 2:]
    sum1 = 0
    sum2 = 0
    for enum in half1:
        sum1 += int(enum)
    for enum in half2:
        sum2 += int(enum)
    if sum1 == sum2:
        return True
    return False