Automatizacion E2E

-Aplicante: 
    Galo Sanchez

-Ejercicio: 

    Ejercicio 1

    Prueba funcional automatizada (Prueba E2E) de un flujo de compra en la pagina https://www.demoblaze.com/ que incluye:

        a. Agregar dos productos al carrito
        b. Visualizar al carrito
        c. Completar el formulario de compra
        d. Finalizar la compra

-Tecnologias utilizadas:

    Para el ejercicio de automatizacion propuesto se ha utilizado el framework de Selenium Webdriver en leguage de programacion Python 
    puesto que son las tecnologias en las que poseo mayor conocimiento. Adicionalmente se han utilizado librerias de soporte como Unittest
    para el manejo y organizacion de casos de prueba y Test Suites para un mayor control de ejecucion y generacion de reportes en HTML con 
    HtmlTestRunner. (Otras librerias tambien se han implementado para el uso en los diferentes casos de prueba y las validaciones propuestas).

-Descripcion de Archivos:

    -Scripts de Python: 'e2e_qa_automation_example.py' que comprende 4 casos de prueba que van
    acorde a las acciones solicitadas en el ejercicio (Agregar dos productos al carrito, Visualizar al carrito, Completar el formulario de compra,
    Finalizar la compra). Adicionalmente se pueden encontrar funciones implementadas por efectos de las validaciones deseadas.
    
    -Scripts de Python: 'test_suite.py' conforma el Test suite a ser ejecutado estableciendo el orden de ejecucion asi como la generacion del reporte
    HTML con los resultados obtenidos.
    
    -Archivo de texto: 'readmy.txt' presente documento en el que se detallan los pasos de ejecucion de los scripts y detalles adicionales de la 
    solucion implementada.
    
    -Archivo de texto: 'conclusiones.txt' archivo que resume los hallazgos y resultados obtenidos del ejercicio propuesto.
    
    -Directorio: Una carpeta con el nombre Reports donde se almacenaran los reportes HTML generados de cada iteracion ejecutada.

-Pasos de ejecucion:

    -Ejecutar el script 'test_suite.py'
    -Se lo puede hacer directamente desde el terminal 'python3 test_suite.py'
    -El reporte HTML se lo puede encontrar en la carpeta 'Reports' 

-Notas adicionales:

    Se han omitido las tildes en el presente documento para evitar caracteres no deseados en caso de abrir el documento en un dispositivo con un lenguaje 
    diferente al espanol.