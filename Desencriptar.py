# Programa creado y elaborado por Valencia Cruz Jonathan Josué y Leonardo Aguirre Muñoz

#Se importan las librerías necesarias para el proyecto
from binascii import unhexlify
from Crypto.Cipher import AES
from Crypto.Protocol.SecretSharing import Shamir
from tkinter import filedialog
from tkinter import *
from pathlib import *
import os

#Sirve para descifrar un archivo encriptado dado
class descifrar:
    
    #Se almacenan las claves dadas por el usuario
    def get_shares(self):
        
        #Inicia un arreglo en donde irán las claves
        shares = []
        
        #Sirve para el manejo de errores
        while True:
            try:
                #Le pregunta al usuario el número de claves requeridas
                personas = int(input("\n\nIngresa el número de personas presentes: \n"))
                if personas<1:
                    self.error()
                break
            except ValueError:
                self.error()
                
        #Inicia un ciclo en donde se almacenarán las respectivas claves
        for x in range(personas):
            
            #Le pregunta al usuario la clave
            cadena = input("\n\nIngresa tu clave: \n")
            
            #Separa el número y la clave
            cadena = cadena.strip()
            tupla = cadena.split(sep=':', maxsplit=1)
            clave=tupla[1].split(sep='b', maxsplit=1)
            
            #Almacena el número y clave en el arreglo shares
            shares.append((int(tupla[0]),unhexlify(clave[1].strip('\''))))
    
        #Regresa el arreglo de claves dadas por el usuario
        return shares

    #Obtiene la llave con las claves dadas por el usuario
    def get_key(self,shares):
    
        #En caso de algún error, imprime un mensaje en pantalla
        try:
            #Combina las claves y obtiene la llave
            key = Shamir.combine(shares)
        except ValueError:
            print("\n\nLas claves son incorrectas\n\n")
        
        #Regresa la llave
        return key

    #Envia un mensaje de error
    def error(self):
        print('\n\nNúmero no válido, por favor intente de nuevo\n')
        
    #Desencripta el archivo dado por el usuario a partir de la llave
    def decrypt(self,key):
        
        #inicializa la interfaz gráfica
        root = Tk()
        root.withdraw()
        root.update()
        
        #Le solicita al usuario el archivo a desencriptar
        ruta = filedialog.askopenfilename(defaultextension='.txt',filetypes = [("Formato txt", ".txt")],title="Selecciona el archivo .txt")   
        #Le pide al usuario el nombre y ruta del nuevo archivo desencriptado
        guardar = filedialog.asksaveasfilename(defaultextension='.txt',filetypes = [("Formato txt", ".txt")],title="Guardar como")
        
        #Cierra la ventana restante
        root.destroy()
        
        #Obtiene la ruta de guardar
        direccion = PurePath(guardar)
        #Cambia la ruta en que se situa el usuario
        os.chdir(direccion.parents[0])
        #Obtiene el nombre de guardar
        nombre = PurePath(guardar).name
        
        #Declara y acorta el comando read
        with open(ruta, "rb") as fi:
            #Obtiene las variables almacenadas en el archivo encriptado
            nonce, tag = [ fi.read(16) for x in range(2) ]
            #Realiza una nueva llave AES
            cipher = AES.new(key, AES.MODE_EAX, nonce)
            #En caso de que la llave sea incorrecta, imprime un mensaje en pantalla
            try:
                #Verifica que la llave sea correcta
                result = cipher.decrypt(fi.read())
                cipher.verify(tag)
                #Declara y acorta el comando write
                with open(guardar, "wb") as fo:
                    #En caso de ser correcta la llave, crea el archivo desencriptado
                    fo.write(result)
            except ValueError:
                print("Las claves son incorrectas, son insuficientes o no son las correspondientes del archivo")


