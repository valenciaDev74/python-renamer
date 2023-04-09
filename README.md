Renombrar archivos en una carpeta
Este programa en Python permite renombrar todos los archivos que se encuentran en una carpeta, eliminando una serie de palabras específicas del nombre de los archivos.

# Funcionamiento
El programa solicita al usuario la ruta de la carpeta en la que se encuentran los archivos a renombrar, así como las palabras que se deben eliminar del nombre de los archivos. Las palabras a eliminar se ingresan entre comillas dobles y se separan por espacios.

# Uso
Para utilizar el programa, se debe ejecutar el archivo Python renamer.py en un entorno de Python. El programa solicitará la ruta de la carpeta y las palabras a eliminar. Por ejemplo:

Ingrese la ruta de la carpeta: /Users/usuario/Documentos/archivos_a_renombrar
Ingrese las palabras a eliminar entre comillas dobles y separadas por un espacio: "borrar" "temporal"
En este ejemplo, el programa buscará todos los archivos en la carpeta /Users/usuario/Documentos/archivos_a_renombrar y eliminará las palabras "borrar" y "temporal" de los nombres de los archivos.

# Limitaciones
Este programa tiene algunas limitaciones importantes:

El programa no tiene en cuenta la extensión de los archivos, por lo que se pueden renombrar archivos que no deberían ser renombrados.
Si dos o más archivos tienen el mismo nombre y se eliminan las mismas palabras del nombre de los archivos, los archivos pueden tener el mismo nombre después de la ejecución del programa, lo que puede causar conflictos.
El programa no tiene en cuenta la ubicación de las palabras en el nombre de los archivos. Por ejemplo, si se eliminan las palabras "temporal" y "archivo", el archivo "archivo_temporal.txt" se renombraría como "_t.txt", lo que probablemente no sería lo esperado.
Estas limitaciones deben tenerse en cuenta al utilizar el programa y se deben tomar las precauciones necesarias para evitar problemas.