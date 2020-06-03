import numpy as np
from Clase_inscripcion import Inscripcion
class ManejadorInscripciones():
    __arregloInscripciones=None
    __cantidad=0
    __dimension=0
    __incremento=5
    def __init__(self,dimension=5,incremento=5):    
        self.__arregloInscripciones=np.empty(dimension,dtype=Inscripcion)
        self.__dimension=dimension
        self.__incremento=incremento
        self.__cantidad=0
    def agregarInscripcion(self,inscripcion):
        if (type(inscripcion)==Inscripcion):
            if self.__cantidad==self.__dimension:
                self.__dimension+=self.__incremento
                self.__arregloInscripciones.resize(self.__dimension)
            self.__arregloInscripciones[self.__cantidad]=inscripcion
            self.__cantidad+=1
        else:
            print("No se añadio una inscripción, el parametro no era un objeto de tipo Inscripcion ")
    def consultarInscripcion(self,dni):            
        pos=self.buscarInscripcionPorDNI(dni)
        if(pos!=-1):
            taller=self.__arregloInscripciones[pos].getTaller()
            nombre=taller.getNombre()
            if(self.__arregloInscripciones[pos].getPago()):
                print("Taller: ",nombre," ,No adeuda")
            else:
                print("Taller:",nombre,"Adeuda: ",taller.getMonto())
        else:
            print("No se encontro el DNI")
    def buscarInscripcionPorDNI(self,dni):
        bandera=True
        i=0
        posicion=-1
        while(i<len(self.__arregloInscripciones) and bandera):
            if self.__arregloInscripciones[i]!=None:
                persona=self.__arregloInscripciones[i].getPersona()
                if(dni==persona.getDNI()):
                    bandera=False
                    posicion=i
            i+=1
        return posicion
    def registrarPagoPorDNI(self,dni):
        pos=self.buscarInscripcionPorDNI(dni)
        if(pos!=-1):
            if(self.__arregloInscripciones[pos].getPago()):
                print("La persona ya acredito el pago")
            else:
                self.__arregloInscripciones[pos].modificarPago()
                print("Se registro el pago")
        else:
            print("No se encontro el DNI")
    def almacenarInscripciones(self):
        import csv
        archivo=open("inscripciones.csv","w",newline='')
        writer=csv.writer(archivo,delimiter=";")
        for inscripcion in self.__arregloInscripciones:
            if(inscripcion!=None):
                taller=inscripcion.getTaller()
                persona=inscripcion.getPersona()
                fecha=inscripcion.getFecha()
                pago=inscripcion.getPago()
                writer.writerow([persona.getDNI(),str(taller.getId()),fecha,str(pago)])
        archivo.close()
    def testInscripciones(self):
        from Clase_persona import Persona
        from Clase_manejadorTalleres import ManejadorTalleres
        from Clase_taller import TallerCapacitacion
        manejadorIns=ManejadorInscripciones()
        manejadortall=ManejadorTalleres()
        manejadortall.agregarTaller(TallerCapacitacion(1,"Taller de Confección",2,1500))
        manejadortall.agregarTaller(TallerCapacitacion(2,"Taller de Programación",3,2000))
        print("Talleres:")
        manejadortall.mostrarTalleres()
        persona1=Persona("Juan Fernandez", "Nueva españa 234N","40321789")
        persona2=Persona("Jose Hernandez", "Av. Libertador 524N","41322584")
        persona3=Persona("Agustin Amaya", "Nueva America 1678O","39348321")
        inscripcion=manejadortall.inscribirPersona(persona1,1,"23/05/2020")
        manejadorIns.agregarInscripcion(inscripcion)
        inscripcion=manejadortall.inscribirPersona(persona2,1,"20/05/2020")
        manejadorIns.agregarInscripcion(inscripcion)
        inscripcion=manejadortall.inscribirPersona(persona3,2,"23/05/2020")
        manejadorIns.agregarInscripcion(inscripcion)
        print("Se consultan inscriptos en ambos talleres:")
        print("Taller 1:")
        manejadortall.consultarInscriptos(1)
        print("Taller 2")
        manejadortall.consultarInscriptos(2)
        print("Se guardan inscripciones al csv:")
        manejadorIns.almacenarInscripciones()
        print("Se consulta si adeuda:")
        print("Se consulta inscripción de la persona con DNI:41322584 ")
        manejadorIns.consultarInscripcion("41322584")
        manejadorIns.registrarPagoPorDNI("41322584")
        print("Se consulta si adeuda luego de registrar pago:")
        manejadorIns.consultarInscripcion("41322584")