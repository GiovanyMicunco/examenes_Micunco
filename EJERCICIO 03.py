def ingresar_variables():
    while True:
        try:
            a=float(input("Ingresar primer numero:  "))
            b=float(input("Ingresar segundo numero: "))
            return a, b
        except ValueError:
            print("Ups, tenemos un error. Ingresar un numero correcto.")
           
def division(a,b):
    while True:
        try:
            resultado= a/b
            return resultado
        except ZeroDivisionError:
            print("Ups, tenemos un error. No se puede dividir entre cero")
            b=float(input("Ingresa otro numero diferente a cero  :"))

def evaluar_suma(a,b):
    while True:
        try:
            if a+b<0:
                raise ValueError("Tienes un error: la suma de los numero es negativa")
            return a+b
        except ValueError as e:
            print(e)
            a,b=ingresar_variables()

def ingresar_lista():
    lista=[]
    while True:
        try:
            n=int(input("Ingresar cantidad de elementos :"))
            for i in range(n):
                elemento=float(input("Ingresar el elemento: ".format(i+1)))
                lista.append(elemento)
            indice=int(input("Ingresar indice que desea consultar:  "))
            print("El elemento en el indice es: ".format(indice, lista[indice]))
            break
        except(ValueError,IndexError):
            print("Ups, error: Ingresa un indice valido")

def main():
    print("1. División entre dos números")
    print("2. Evaluar la suma de dos números")
    print("3. Ingresar N elementos a una lista y consultar un índice")
    opcion = int(input("Seleccione una opción (1, 2 o 3): "))

    if opcion == 1:
        num1, num2 = ingresar_variables()
        resultado = division(num1, num2)
        print("El resultado de la división es:", resultado)
    elif opcion == 2:
        num1, num2 = ingresar_variables()
        resultado = evaluar_suma(num1, num2)
        print("El resultado de la suma es:", resultado)
    elif opcion == 3:
        ingresar_lista()
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()              
            