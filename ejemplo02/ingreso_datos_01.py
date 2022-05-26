from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_tablas import Club, Jugador

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

club= open("data/datos_clubs.txt", "r")
jugador= open("data/datos_jugadores.txt", "r")


registros = club.readlines()
registros = jugador.readlines()


for c in registros:
    nombre = c.split(";")[0]
    deporte = c.split(";")[1]
    fundacion  = c.split(";")[2].replace("\n","")
    print(nombre)
    print(deporte)
    print(fundacion)
    club1 = Club(nombre= nombre, deporte=deporte, fundacion= fundacion)

    session.add(club1)

for j in registros:
    nombre = j.split(";")[0]
    dorsal = j.split(";")[1]
    posicion  = j.split(";")[2].replace("\n","")
    club_id = j.split(";")[3]

    print(nombre)
    print(dorsal)
    print(posicion)
    jugador1 = Jugador(nombre = nombre, dorsal= dorsal, posicion= posicion, club_id= club_id)
    session.add(jugador1)
session.commit()






