print ("Екатеринбург - код 343\nОмск - код 381\nВоронеж  - код 473\nЯрославль - код 485")
code = int (input ("Ведите код города:"))
min = float (input("Введите количество минут:"))
if code:
	if code == 343:
		print (15*min)
	elif code == 381:
		print (18*min)
	elif code == 473:
		print (13*min)
	elif code == 485:
		print (11*min)
	else:
		print ("Код города введен неверно!")
else:
	print ("Пустая строка, введите число1")
	