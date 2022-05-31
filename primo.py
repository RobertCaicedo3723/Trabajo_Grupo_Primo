from xml.etree.ElementTree import XMLID


print("-------------------------------------------------")
print("-------------Calcular un numero primo------------")
print("-------------------------------------------------")

#Input

X = int(input("Ingrese un numero: "))

# Procesing

Y = int(2)
Z = "ROBERT"

while ((Z == "ROBERT") and (Y < X)):
    if((X % Y) == 0):
        Z = "CAICEDO"
    else:
        Y = Y + 1

#Output

if(Z == "ROBERT"):
    print("El número ingresado es primo")
else:
    print("El número ingresado NO es primo")
