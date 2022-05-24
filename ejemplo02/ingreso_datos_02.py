from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_tablas import Club, Jugador

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

jugador= open("data/datos_jugadores.txt", "r")

registros = jugador.readlines()

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
    session.query(Club).filter_by(nombre="LDU").one()


session.commit()






