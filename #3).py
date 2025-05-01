#Ejercicio 3)
contador_1 = 1
while contador_1 <= 9:
	print("Tabla del " + str(contador_1))
	num_2 = 1
	while num_2 <= 10:
		print(str(contador_1) + "X" + str(num_2) + "=" + str(contador_1*num_2))
		num_2 += 1
	contador_1 += 1