from Clase_persona import Persona 
class ManejadorPersonas:
    __personas=[]
    def __init__(self):
        self.__personas=[]
    def agregarPersona(self,persona):
        if type(persona)==Persona:
            self.__personas.append(persona)
        else:
            print("El parametro no es instancia de la clase Persona")
    def buscarPersonaDni(self,dni):
        i=0
        while(i<len(self.__personas) and self.__personas[i].getDNI()!=dni):
            i+=1
        if(not(i<len(self.__personas))):
            i=-1
        return i