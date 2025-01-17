# ---------------------------------------------------------------
# Обучение на Python курс "Поколение Python": курс для начинающих
# ---------------------------------------------------------------


# ---------------------------------------------------------------
# Обработка цифр числа
# ---------------------------------------------------------------

# При изучении целых чисел (тип данных int), мы говорили про операцию целочисленного деления // и операцию нахождения остатка от деления одного целого числа на другое %. Используя цикл while и две данных операции, можно обработать цифры числа с произвольным количеством разрядов (цифр).

# Пусть дано натуральное число n. Тогда:

# результатом операции n % 10 – является последняя цифра числа;
# результатом операции n // 10 – является число с удаленной последней цифрой.
# Напишем программу, которая считывает натуральное число (целое положительное) и обрабатывает его цифры.

n = int(input())
while n != 0:  # пока в числе есть цифры
    last_digit = n % 10  # получить последнюю цифру
    # код обработки последней цифры
    n = n // 10  # удалить последнюю цифру из числа

# Цикл while работает до тех пор, пока в числе есть необработанные цифры. Тело цикла содержит:

# 1. Процедуру получения последней цифры last_digit = n % 10;
# 2. Код обработки последней цифры;
# 3. Процедуру удаления последней цифры из числа n = n // 10.
# В качестве процедуры обработки может быть все что угодно: вывод цифр, нахождение суммы, произведения цифр, нахождение наибольшей или наименьшей цифры, подсчет цифр удовлетворяющих некоторому условию и т.д.

# Напишем программу, которая определяет, есть ли в числе цифра 7.

num = int(input())
has_seven = False  # сигнальная метка

while num != 0:
    last_digit = num % 10
    if last_digit == 7:
        has_seven = True
    num = num // 10

if has_seven == True:
    print('YES')
else:
    print('NO')

# Программа чтобы получить все цифры в столбик в обратном порядке с помощью цикла while 

num = int(input())

while num != 0:
    last_digit = num % 10
    num = num // 10
    print(last_digit)

# Программа для нахождения минимальную и максимальную цифру в большом числе 

num = int(input())
maxx = -1
minn = 10
while num != 0:
    last_digit = num % 10
    if last_digit > maxx:
        maxx = last_digit
    if last_digit < minn:
        minn = last_digit
    num = num // 10

print('Максимальная цифра равна', maxx)
print('Минимальная цифра равна', minn)

# Дано натуральное число. Напишите программу, которая вычисляет:

# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.

num = int(input())
summ = 0
count = 0
proizv = 1
first_digit = 0
last = num % 10 # Последнее число

while num != 0:
    last_digit = num % 10
    num = num // 10
    summ += last_digit #Сумма всех его цифр
    count += 1 # Количество ифр в нем
    proizv *= last_digit # Произведение
    first_digit = last_digit # Первое число

print(summ)
print(count) 
print(proizv)
print(summ / count) # Среднее арифметическое (это сумма всех чисел / на их кол-во)
print(first_digit)
print(first_digit + last) # сумма его первой и последней цифры