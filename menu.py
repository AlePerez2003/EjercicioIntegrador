from alumno import Alumno
from manejadorAlumnos import Alumnos
from materiasAprobadas import MateriasAprobadas
from manejadorMateriasAp import ManjeadorMateriasAp
import numpy as np

class Menu:
    __codigo: int
    
    def __init__(self, codigo = 0):
        self.__codigo = codigo
        
    def mostrar_menu(self):
        print('Opción 1: informar el promedio con aplazos y sin aplazos de un alumno')
        print('Opción 2: informar los estudiantes de una materia que la aprobaron en forma promocional, con nota mayor o igual que 7')
        print('Opción 3: Obtener listado ordenado de alumnos')
        print('Opción 0: finalizar operación')
        print('')
    
    def ejecutar_menu(self, materias:ManjeadorMateriasAp, alumnos:Alumnos):
        self.mostrar_menu()
        self.__cod = int(input('Ingrese el código'))
        while self.__cod != 0:
            if self.__cod == 1:
                self.opcion1(materias)
            elif self.__cod == 2:
                self.opcion2(materias, alumnos)
            elif self.__cod == 3:
                self.opcion3(alumnos)
            else: 
                print('Codigo incorrecto')
            self.mostrar_menu
            self.__cod = int(input('Ingrese el código'))
        return
    
    def opcion1 (self, materias:ManjeadorMateriasAp):
        materias.comunicar_promedios()
        
    def opcion2 (self, materias:ManjeadorMateriasAp, alumnos:Alumnos):
        materia = input('Ingrese el nombre de una materia')
        materias.informarAprobados(materia, alumnos)
        
    def opcion3 (self, alumnos:Alumnos):
        lista = alumnos.ordenar()
        for alumno in lista:
            print(alumno)