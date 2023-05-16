# Задача № 26:
# Напишите программу, 
# которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# Проверка:
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8 

# Решение: 
a = int(input("Введите число: "))
b = int(input("Введите степень: "))

def exponentiation_recursive(a,b):
    if b == 0:
        return 1
    else:
        return a * exponentiation_recursive(a, b-1) 

print(exponentiation_recursive(a,b)) 