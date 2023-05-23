

|![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.001.png)|**UNIVERSIDAD NACIONAL DE SAN AGUSTIN FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMA**|![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.002.png)|
| - | :-: | - |
|**Formato:** Guía de Práctica de Laboratorio / Talleres / Centros de Simulación|
|**Aprobación: 2022/03/01**|**Código: GUIA-PRLE-001**|**Página:** 1|

**INFORME DE LABORATORIO![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.003.png)**



|**INFORMACIÓN BÁSICA**|
| - |
|**ASIGNATURA:**|PROGRAMACIÓN WEB 2|
|**TÍTULO DE LA PRÁCTICA:**|*JavaScript*|
|**NÚMERO DE PRÁCTICA:**|*02*|**AÑO LECTIVO:**|*2023*|**NRO. SEMESTRE:**|*I*|
|**FECHA DE PRESENTACIÓN**|*22/05/2023*|**HORA DE PRESENTACIÓN**|*23:59 pm*|
|<p>**INTEGRANTE (s):**</p><p>- Alfonso Huacasi Alejandro Sebastian</p>|**NOTA:**||
|<p>**DOCENTE(s):**</p><p>**- Anibal Sardon**</p>|



|**SOLUCIÓN Y RESULTADOS**|
| - |
|<p>**I. SOLUCIÓN DE EJERCICIOS/PROBLEMAS**</p><p>- **GITHUB: [https://github.com/Sebastianzzzin/proyecto.git**](https://github.com/Sebastianzzzin/proyecto.git)**</p><p>- **VIDEO EN FLIPGRID:**</p><p>**Ejercicio 1:** Escriba una función que reciba el número de día de la fecha actual new Date() y devuelva</p>|
|el texto del día de las semanas correspondientes. Por ejemplo si recibe 0, devolvería “Domingo”.|
||
|- La variable declarada day y utilizamos el switch para evaluar el valor devuelto por la función|
|new Date().getDay(). Esta función obtiene el día actual de la semana como un número, donde el|
|domingo es 0, el lunes es 1, y así sucesivamente hasta el día viernes que sería el 6.|
|- Dentro de la estructura switch, se definen varios casos, cada uno correspondiente a un día de la|
|semana. Cuando se encuentra un caso que coincide con el valor devuelto por getDay(), se|
|ejecuta el código asociado a ese caso. En cada caso, se asigna un nombre de día de la semana a|
|la variable "day" correspondiente. Por ejemplo, si el día actual es 0, se asigna el valor|
|"Domingo" a la variable "day".|


|![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.001.png)|**UNIVERSIDAD NACIONAL DE SAN AGUSTIN FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMA**|![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.002.png)|
| - | :-: | - |
|**Formato:** Guía de Práctica de Laboratorio / Talleres / Centros de Simulación|
|**Aprobación: 2022/03/01**|**Código: GUIA-PRLE-001**|**Página:** 2|



- Después de cada asignación, se utiliza la instrucción break para salir del switch y evitar que se ejecuten los casos siguientes.![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.004.png)![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.005.png)
- Fuera del switch, se utiliza el método getElementById("demo") para obtener una referencia al elemento HTML con el id "demo". Se modifica el contenido del elemento HTML usando la propiedad innerHTML. En este caso, se concatena el texto "Hoy es " con el valor de la variable "day" y se asigna como contenido del elemento.

![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.006.png)

|![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.001.png)|**UNIVERSIDAD NACIONAL DE SAN AGUSTIN FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMA**|![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.002.png)|
| - | :-: | - |
|**Formato:** Guía de Práctica de Laboratorio / Talleres / Centros de Simulación|
|**Aprobación: 2022/03/01**|**Código: GUIA-PRLE-001**|**Página:** 3|

![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.007.jpeg)

**Ejercicio 2:** Escriba una página web que reciba un texto y al presionar un botón muestre el mismo texto invertido en otra sección (div). Por ejemplo si se escribe “Hola”, se mostraría como “aloH”.![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.008.png)

- Se define una función llamada textoInvertido que toma un parámetro t.
- Dentro de la función, se obtiene el valor de un elemento HTML utilizando document.getElementById(t).value.![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.009.png) El parámetro t representa el id del elemento HTML que contiene el texto que se desea invertir, eso almacena la variable x.![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.010.png)
- Se declara una variable llamada aux para almacenar el texto invertido. Se inicializa como una cadena vacía.![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.011.png)

\-

- Se inicia un bucle for que recorre cada carácter del texto, comenzando desde el último carácter (x.length-1)![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.012.png) hasta el primer carácter (0), en orden inverso. En cada iteración del bucle, se agrega el carácter actual al final de la cadena aux utilizando x.charAt(i).
- Después de que el bucle for finalice, se actualiza el contenido de un elemento HTML con el id "rpta" utilizando document.getElementById("rpta").innerHTML. El contenido se establece como el![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.013.png) mensaje "El texto invertido es " seguido del valor almacenado en la variable aux, que representa el texto invertido.

\- Demostración:



|![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.001.png)|**UNIVERSIDAD NACIONAL DE SAN AGUSTIN FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMA**|![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.002.png)|
| - | :-: | - |
|**Formato:** Guía de Práctica de Laboratorio / Talleres / Centros de Simulación|
|**Aprobación: 2022/03/01**|**Código: GUIA-PRLE-001**|**Página:** 4|

![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.014.jpeg)

**Ejercicio 3:** Escribir una página que muestre cuántos días faltan para el día de Arequipa!![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.015.png)

- Se utiliza la función window.onload para asegurarse de que el script se ejecute una vez que la página se haya cargado completamente.
- Se crea un objeto Date almacenado en la variable hoy que representa la fecha actual.![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.016.jpeg)
- Se crea otro objeto Date almacenando en la var diaArequipa que representa la fecha del Día de Arequipa. En este caso, se asume que el Día de Arequipa es el 15 de agosto. Se utiliza el año actual de "hoy" y se establece el mes como 7 (agosto) y el día como 15.![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.017.jpeg)
- Se verifica si la fecha actual es posterior al Día de Arequipa del año actual. Si es así, se suma un año![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.018.jpeg)![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.019.jpeg) al objeto diaArequipa para asegurarse de que se esté calculando la diferencia correcta para el próximo Día de Arequipa.
- Se calcula la diferencia en milisegundos entre la fecha del Día de Arequipa y la fecha actual, utilizando la función getTime(), que devuelve el número de milisegundos.
- La diferencia en milisegundos se divide entre el número de milisegundos en un día (1000 \* 3600

\* 24) para obtener el número de días restantes.




|![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.001.png)|**UNIVERSIDAD NACIONAL DE SAN AGUSTIN FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMA**|![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.002.png)|
| - | :-: | - |
|**Formato:** Guía de Práctica de Laboratorio / Talleres / Centros de Simulación|
|**Aprobación: 2022/03/01**|**Código: GUIA-PRLE-001**|**Página:** 5|



- Se utiliza Math.ceil() para redondear hacia arriba el resultado, asegurándose de que el número de días restantes se muestre como un número entero.![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.020.png)![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.021.jpeg)![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.022.jpeg)![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.023.jpeg)
- Finalmente, se actualiza el contenido de un elemento HTML con el id "diasRestantes" utilizando document.getElementById("diasRestantes").innerHTML. El contenido se establece como el número de días restantes hasta el próximo Día de Arequipa.
- Demostración:

![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.024.jpeg)

**Ejercicio 4:** Escribir una página que reciba la URL de la sesión de google meet de hoy y devuelva el código de la sesión sin guiones separados

- La función obtenerCodigoSesion() se llama cuando se activa algún evento como hacer click en un botón) y se encarga de obtener el código de sesión a partir de una URL ingresada en un campo de entrada (urlInput). Se obtiene el valor de la URL ingresada utilizando document.getElementById("urlInput").value y lo almacena en la variable url.
- Se llama a la función obtenerCodigoDesdeURL(url) pasando la URL como argumento para obtener el código de sesión.![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.025.jpeg)



