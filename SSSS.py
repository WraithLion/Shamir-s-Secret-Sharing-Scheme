# Programa creado y elaborado por Valencia Cruz Jonathan Josué y Leonardo Aguirre Muñoz

#Se importan las librerías binascii y Crypto
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
from pathlib import *
import os
from binascii import hexlify
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.SecretSharing import Shamir

class ocultar:
    
    #Genera la llave requerida para la encriptación del archivo
    def get_key(self):
    
        #Genera un número de 16 bits al azar
        key = get_random_bytes(16)
        #Regresa la clave secreta generada
        return key

    #Genera claves usando el Esquema de Shamir a partir de una llave
    def get_shares(self,key):

        total_shares = None
        #Le pregunta al usuario el número de claves correspondientes
        while total_shares is None or total_shares<1:
            try:
                total_shares = int(input("\n\nIngresa el número total de claves a generar: \n"))
            except:
                self.error()
        req_shares=None
        while req_shares is None or req_shares<0 or req_shares>total_shares:
            try:
                req_shares = int(input("\n\nIngresa el número requerido de claves para la desencriptación del archivo: \n"))
            except ValueError:
                self.error()
        
    
        #Genera las claves usando el Esquema de Shamir
        shares = Shamir.split(req_shares, total_shares, key)
    
        #Regresa las claves generadas por SSSS
        return shares

    def error(self):
        messagebox.showinfo(message="Opcion invalida, intenta de nuevo", title="Aviso")

    #Imprime las claves en pantalla
    def print_shares(self,shares):
        for idx, share in shares:
            print("-------------------------------------------\n%d: %s" % (idx, hexlify(share)))

    #Encripta un archivo dado
    def encrypt(self,key):

        global ruta
        ruta=None
        while ruta is None:
            try:
                ruta = filedialog.askopenfilename(defaultextension='.txt',filetypes = [("Formato txt", ".txt")],title="Selecciona el archivo .txt")
            except:
                self.error()
                ruta = filedialog.askopenfilename(defaultextension='.txt',filetypes = [("Formato txt", ".txt")],title="Selecciona el archivo .txt")
        global guardar
        guardar=None
        while guardar is None:
            try:
                guardar = filedialog.asksaveasfilename(defaultextension='.txt',filetypes = [("Formato txt", ".txt")],title="Guardar como")
            except:
                self.error()
                guardar = filedialog.asksaveasfilename(defaultextension='.txt',filetypes = [("Formato txt", ".txt")],title="Guardar como")
            pass
            direccion = PurePath(guardar)
            os.chdir(direccion.parents[0])
            nombre = PurePosixPath(guardar).name
            with open(ruta, "rb") as fi, open(nombre, "wb") as fo:
                cipher = AES.new(key, AES.MODE_EAX)
                ct, tag = cipher.encrypt(fi.read()), cipher.digest()
                nonce = cipher.nonce
                fo.write(nonce + tag + ct)
    
