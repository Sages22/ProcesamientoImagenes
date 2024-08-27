import os
import cv2
#Codigo para obtener la dimension de imagenes en una carpeta y su posterior guardado de estas.
# Cargar la carpeta
carpeta_origen= 'C:\\Users\\santi\\OneDrive\\Documentos\\Formacion\\Tesis\\Imagenes_no_Procesadas\\Paredes_Sanas'

# Abrir archivo o crearlo txt
f=open('C:\\Users\\santi\\OneDrive\\Documentos\\Formacion\\Tesis\\Imagenes_no_Procesadas\\ListaResolucionSanas.txt', 'w', encoding = 'utf-8')
for nombre_archivo in os.listdir(carpeta_origen):
    ruta_archivo = os.path.join(carpeta_origen, nombre_archivo)
    # Verificar si es un archivo de imagen
    if os.path.isfile(ruta_archivo) and nombre_archivo.lower().endswith(('.png', '.jpg', '.jpeg')):
        # Cargar la imagen
        imagen = cv2.imread(ruta_archivo)
        # Obtener las dimensiones de la imagen
        alto, ancho, canales = imagen.shape
        #Guardarlas en un documento txt para su posterior análisis
        f.write("Nombre del archivo || Ancho || Alto \n")
        f.write(f"{nombre_archivo} || {ancho} || {alto}\n")
        #Imprimir los resultados
        print(f"Nombre del archivo: {nombre_archivo}")
        print(f"Ancho: {ancho} píxeles")
        print(f"Alto: {alto} píxeles")



