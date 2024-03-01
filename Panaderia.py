PanesDulces = {
    'Panettone': 25000,
    'Brioche': 9000,
    'Challah': 21000,
    'Concha': 1800,
    'Roscón': 4300,
    'Pan de muerto': 23000,
    'Pan de higo': 22300,
    'Pan de frutas': 35400,
    'Cinnamon roll': 15000,
    'Pan de naranja': 22800
    }

PanesSalados = {
    'Baguette': 13500,
    'Ciabatta': 14500,
    'Focaccia': 21800,
    'Pan de centeno': 32800,
    'Pan de ajo': 53200,
    'Pretzel': 32000,
    'Pan de cebolla': 34000,
    'Pan de queso': 22500,
    'Pan de aceitunas': 13800,
    'Pan de maíz': 11500
}

Postres = {
    'Tiramisú': 62000,
    'Cheesecake': 43500,
    'Crème brûlée': 74000,
    'Profiteroles': 18500,
    'Mousse de chocolate': 52000,
    'Flan': 53800,
    'Tarta de frutas': 61500,
    'Pastel de zanahoria': 17500,
    'Brownie': 33200,
    'Macarons': 16800
}

print("""Tipos de Panes disponibles: 
      1. PanesDulces 
      2. PanesSalados 
      3. Postres""")
TipoDePan = int(input("Seleccione el tipo de pan: "))

if TipoDePan == 1:
    TipoDePan = "PanesDulces"
elif TipoDePan == 2:
    TipoDePan = "PanesSalados"
else:
    TipoDePan = "Postres"

if TipoDePan in ["PanesDulces", "PanesSalados", "Postres"]:
    print(f"Productos de la categoría {TipoDePan}:")
    if TipoDePan == "PanesDulces":
        productos = PanesDulces
    elif TipoDePan == "Postres":
        productos = PanesSalados
    else:
        productos = Postres

    for i, (val, dinero) in enumerate(productos.items()):
        print(f"{i + 1}. {val} = ${dinero}")

    productoElegido = int(input("Seleccione un producto: "))

    if productoElegido in [1, 10, 0, 3]:
        productoElegido = list(productos.keys())[productoElegido - 1]
        promocion = input(f"El producto {productoElegido} tiene promoción de 2x1, ¿Desea aprovecharla? Contesta con un SI o NO: ").lower()


        if promocion =="si":
            precioInicial = productos[productoElegido]
            print(f"Producto elegido: 2 x {productoElegido}")
            print(f"Precio final: ${precioInicial}")
            dinero = int(input("Ingrese la cantidad de dinero que va a pagar: $"))

            if dinero <precioInicial:
                print("Lo sentimos, no tienes suficiente dinero")
            else:
                print(f"Su cambio es de ${dinero - precioInicial}")
        else:
            precioInicial = productos[productoElegido]
            print(f"Producto elegido: {productoElegido}")
            print(f"Precio original: ${precioInicial}")
            dinero = int(input("Ingrese la cantidad de dinero que va a pagar: $"))

            if dinero < precioInicial:
                print("Lo sentimos, no tienes suficiente dinero")
            else:
                print(f"Su cambio es de ${dinero - precioInicial}")
    else:
        if 1 <= productoElegido <= len(productos):
            productoElegido = list(productos.keys())[productoElegido - 1]
            precioInicial = productos[productoElegido]
            print(f"Producto elegido: {productoElegido}")
            print(f"Precio original: ${precioInicial}")
            dinero = int(input("Ingrese la cantidad de dinero que va a pagar: $"))

            if dinero < precioInicial:
                print("Lo sentimos, no tienes suficiente dinero")
            else:
                print(f"Su cambio es de ${dinero - precioInicial}")
        else:
            print("Selección no válida.")
else:
    print("Selección no válida.")