#Reemplace el ejercicio 3 por una implementación con parámetros pasados por
#consola usando la librería sys.


import sys
#print ("El valor del sueldo:" , sys.srgv[0])
#utilizando sys puedo inocar programas en python y almacenarlo en una variable
#print ("El valor pasado es:", sys.argv[1])

def calcular_salario(sueldo, rango):
    if rango == 1:
        return sueldo * 0.83
    elif rango == 2:
        return sueldo * 1.2
    elif rango == 3:
        return sueldo * 5
    else:
        return "Rango no válido"

def main():
    sueldo = float(input(sys.argv[1]))
    rango = int(input(sys.argv[2]))

    salario_final = calcular_salario(sueldo, rango)

    if isinstance(salario_final, str):
        print(salario_final)
    else:
        print("El salario correspondiente al rango", rango, "es:", salario_final)

if __name__ == "__main__":
    main()
