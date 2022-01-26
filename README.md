# Shamir-s-Secret-Sharing-Scheme

#1. Introducción

El Esquema de Secreto Compartido de Shamir (Shamir's Secret Sharing Scheme o SSSS por sus siglas en inglés) es un algoritmo criptográfico descrito y publicado
por primera vez a nombre de Adi Shamir en el escrito "How to Share a Secret", publicado en Abril de 1979.

Este algoritmo fue pensado en consideración de resolver un problema presente en aquel momento, el cual dice lo siguiente:

Once científicos están trabajando en un proyecto secreto. Ellos quieren asegurar los documentos en un gabinete, de modo que el gabinete se pueda abrir si 
y sólo si seis o más de los científicos están presentes. ¿Cuál es el menor número de candados requeridos? ¿Cuál es el menor número de llaves
necesarias que cada científico debe portar?

La solución de aquel problema dictaba que se requería de un número impráctico de candados y llaves, lo que motivó a un método más eficiente para la resolución del problema.
En palabras del mismo, consiste de un esquema basado en interpolación polinomial: dado k puntos en un plano 2-dimensional (x_1,y_1),...,(x_k,y_k) con distintos valores x_i, 
existe uno y sólo un polinomio q(x) de grado k-1 tal que q(x_i)=y, para toda i.

A partir de este razonamiento n claves son generadas de modo que cada una de estas representan un punto que define un polinomio de grado k-1.

<div align="center">
    <img src="https://i.postimg.cc/63wQNnDB/imagen-2022-01-25-205810.png"</img> 
</div>

El coeficiente a_0 se trata de la clave secreta. Los demás coeficientes son generados de manera aleatoria y son descartadas tan pronto sean creadas las claves.

Cada clave representa una tupla (x_i,y_i), siendo estas las coordenadas de un punto del polinomio q(x), siendo x_i un único y arbitrario número asignado por el esquema y y_i=q(x_i). 

La clave secreta puede ser usada como llave para acceder a un proyecto, información o cualquier ente que quiera ocultarse a la vista de agentes externos, esta clave se nos dará al introducir las claves dadas con anterioridad en el Esquema de Shamir.

Una vez dicho esto, el proyecto consiste en crear un programa que emule lo anterior descrito de tal manera que, a partir de la clave secreta, se descencripte un archivo .txt dado.

# 2. Ejecución del programa

Para proceder a ejecutar el programa, se requerirá primeramente que se descargue la carpeta Shamir-s-Secret-Sharing-Scheme-main adjunto a su contenido.

Posteriormente, se ejecutará el archivo Encriptar.pyw localizado en Esteganografia/, éste archivo se puede ejecutar ya sea dando doble click al archivo, dentro de una terminal
(esto se puede realizar utilizando el comando "python3 Main.pyw", asegúrate de que la terminal se encuentre en la carpeta donde se ubica "Main.pyw" usando el comando cd, de lo contrario te marcará el error de archivo no encontrado) o ejecutando el script con algún IDE (como lo es el caso del programa Anaconda, Spider o Visual Studio Core disponible para Windows, Linux y Mac, puedes consultar el método de instalación en el siguiente enlace: https://docs.anaconda.com/anaconda/install/index.html)

Con lo anterior realizado, usted verá que se iniciará el programa mostrando en pantalla una interfaz en donde se mostrarán las siguientes opciones:

1. Seleccionar imagen: Esta opción permite seleccionar la imagen a modificar, ya sea para esconder u obtener un mensaje oculto.
2. Ocultar: Una vez seleccionado la imagen del apartado anterior, se le pedirá seleccionar el archivo .txt donde se tendrá el mensaje a ocultar para posteriormente solicitar el nombre y localización donde se almacenará la imagen modificada.
3. Develar: Igualmente se requeríra de Seleccionar imagen, su función es la de obtener el mensaje oculto en una imagen, este mensaje se almacenará en forma de un archivo .txt con el nombre que especifique el usuario

# 3. Información del contenido

A continuación se mostrará la lista de elementos contenidos en Estenografía junto a una somera descripción de los mismos:

Estenografía/

1. README.md: Es el archivo que está leyendo en este momento
2. Proyecto_Aguirre_Leonardo_Valencia_Jonathan.pdf: Se trata de un archivo en formato pdf que explica en mayor profundidad lo realizado en el proyecto

Estenografía/RevealShowApp/

1. Main.py: Es el archivo principal para la ejecución del programa
2. Imagen.py: Se almacenan los métodos necesarios para el procesamiento de imágenes
3. Develar.py: En este archivo se encuentra el procedimiento necesario para obtener el mensaje oculto por estenografía LSB de una imagen
4. Ocultamiento.py: Se guarda la clase que se encarga de ocultar un mensaje en una imagen por medio de estenografía LSB
5. Mensaje.py: Se almacenan los métodos necesarios para el procesamiento de archivos .txt
