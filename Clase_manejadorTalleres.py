import numpy as np
import csv
from Clase_taller import TallerCapacitacion
class ManejadorTalleres:
    __arregloTalleres=None
    __cantidad=0
    __dimension=0
    __incremento=5
    def __init__(self,dimension=1,incremento=5):    
        self.__arregloTalleres=np.empty(dimension,dtype=TallerCapacitacion)
        self.__dimension=dimension
        self.__incremento=incremento
        self.__cantidad=0
    def agregarTaller(self,taller):
        if type(taller)==TallerCapacitacion:
            if self.__cantidad==self.__dimension:
                self.__dimension+=self.__incremento
                self.__arregloTalleres.resize(self.__dimension)
            self.__arregloTalleres[self.__cantidad]=taller
            self.__cantidad+=1
        else:
            print("No se añadio un taller, el parametro no era objeto de tipo TallerCapacitacion")
    def redimensionarArreglo(self,dimension):
        self.__dimension=dimension
        self.__arregloTalleres.resize(dimension)
    def CargarTalleres(self):
        archivo=open("talleres.csv")
        reader=csv.reader(archivo,delimiter=";")
        error=None
        for fila in reader:
            if(len(fila)==4):
                self.agregarTaller(TallerCapacitacion(int(fila[0]),fila[1],int(fila[2]),int(fila[3])))
            elif(len(fila)==1):
                self.redimensionarArreglo(int(fila[0]))
            else:
                print("Hay un error en una linea del archivo, por favor revisar el archivo")
                error=-100
        archivo.close()
        return error
    def mostrarTalleres(self):
        for taller in self.__arregloTalleres:
            if(taller!=0):
                print(taller)
    def inscribirPersona(self,persona,idtaller,fecha):
        from Clase_persona import Persona
        from Clase_inscripcion import Inscripcion
        inscripcion=None
        if(type(persona)==Persona):
            posicion=self.buscarTallerPorId(idtaller)
            if(posicion!=-1):
                if self.__arregloTalleres[posicion].getVacantes()>0:
                    inscripcion=Inscripcion(fecha,persona,self.__arregloTalleres[posicion])
                    self.__arregloTalleres[posicion].agregarInscripcion(inscripcion)
                else:
                    inscripcion=-100
            else:
                print("Id de taller incorrecto, no se encontro el taller")
                inscripcion=-10
        else:
            print("El parametro recibido no coincide con la clase Persona, no se pudo realizar la inscripción")
        return inscripcion
    def buscarTallerPorId(self,id):
        i=0
        while(i<len(self.__arregloTalleres) and self.__arregloTalleres[i].getId()!=id):
            i+=1
        if(not(i<len(self.__arregloTalleres))):
            i=-1
        return i
    def consultarInscriptos(self,id):
        posicion=self.buscarTallerPorId(id)
        if(posicion!=-1):
            self.__arregloTalleres[posicion].mostrarDatosInscriptos()
        else:
            print("No se encontro el ID")
        