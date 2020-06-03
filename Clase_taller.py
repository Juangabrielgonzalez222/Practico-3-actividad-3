class TallerCapacitacion():
    __idTaller=0
    __nombre=""
    __vacantes=0
    __montoInscripcion=0
    __inscripciones=[]
    def __init__(self,idtaller,nombre,vacantes,montoinscripcion):
        self.__idTaller=idtaller
        self.__nombre=nombre
        self.__vacantes=vacantes
        self.__montoInscripcion=montoinscripcion
        self.__inscripciones=[]
    def getId(self):
        return self.__idTaller
    def getNombre(self):
        return self.__nombre
    def agregarInscripcion(self,inscripcion):
        from Clase_inscripcion import Inscripcion
        if(type(inscripcion)==Inscripcion):
            self.__inscripciones.append(inscripcion)
            self.__vacantes-=1
        else:
            print("La inscripción no es instancia de Inscripcion")
    def getMonto(self):
        return self.__montoInscripcion
    def getVacantes(self):
        return self.__vacantes
    def mostrarDatosInscriptos(self):
        if len(self.__inscripciones)==0:
            print("No hay inscriptos")
        else:
            for inscripcion in self.__inscripciones:
                print(inscripcion.getPersona())
    def __str__(self):
        cadena="ID: "+str(self.__idTaller)+" Nombre: "+self.__nombre+" Vacantes: "+str(self.__vacantes)+" Monto: "+str(self.__montoInscripcion)
        return cadena