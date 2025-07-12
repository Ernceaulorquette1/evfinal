#productos= { modelo: [marca,pantalla,RAM,disco, Gb de DD, procesador, videro],...}

productos = {"8475HD": ["HP",15.6,"8GB","DD","1T","Intel Core i5","Nvidia GTX1050"],
             "2175HD": ["lenovo",14,"4GB","SSD","1512","Intel Core i5","Nvidia GTX1050"],
             "JjfFHD": ["Asus",14,"16GB","SSD","256T","Intel Core i7","Nvidia RTX208Ti"],
             "fgdxHD": ["HP",15.6,"8GB","DD","1T","Intel Core i3","integrada"],
             "GF75HD": ["Asus",15.6,"8GB","DD","1T","Intel Core i7","Nvidia GTX1050"],
             "123FHD": ["lenovo",15.6,"6GB","DD","1T","AMD Ryzen 5","Nvidia integrada"],
             "342HD": ["lenovo",15.6,"8GB","DD","1T","AMD Ryzen /","Nvidia GTX1050"],
             "UWU13HD": ["Dell",15.6,"8GB","DD","1T","AMD RYzen 3","Nvidia GTX1050"],
              }

stock = {"8475HD": [387990,10],
             "2175HD": [327990,4],
             "JjfFHD": [424990,1],
             "fgdxHD": [664990,21],
             "GF75HD": [749990,2],
             "123FHD": [290890,32],
             "342HD": [444990,7],
             "UWU13HD": [3499990,1],
             "fs1230hd":[249990,0],
              }

#MENU PRINCIPAL

def stock_marca():
    marcas= productos.values()
    encontrados = []
    stock_encontre =[]

    for stock1 in stock :
        stock_encontre = stock1[1]

    for marca in marcas :
        marca_a_consulta = marca[0]

        if marca_a_consulta.lower()==marca.lower():
         encontrados.append(stock1[1])
        print(encontrados)
    
    while True: 
        marca=""
        try: 
            marca=input("Ingrese marca a consultar: ")
            break
        except ValueError:
            print("debe encribir la mara")
        else:
             print ("entra la marca de nuevo")

def precio():
    buscar_precio = []
    list_buscar = ["", ""]

def modelo ():



""" def turistas_por_pais(pais):
    valores = turistas.values()
    
    encontrados = []

    for valor in valores:
        pais_valor = valor[1]

        if pais_valor.lower() == pais.lower():
            encontrados.append(valor[0]) """

while True : 
  
    print("***MENU PRINCIPAL***")
    print("1. Stock marca.")
    print("Busqueda por precio")
    print("3.Actualizar precio")
    print("4. Salir")
    
    opcion = 0

    try:
        opcion = int(input("Ingrese opción del Menu principal"))
    except ValueError:
        print("La opción debe ser un número")
    else:
        if opcion == 1:
            stock_marca()
        elif opcion == 2 :
            precio()
        elif opcion == 3 :
            modelo()
        else :
         opcion == 43
            print("Programa finalizado")
         

        
           


