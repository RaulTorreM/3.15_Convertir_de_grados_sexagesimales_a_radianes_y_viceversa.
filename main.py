
from Lib.Conversor import Convertir_A_Grados
from Lib.Conversor import Convertir_A_Radianes

if __name__ == '__main__':
    opcionIngresado = 0
    numIngresado = float(input("Ingrese un ángulo a calcular  : "))
    while opcionIngresado != 1 and opcionIngresado != 2:
        print("""El Ángulo ingresado está en grados o en radianes?
        1) Grados
        2) Radianes""")
        opcionIngresado = int(input("Ingrese una Opción: "))

    if opcionIngresado == 1:
        Convertir_A_Radianes(numIngresado)
    elif opcionIngresado == 2:
        Convertir_A_Grados(numIngresado)