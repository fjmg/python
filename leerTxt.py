
ruta = "/home/fjmg/Documents/Python/Eddy/datosDJugador.txt"
lista = []

with open(ruta) as f:
    for linea in f.readlines():
        lista.append([linea.replace("\n","")])

atleta = {
    "nombre": "Fidel",
    "deporte": "Futbol",
    "pais": "Cuba",
    "medallas": {
        "oro":1,
        "plata":0,
        "bronce":0
    }
}

lista.append(['{0:10} {1:10} {2:10} {3:10}{4:5}{5:5}'.format(atleta["nombre"], atleta["deporte"], atleta["pais"], atleta["medallas"]["oro"], atleta["medallas"]["plata"], atleta["medallas"]["bronce"] )])

with open(ruta, "w") as f:
    for l in lista:
        f.write('{0:10}\n'.format(l[0]))