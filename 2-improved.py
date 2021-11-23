first_num = 2
second_num = 3

def sum_of_args(*args):  # (*) - дает переменное количество аргументов
    sum = 0

    for i in args:
        sum += i
    return sum

print(sum_of_args(first_num, second_num))
