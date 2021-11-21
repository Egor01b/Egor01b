def sum_of_args(*args):  # (*) - дает переменное количество аргументов
    sum = 0

    for i in args:
        sum += i
    return sum


print(sum_of_args(64, 128, 256, 512, 1000))
