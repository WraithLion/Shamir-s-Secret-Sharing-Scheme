from Desencriptar import descifrar
from SSSS import ocultar

class menu():

    def Encriptar(self):
        Encripta = ocultar()
        key = Encripta.get_key()
        shares = Encripta.get_shares(key)
        Encripta.print_shares(shares)
        Encripta.encrypt(key)

    def Desencriptar(self):
        #Llama a la clase descifrar
        Desencripta=descifrar()
        #Obtiene las claves requeridas para desencriptar el archivo
        shares = Desencripta.get_shares()
        #Obtiene una llave a partir de las claves dadas
        key = Desencripta.get_key(shares)
        #Desencripta el archivo
        Desencripta.decrypt(key)
    def RegresarMenu(self):
        print("\n\nVolviendo al menú principal...\n\n")
    def Ejecutable(self):
        while True:
            try:
                opcion=int(input("\n-------------------------------------------------------\nBienvenido a ENDEcryptApp, ¿Qué te gustaría hacer?\n\n1.-Encriptar un archivo\n\n2.-Desencriptar un archivo\n\n3.-Salir\n------------------------------------------------------\n"))
                if opcion==1:
                    self.Encriptar()
                    self.RegresarMenu()
                elif opcion==2:
                    self.Desencriptar()
                    self.RegresarMenu()
                elif opcion==3:
                    print("\n\n\nGracias por usar nuestra aplicación, vuelve pronto\n\n")
                    break
                elif opcion<1 or opcion>3:
                    self.error()

            except ValueError:
                self.error()

    def error(self):
        print('Opción no válida, intente de nuevo...')
Aplicacion=menu()
Aplicacion.Ejecutable()
