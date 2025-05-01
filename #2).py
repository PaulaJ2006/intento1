#Ejercicio 2)
number = int(input("Enter the number: "))
i = 1
while i <= number:
    resto = number % i
    if resto == 0:
        print(f"Divisores del {number}: ", i)
    i += 1