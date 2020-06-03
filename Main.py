from Clase_manejadorInscripciones import ManejadorInscripciones
from Clase_manejadorPersonas import ManejadorPersonas
from Clase_manejadorTalleres import ManejadorTalleres
from Clase_menu import Menu
if __name__ =="__main__":
    manejadorIns=ManejadorInscripciones()
    manejadorPer=ManejadorPersonas()
    manejadorTall=ManejadorTalleres()
    menu=Menu()
    op=None
    error=manejadorTall.CargarTalleres()
    if(error!=-100):
        print("Bienvenido al programa:")
        while(op!=7):
            print("Ingrese 1 para inscribir una persona")
            print("Ingrese 2 para consultar inscripción ")
            print("Ingrese 3 para consultar inscriptos ")
            print("Ingrese 4 para registrar pago")
            print("Ingrese 5 para guardar inscripciones en un archivo csv")
            print("Ingrese 6 para realizar un test")
            print("Ingrese 7 para salir")
            op=int(input("Ingrese opcion:"))
            menu.opcion(op, manejadorIns, manejadorPer,manejadorTall)
    else:
        print("Ocurrio un error en el archivo, fin de ejecución")