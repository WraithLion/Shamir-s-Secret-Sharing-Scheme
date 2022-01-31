from Desencriptar import descifrar
from SSSS import ocultar
from tkinter import messagebox
class menu():

    def Encriptar(self):
        #Llama la clase ocultar
        Encripta = ocultar()
        #Genera la llave
        key = Encripta.get_key()
        #Fragmenta la llave para encriptar el archivo
        shares = Encripta.get_shares(key)
        #Muestra los fragmentos generados en forma de clave
        Encripta.print_shares(shares)
        #Encripta el archivo solicitado
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
        messagebox.showinfo(message="Regreando al menú principal", title="Regresando")
    def Ejecutable(self):
        global opcion
        opcion=None
        while opcion is None or opcion<1 or opcion !=3:
            try:
                opcion=int(input("\n-------------------------------------------------------\nBienvenido a ENDEcryptApp, ¿Qué te gustaría hacer?\n\n1.-Encriptar un archivo\n\n2.-Desencriptar un archivo\n\n3.-Salir\n------------------------------------------------------\n"))
                if opcion==1:
                    self.Encriptar()
                    self.RegresarMenu()
                elif opcion==2:
                    self.Desencriptar()
                    self.RegresarMenu()
                elif opcion==3:
                    messagebox.showinfo(message="Gracias por usar nuestra aplicación, vuelve pronto", title="Agradecimiento")
                    break
                elif opcion<1 or opcion>3:
                    self.error()

            except ValueError:
                self.error()

    def error(self):
        messagebox.showinfo(message="Opcion invalida, intenta de nuevo", title="Aviso")
Aplicacion=menu()
Aplicacion.Ejecutable()
