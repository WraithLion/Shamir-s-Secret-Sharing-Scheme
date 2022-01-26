# Shamir-s-Secret-Sharing-Scheme

El Esquema de Secreto Compartido de Shamir (Shamir's Secret Sharing Scheme o SSSS por sus siglas en inglés) es un algoritmo criptográfico descrito y publicado
por primera vez a nombre de Adi Shamir en el escrito "How to Share a Secret", publicado en Abril de 1979.

Este algoritmo fue pensado en consideración de resolver un problema presente en aquel momento, el cual dice lo siguiente:

Once científicos están trabajando en un proyecto secreto. Ellos quieren asegurar los documentos en un gabinete, de modo que el gabinete se pueda abrir si 
y sólo si seis o más de los científicos están presentes. ¿Cuál es el menor número de candados requeridos? ¿Cuál es el menor número de llaves
necesarias que cada científico debe portar?

La solución de aquel problema dictaba que se requería de un número impráctico de candados y llaves, lo que motivó a un método más eficiente para la resolución del problema.
En palabras del mismo, consiste de un esquema basado en interpolación polinomial: dado k puntos en un plano 2-dimensional <img src="https://latex.codecogs.com/svg.image?(x_1,y_1),...,(x_k,y_k)" title="(x_1,y_1),...,(x_k,y_k)" /> con distintos valores <img src="https://latex.codecogs.com/svg.image?x_i" title="x_i" />, 
existe uno y sólo un polinomio <img src="https://latex.codecogs.com/svg.image?q(x)" title="q(x)" /> de grado <img src="https://latex.codecogs.com/svg.image?k-1" title="k-1" /> tal que <img src="https://latex.codecogs.com/svg.image?\bg_black&space;q(x_i)=y&space;" title="\bg_black q(x_i)=y " />, para toda i.

<div align="center">
    <img src="https://i.postimg.cc/63wQNnDB/imagen-2022-01-25-205810.png"</img> 
</div>
