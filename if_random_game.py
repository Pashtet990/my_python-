import random

x = random.randint (1,4)
y = int (input ("Введите число:"))
if x == y:
	print ("Победа!")
elif y > x:
	print ("Результат меньше вашего значения")
elif y < x:
	print ("Результат больше вашего значения")
else:
	print ("Что-то пошло не так!")