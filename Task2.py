#                       Задача 2
# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.

num = int(input("Введите число N: "))
num_list = []
for i in range(1, num + 1):
    if i == 1:
        num_list.append(i)
    else:
        temp = num_list[i - 2] * i
        num_list.append(temp)
print(num_list)