# functions with arguments

def clasificacion(name, gender):
    print(f"Hola, mi nombre es: {name}")
    if gender == 'male':
        #invocan la funcion
        print("confirmado, eres género {}".format(gender))
    elif gender == "female":
        print("confirmado, eres género {}".format(gender))
    elif gender == "no binario":
        print("confirmado, eres género {}".format(gender))
    else:
        print("confirmado, Tú género {} no está clasificado".format(gender))

# funcion auxiliar
def age_name(age):
    if age >= 18:
        #invocan la funcion
        print("confirmado, eres mayor de edad")
    else:
        print("confirmado, eres menor de edad ")


if  __name__ == '__main__':
    name = (input("Enter your name: ")).upper() # convetir el texto a mayúscula
    gender = (input("Enter your gender (male, female, no binario): ")).lower() # convetir el texto a minúscula
    age = int(input("Enter your age: "))    
    clasificacion(name, gender)
    age_name(age)

# execise in house:
#Dado el ejericio anterior, definir si el usuario es mayor o menor de edad 