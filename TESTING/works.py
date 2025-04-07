
'''
 Напишите функцию add принимающую на вход два целых числа.
 Первый аргумент
     'возводится в степень второго аргумента, и возвращается результат. Если один
     'или оба аргумента НЕ являются целыми числами, то возвращается None.
'''
def add(a: int, b: int):
    a = a**b
    return a if type(a) != float and type(b) != float else None

'''
    Напишите функцию my_func, 
        которая при получении двух аргументов вернёт их сумму, 
        а при получении трёх аргументов вернёт их произведение.
'''
def my_func(*numb):
    if len(numb) == 3:
        return sum(numb)
    elif len(numb) == 2:
        total = 0
        for i in numb:
            total *= i
        return total


'''
'Напишите функцию bank, которая в качестве аргументов принимает 2 числа. '
 'Первое число - сумма вклада, второе число - количество лет. Верните сумму, '
 'которая будет на счете в конце срока вклада, при условии что ставка 8% '
 'годовых, и проценты начисляются раз в год.
'''
# РЕШЕНО
def bank(deposit, years):
    rate = 0.08  # Годовая процентная ставка (8%)
    final_amount = deposit * (1 + rate) ** years  # Формула расчёта
    return round(final_amount, 2)  # Округление до двух знаков после запятой

# Примеры использования:
print(bank(100000.500, 3))  # Вывод: 125971.83
print(bank(500000, 5))      # Вывод: 734664.04


'''
Напишите функцию maxlength в которую подаётся кортеж, состоящий из чисел и '
 'слов. Верните самое длинное слово.
'''
# РЕШЕНО
def maxlength(*args):
    lst = [i for i in args if isinstance(i, str)]
    return max(lst)

# print(maxlength('apple', 30000000000, 'orange', 'watermelon', 2))

'''
'Напишите функцию clean, которая в качестве аргумента принимает строку с '
 'буквами разного регистра. Очистите строку от букв нижнего регистра и верните '
 'результат.
'''
# РЕШЕНО
def clean(st: str):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    result = ''
    try:
        for i in st:
            if i not in alphabet:
                result += i
    except Exception as ex:
        return ex
    else:
        return result

#
# print(clean('CsaLeEipAmjRnIuNvG'))

'''
'Напишите функцию cycle, в которой с помощью цикла, верните результат '
 'сложения трёхзначных чисел, из которых состоит строка, с длиной кратной '
 'трём. Ответ должен быть в виде словаря, где ключ это входящая строка, и '
 'значение это результат сложения.'
'''
# РЕШЕНО
def cycle(numbers: str):
    st = ''
    total = 0
    try:
        for i in numbers:
            st += i
            if len(st) == 3:
                total += int(st)
                st = ''
        return {numbers: str(total)}
    except Exception as ex:
        return ex


'''
Напишите функцию enum в которую подаётся список фамилий. Верните список '
 'кортежей, в котором первым элементом будет цифра, начиная со ста.
'''
# РЕШЕНО
def enum(lst: list):
    total = 100
    result = []
    try:
        for i in lst:
            result.append((total, i))
            total += 1
        return result
    except Exception as ex:
        return ex

# print(enum(["Шишкин", "Захаров", "Васечкин", "Конев"]))

'''
'Допишите код, вставив вместо < *** > сортировку по второй букве в словах '
 'списка.
'''
# РЕШЕНО
def sorted_char(words):
    words = sorted(words, key=lambda x: x[1])
    return words

lst = ['фича', 'комп', 'джун', 'баг', 'тренд', 'код']
print(sorted_char(lst))