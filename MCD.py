def MCD(a, b):
    # Paso 1
    r_prev, r = a, b
    s_prev, s = 1, 0
    t_prev, t = 0, 1

    while r != 0:
        # Paso 2
        cociente = r_prev // r
        r_prev, r = r, r_prev - cociente * r
        s_prev, s = s, s_prev - cociente * s
        t_prev, t = t, t_prev - cociente * t

    # Paso 5
    Formato = f"{a}X + {b}Y = {r_prev}"
    return Formato

# Ejemplo de uso
a = int(input("Ingresa el acompanante de la X: "))
b = int(input("Ingresa el acompanante de la Y: "))
c = int(input("Ingresa la variable independiente: "))


Formato = MCD(a, b)
if b == 0:
    print("La ecuacion no tiene solucion")
else:
    print(" ")
    print("El resultado de la ecuacion es: ",Formato)
  

