import os

# obtener el nombre del archivo Python actual
current_file = os.path.basename(__file__)

# pedir la ruta de la carpeta por consola
folder_path = input("Ingrese la ruta de la carpeta: ")

# pedir las palabras a eliminar por consola
words_to_remove = input("Ingrese las palabras a eliminar: ").split()

# iterar sobre todos los archivos en la carpeta
for filename in os.listdir(folder_path):
    # crear la ruta completa del archivo
    filepath = os.path.join(folder_path, filename)
    # comprobar si el archivo es un archivo regular y no es el archivo Python actual
    if os.path.isfile(filepath) and filename != current_file:
        # quitar las palabras a eliminar del nombre del archivo
        new_filename = filename
        for word in words_to_remove:
            new_filename = new_filename.replace(word, "")
        # crear la nueva ruta completa del archivo
        new_filepath = os.path.join(folder_path, new_filename)
        # renombrar el archivo
        os.rename(filepath, new_filepath)