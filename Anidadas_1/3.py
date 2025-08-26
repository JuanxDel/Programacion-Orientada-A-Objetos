e = int(input("Ingrese su edad: "))
i = int(input("Ingrese sus ingresos mensuales: "))
if e < 18 and i<5_000_000:
    print("No tiene que declarar renta.")
else:
    print("Tiene que declarar renta.")
