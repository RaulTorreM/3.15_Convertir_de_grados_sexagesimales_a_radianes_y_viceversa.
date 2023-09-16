import math

def Convertir_A_Radianes(numIngresado):
    print("""El Ángulo en Grados se Convertirá en Radianes ...""")
    numIngresado = numIngresado * (180.00/(2 * math.pi))
    return print(f"""El Ángulo en Radianes Es: {numIngresado}""")
def Convertir_A_Grados(numIngresado):
    print("""El Ángulo en Radianes se Convertirá en Grados...""")
    numIngresado = numIngresado * ((2 * math.pi) / 180.00)
    print(f"""El Ángulo en Grados Es: {numIngresado}""")