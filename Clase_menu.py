class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1:self.opcion1,
                            2:self.opcion2,
                            3:self.opcion3,
                            4:self.opcion4,
                            5:self.opcion5,
                            6:self.opcion6,
                            7:self.salir
                         }
    def opcion(self,op, manejadorIns, manejadorPer,manejadorTall):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if(op<1 or op>7):    
            func()
        else:
            func(manejadorIns,manejadorPer,manejadorTall)
    def salir(self,manejadorIns,manejadorPer,manejadorTall):
        print('Usted salio del programa')
    def opcion1(self,manejadorIns,manejadorPer,manejadorTall):
        from Clase_persona import Persona
        print("Ingrese datos de la persona:")
        nombre=input("Nombre:")
        direccion=input("Dirección:")
        dni=input("DNI:")
        persona=Persona(nombre, direccion, dni)
        dia=input("Ingrese día de inscripción:")
        mes=input("Ingrese mes de inscripción:")
        año=input("Ingrese año:")
        fecha=dia+"/"+mes+"/"+año
        manejadorTall.mostrarTalleres()
        id=int(input("Ingrese el id del taller:"))
        registrar=manejadorTall.inscribirPersona(persona,id,fecha)
        while (registrar==-10):
            print("Id incorrecto,vuelva a intentarlo:")
            manejadorTall.mostrarTalleres()
            id=int(input("Ingrese el id del taller:"))
            registrar=manejadorTall.inscribirPersona(persona,id,fecha)
        if(registrar!=-100):
            manejadorPer.agregarPersona(persona)
            manejadorIns.agregarInscripcion(registrar)
        else:
            print("No quedan vacantes para la inscripción")
    def opcion2(self,manejadorIns,manejadorPer,manejadorTall):
        dni=input("Ingrese el DNI de la persona:")
        busqueda=manejadorPer.buscarPersonaDni(dni)
        if busqueda!=-1:
            manejadorIns.consultarInscripcion(dni)
        else:
            print("No se encontro el DNI")
    def opcion3(self,manejadorIns,manejadorPer,manejadorTall):
        manejadorTall.mostrarTalleres()
        id=int(input("Ingrese el id del taller:"))
        manejadorTall.consultarInscriptos(id)
    def opcion4(self,manejadorIns,manejadorPer,manejadorTall):
        dni=input("Ingrese el DNI de la persona:")
        busqueda=manejadorPer.buscarPersonaDni(dni)
        if busqueda!=-1:
            manejadorIns.registrarPagoPorDNI(dni)
        else:
            print("No se encontro el DNI")
    def opcion5(self,manejadorIns,manejadorPer,manejadorTall):
        manejadorIns.almacenarInscripciones()
    def opcion6(self,manejadorIns,manejadorPer,manejadorTall):
        manejadorIns.testInscripciones()