import math
import random

# 1

num_1= int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))

print("сумма:", num_1 + num_2)
print("разность:", num_1 - num_2)
print("произведение:", num_1 * num_2)
print("частное:", num_1 / num_2)

# 2 

hours = int(input("Введите кол-во часов: "))
min = int(input("Введите кол-во минут: "))
sec = int(input("Введите кол-во секунд: "))

print("Время в секундах:", hours * 3600 + min * 60 + sec)

# 3

num_3 = int(input("Введите число: "))

if num_3 > 0:
    print("число положительное")
elif num_3 < 0:
    print("число отрицательное")
else:
    print("число равняется нулю")

# 4

year = int(input("Введите год: "))

if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print("Год является високосным")
else:
    print("Год не является високосным")

# 5 

d = int(input("Введите первое число: "))
e = int(input("Введите второе число: "))
f = int(input("Введите третье число: "))

if d > e and d > f:
    print("Наибольшее число:", d)
elif e > d and e > f:
    print("Наибольшее число:", e)
elif f > d and f > e:
    print("Наибольшее число:", f)
elif d == e and e == f:
    print("числа равны")
else:
    print(max(d, e, f))

# 7
# циклом for вывести четные числа от 2 до 20 включительно
print("Четные числа от 2 до 20:")
for number in range(2, 21, 2):
    print(number)

# (2, 21, 2) -> первое число - начало диапозона, второе число конец диапозона + 1, третье число - шаг цикла

# 8 

n = int(input("Введите число: ")) 
print(math.factorial(n))

# 9 

import random

g = random.randint(1, 100)      # генерация случайного числа от 1 до 100
user_num = None                 # изначально, число пользователя ничему не равно

while user_num != g:
    user_num = int(input("Введите число от 1 до 100: "))
        
    if user_num > g:
        print("Ваше число больше чем загаданное")
    elif user_num < g:
        print("Ваше число меньше чем загаданное")
    else:
        print("Вы угадали")
        break


# 10
# вывести первые 20 чмсел фибоначчи
# 1 1 2 3 5 8 13 и тд

fib = [1, 1]

for i in range(2, 20):
    next_num = fib[i-1] + fib[i-2]
    fib.append(next_num)

print(f"первые 20 чисел фибоначчи:\n {fib}")


# 11 

text = input("Введите стоку: ")
reversed_text = text[::-1]           # срез, переворачивает задом наперед
print(reversed_text)

# 12
txt = input("Введите сторку:")
glasnie = "аеёиоуыэюя"
counter = 0

for char in txt:
    if char.lower() in glasnie:
        counter += 1
    
print(counter)

# 14 

digit = []          #создаем пустой массив

for i in range(10):
    digit.append(random.randint(0, 50))             # рандом заполняет массив случайными числами от 1 до 50, append - добавить эл-ты в массив
print(digit)

print(sum(digit))
