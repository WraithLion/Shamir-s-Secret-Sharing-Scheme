# Shamir-s-Secret-Sharing-Scheme

El Esquema de Secreto Compartido de Shamir (Shamir's Secret Sharing Scheme o SSSS por sus siglas en inglés) es un algoritmo criptográfico descrito y publicado
por primera vez a nombre de Adi Shamir en el escrito "How to Share a Secret", publicado en Abril de 1979.

Este algoritmo fue pensado en consideración de resolver un problema presente en aquel momento, el cual dice lo siguiente:

Once científicos están trabajando en un proyecto secreto. Ellos quieren asegurar los documentos en un gabinete, de modo que el gabinete se pueda abrir si 
y sólo si seis o más de los científicos están presentes. ¿Cuál es el menor número de candados requeridos? ¿Cuál es el menor número de llaves
necesarias que cada científico debe portar?

La solución de aquel problema dictaba que se requería de un número impráctico de candados y llaves, lo que motivó a un método más eficiente para la resolución del problema.
En palabras del mismo, consiste de un esquema basado en interpolación polinomial: dado k puntos en un plano 2-dimensional (x_1,y_1),...,(x_k,y_k) con distintos valores x_i, 
existe uno y sólo un polinomio q(x) de grado k-1 tal que q(x_i)=y, para toda i.

<div align="center">
    [![imagen-2022-01-25-205810.png](https://i.postimg.cc/63wQNnDB/imagen-2022-01-25-205810.png)](https://postimg.cc/v1qyrgYK) 
</div>
