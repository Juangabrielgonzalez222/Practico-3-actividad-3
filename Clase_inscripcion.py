class Inscripcion():
    __fechaInscricion=None
    __pago=False
    __persona=None
    __taller=None
    def __init__(self,fecha,persona,taller,pago=False,):
        from Clase_persona import Persona
        from Clase_taller import TallerCapacitacion
        if (type(persona)==Persona and type(taller)==TallerCapacitacion):
            self.__fechaInscricion=fecha
            self.__pago=pago
            self.__persona=persona
            self.__taller=taller
        else:
            print("No se inicializo la inscripción, no hay instancias de clases correctas")
    def modificarPago(self):
        self.__pago=True
    def getPersona(self):
        return self.__persona
    def getPago(self):
        return self.__pago
    def getTaller(self):
        return self.__taller
    def getFecha(self):
        return self.__fechaInscricion