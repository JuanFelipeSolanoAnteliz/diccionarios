#definir las variables y establecer los diccionarios con los productos

menu = dict ({
    "Pan_Dulces": {
        "producto": list([
                {"nombre":'Pan de canela', "valor": 250},
            {"nombre":'Bollo de chocolate', "valor": 300},
            {"nombre":'Rosquillas glaseadas', "valor": 275},
            {"nombre":'Pan de plátano', "valor": 225},
            {"nombre":'Concha', "valor": 250},
            {"nombre":'Pandemuerto', "valor": 280},
            {"nombre":'Trenza de frutas', "valor": 325},
            {"nombre":'Pan de jengibre', "valor": 350},
            {"nombre":'Bollos de pasas', "valor": 290},
            {"nombre":'Donas de vainilla', "valor": 275}
        ]),
        "promociones": [
            {"codigo": 0, "nombre": "Descuento del 15%", "precio": 212},
            {"codigo": 1, "nombre": "3 por 2", "precio": 600}
            ]
      },
    
    "pan_salado":{
            "producto": list([
                {"nombre":'Baguette',"valor": 200},
            {"nombre":'Pretzel',"valor": 220},
            {"nombre":'Focaccia',"valor": 250},
            {"nombre":'Pan de ajo',"valor": 225},
            {"nombre":'Pan de centeno',"valor": 230},
            {"nombre":'Ciabatta',"valor": 240},
            {"nombre":'Bollos de perrito caliente',"valor": 250},
            {"nombre":'Pan de maíz',"valor": 210},
            {"nombre":'Pan de pita',"valor": 220},
            {"nombre":'Panecillos de queso',"valor": 275}
        ]),
            "promociones": [
            {"codigo": 0, "nombre": "Descuento del 15%", "precio": 170},
            {"codigo": 1, "nombre": "3 por 2", "precio": 440}
            ]
        },    
    "postres":{
            "producto": list([
            {"nombre":"Pastel de Chocolate", "valor": 2599},
            {"nombre":"Helado de Vainilla", "valor": 1250},
            {"nombre":"Tarta de Manzana", "valor": 1875},
            {"nombre":"Cupcakes de Fresa", "valor": 899},
            {"nombre":"Mousse de Limón", "valor": 1425},
            {"nombre":"Brownie de Nuez", "valor": 1050},
            {"nombre":"Gelatina de Frutas", "valor": 699},
            {"nombre":"Cheesecake de Frambuesa", "valor": 2200},
            {"nombre":"Profiteroles de Chocolate", "valor": 1680},
            {"nombre":"Arroz con Leche", "valor": 925}
   
        ]),
            "promociones": [
            {"codigo": 0, "nombre": "Descuento del 15%", "precio": 2209},
            {"codigo": 1, "nombre": "3 por 2", "precio": 2500}
            ]
    }
})

print("Selecciona la Categoría")
listaCategoria = menu.keys()
listaCategoria = list(listaCategoria)
for i,val in enumerate(listaCategoria):
    print(f"{i}. {val}")
opcionCategoria = int(input())
datosCategoria = menu.get(listaCategoria[opcionCategoria])
productosCategorias = datosCategoria["producto"]

print(f"seleccione un producto de la categoria {listaCategoria[opcionCategoria]}")
#despues de seleccionados los datos se muestra salida con la lista de productos
#que se pueden seleccionaren la categoria seleccionada por el cliente

for i, val in enumerate(productosCategorias):
    print(f"{i}. {val}")
#muestra la lista de los productos con su indice (i) y los valores (val) almacenados
#en el dicionario de la categpria correspondiente
 
opcionProducto = int(input())
#se muestra una entrad en la cual el usuario indica el producto que desea guiandose por 
#guiandose por el indice mostrado anteriormente
datosCategoria = menu.get(listaCategoria[opcionCategoria])
promocionesProducto = datosCategoria["promociones"]

promocionesProducto = list()
for val in promocionesProducto:
    if(val.get("indice") == opcionProducto):
        promocionesProducto.append(val)



