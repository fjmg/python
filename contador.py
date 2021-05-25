tabla = []

#Ordeno los datos de la tabla por los puntos
def OrdenarDatos(e):
    return e['puntos']

#Muestro el resultado de la tabla
def MostrarDatos():

    #Aki recorro los datos de la tabla para agregar los puntos por ganados y empatados
    i = 0
    for item in tabla:
        tabla[i]["puntos"] = (item["ganados"]*3) + (item["empates"]*1)
        i= i+1
    
    #Envio los datos a la funcion OrdenarDatos
    #Esta funcion recibe los parametros de tabla para ordenarlos de Mayor a Menos
    tabla.sort(key=OrdenarDatos, reverse=True)

    #Al finalizar muestro los datos de la tabla ya ordenados por puntos
    print(tabla)
        

#Esta funcion crea los datos en la tabla
#Te va pidiendo los datos para conformarla
def IntroducirDatos():
    #En diccionario introdusco los datos
    #Viene en este formato
    #datos = {"equio":"Barcelona", "ganados":12, "empates":3, "perdidos":2}
    datos = {}

    equipo = input("Nombre de equipo: ")
    #aki agrego el nombre del equipo al diccionario
    datos["equipo"] = equipo
    
    #Esta lista tiene los renglones que se tomaran en cuenta para crear la tabla.
    #Puedes agregar cuantos renglones desees. Ej: Goles a favor y encontra, partidos ganados dentro y fuera de casa, etc
    categoria = ['ganados', 'empates', 'perdidos']
    
    #aki creo un while mientras q no desees salir
    i = 0
    while True:
        #Ire pidiendo por categorias.
        print("Juegos {0}: ".format(categoria[i]))
        #Leo la categoria
        c = input()
        #Agrego a al diccionario la categoria y su valor (key:value)
        #Ej: datos["empates"] = 12
        # pongo int(c) para convertirlo a entero, de lo contrario se guarda cmo text y despues no puedes ordenarlo
        datos[categoria[i]] = int(c)
        i+=1    
        #Cuando se han recorrido todas las categorias t pregunto si kieres salir.
        #De salir llamo a la funcion OrdenarDatos. De no salir vuelvo a llamar a la misma funcion. Esto se llama recursividad
        if i >= len(categoria):
            tabla.append(datos)
            i = 0
            s = input('Desea salir(y): ')
            if s == 'y':
                OrdenarDatos()
                exit(0)
            else:
                IntroducirDatos()

IntroducirDatos()
            