|![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.001.png)|**UNIVERSIDAD NACIONAL DE SAN AGUSTIN FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMA**|![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.002.png)|
| - | :-: | - |
|**Formato:** Guía de Práctica de Laboratorio / Talleres / Centros de Simulación|
|**Aprobación: 2022/03/01**|**Código: GUIA-PRLE-001**|**Página:** 6|

- Se actualiza el contenido de un elemento HTML con el id "codigoSesion" utilizando document.getElementById("codigoSesion").innerHTML.![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.026.png)![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.027.jpeg) El contenido se establece como el código![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.028.jpeg) de sesión obtenido, pero sin los guiones ("-") separados. Esto se logra utilizando el método replace() con una expresión regular (/-/g) para reemplazar todos los guiones por una cadena vacía.![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.029.jpeg)
- La función obtenerCodigoDesdeURL(url) recibe una URL como parámetro y busca un código de![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.030.jpeg) sesión en dicha URL utilizando una expresión regular. Se define un patrón de expresión regular (/\/([a-zA-Z0-9\_-]{10,})[#/]?/) para buscar un código de sesión en la URL.
- Utilizamos el método match() de la cadena de la URL con el patrón definido para buscar una coincidencia. El resultado se almacena en la variable resultado.![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.031.jpeg)
- Se verificará si se encontró un código de sesión válido en la URL mediante la condición resultado && resultado.length > 1. Si se cumple, devuelve el código de sesión encontrado (resultado[1]), de lo contrario, se es que no se encuentra un código de sesión válido, devuelve una cadena vacía.

\- Demostración:



|![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.001.png)|**UNIVERSIDAD NACIONAL DE SAN AGUSTIN FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMA**|![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.002.png)|
| - | :-: | - |
|**Formato:** Guía de Práctica de Laboratorio / Talleres / Centros de Simulación|
|**Aprobación: 2022/03/01**|**Código: GUIA-PRLE-001**|**Página:** 7|

![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.032.jpeg)

**Ejercicio 5:** Escribir una página que permita calcular la suma de todos los valores de una tabla de valores![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.033.png) dinámica. La idea es crear una página web con un formulario que te permita decir cuántos valores tendrás la tabla, luego, al enviar el formulario la tabla se debe crear dinámicamente, junto con otro botón de enviado para calcular la suma.

- La función createTable() se activa al enviar un formulario y crea una tabla dinámicamente. La cantidad de filas en la tabla se basa en el número ingresado en un campo de entrada con el id "num-values". Cada fila contiene una celda con un campo de entrada numérico. La tabla resultante se inserta en un contenedor con el id "table-container".

![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.034.jpeg)

- En la función calculateSum() se activa al hacer click en un botón con el id "sum-button" y calcula la suma de los valores ingresados en los campos de entrada numéricos de la tabla. El resultado se muestra en un elemento HTML con el id "result".


|![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.001.png)|**UNIVERSIDAD NACIONAL DE SAN AGUSTIN FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMA**|![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.002.png)|
| - | :-: | - |
|**Formato:** Guía de Práctica de Laboratorio / Talleres / Centros de Simulación|
|**Aprobación: 2022/03/01**|**Código: GUIA-PRLE-001**|**Página:** 8|



|![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.035.jpeg)|
| - |
|- Se agrega un event listener al formulario con el id "value-form". Cuando se envía el formulario,|
|se evita el comportamiento predeterminado (recargar la página) y se llama a la función|
|<p>createTable().</p><p>![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.036.png)</p>|
|- Se agrega un event listener al botón con el id "sum-button". Cuando se hace clic en el botón, se|
|llama a la función calculateSum().|
|![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.037.png)|
|<p>- Demostración:</p><p>![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.038.jpeg)</p>|
|**II. SOLUCIÓN DEL CUESTIONARIO**|

|![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.001.png)|**UNIVERSIDAD NACIONAL DE SAN AGUSTIN FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMA**|![](Aspose.Words.82f77ea7-4715-4ece-97de-38f66d9d8a4e.002.png)|
| - | :-: | - |
|**Formato:** Guía de Práctica de Laboratorio / Talleres / Centros de Simulación|
|**Aprobación: 2022/03/01**|**Código: GUIA-PRLE-001**|**Página:** 9|



||
| :- |
|<p>**III. CONCLUSIONES**</p><p>- En este laboratorio, pudimos realizar nuestras scripts en JS, implementarlas en nuestros html y haciendo más dinámico nuestro trabajo, además de haber realizado nuevamente el trabajo en git.</p>|



|**RETROALIMENTACIÓN GENERAL**|
| - |
||


|**REFERENCIAS Y BIBLIOGRAFÍA**|
| - |
|*Tutoría Javascript. <https://www.w3schools.com/javascript/default.asp> , 2021. Acceso: 02-09-2021.*|
|*Loiane Groner. Aprendizaje de estructuras de datos y algoritmos de JavaScript: escritura compleja y*|
|*poderosa*|
|*Validador HTML - [https://validator.w3.org/*](https://validator.w3.org/)*|
|*Validador CSS - [https://jigsaw.w3.org/css-validator/*](https://jigsaw.w3.org/css-validator/)*|
||

