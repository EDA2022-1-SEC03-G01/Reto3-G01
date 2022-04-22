"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

from asyncio.proactor_events import _ProactorDuplexPipeTransport
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar informacion de jugadores")
    print("3- Reportar las cinco adquisiciones mas recientes del club")
    print("4- Reportar los jugadores de cierta posicion dentro de un rango de desempeño, potencial y salario")
    print("5- Reportar los jugadores dentro de un rango salarial y con cierta etiqueta")
    print("6- Reportar los jugadores con cierto rasgo caracteristico y nacidos en un periodo de tiempo")
    print("7- Graficar el histograma de una propiedad para los jugadores FIFA")
catalog = None

"""
Funciones para imprimir la informacion
"""
def printLoadInfo(cont):
    pass
def printAdquisitionsInfo(cont,club_name):
    pass
def printPlayersByPosDesPotSal(cont,pos,desempeñoLow,desempeñoUp,potencialLow,potencialUp,salarioLow,salarioUp):
    pass
def printPlayersBySalCar(cont,salarioLow,salarioUp,caracteristica):
    pass
def  printPlayersByNacRas(cont,nacimientoLow,nacimientoUp,rasgo):
    pass
def printHistogram(cont,segmentosPropiedad,nivelesMarcas,propiedad):
    pass
"""
Menu principal
"""
cont = None

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("\nInicializando....")
        cont= controller.inicializar()
    elif int(inputs[0]) == 2:
        print("\nCargando informacion de jugadores...")
        controller.loadData(cont)
        printLoadInfo(cont)
    elif int(inputs[0]) == 3:
        club_name=input('Ingrese el nombre del club: ')
        print("Buscando las cinco adquisiciones mas recientes del club " + club_name+"...")
        printAdquisitionsInfo(cont,club_name)
    elif int(inputs[0]) == 4:
        pos=input('Ingrese la posicion del jugador: ')
        desempeñoLow=input('Ingrese el limite inferior para el desempeño global del jugador: ')
        desempeñoUp=input('Ingrese el limite superior para el desempeño global del jugador: ')
        potencialLow=input('Ingrese el limite inferior para el potencial del jugador: ')
        potencialUp=input('Ingrese el limite superior para el potencial de jugador: ')
        salarioLow=input('Ingrese el limite inferior para el salario de los jugadores: ')
        salarioUp=input('Ingrese el limite superior para el salario del jugador: ')
        printPlayersByPosDesPotSal(cont,pos,desempeñoLow,desempeñoUp,potencialLow,potencialUp,salarioLow,salarioUp)
    elif int(inputs[0]) == 5:
        salarioLow=input('Ingrese el limite inferior del salario recibido por los jugadores: ')
        salarioUp=input('Ingrese el limite superior del salario recibido por los jugadores: ')
        caracteristica=input('Ingrese una caracteristica de juego especifica que identifica a los jugadores: ')
        printPlayersBySalCar(cont,salarioLow,salarioUp,caracteristica)
    elif int(inputs[0]) == 6:
        nacimientoLow=input('Ingrese el limite inferior de la fecha del nacimiento del jugador: ')
        nacimientoUp=input('Ingrese el limite superior de la fecha de nacimiento del jugador: ')
        rasgo=input('Ingrese un rasgo caracteristico que identifique a los jugadores: ')
        printPlayersByNacRas(cont,nacimientoLow,nacimientoUp,rasgo)
    elif int(inputs[0]) == 7:
        segmentosPropiedad=input('Ingrese el numero de segmentos en que se divide el rango de propiedad en el histograma: ')
        nivelesMarcas=input('Ingrese el numero de niveles en que se dividen las marcas de jugadores en el histograma: ')
        propiedad=input('Ingrese la propiedad de la cual se va ahacer el histograma: ')
        printHistogram(cont,segmentosPropiedad,nivelesMarcas,propiedad)
    else:
        sys.exit(0)
sys.exit(0)
