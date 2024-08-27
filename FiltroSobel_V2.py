import cv2
import os
import numpy as np

#Codigo para aplicar filtro gaussiano, luego sobel y al final una dilatación para mejorar la deteccion de bordes

# Directorio de entrada (donde están las imágenes originales)
carpeta_origen = 'C:\\Users\\santi\\OneDrive\\Documentos\\Formacion\\Tesis\\Imagenes_no_Procesadas\\Patologias_Estructurales'
# Directorio de salida (donde se guardarán las imágenes procesadas)
carpeta_destino = 'C:\\Users\\santi\\OneDrive\\Documentos\\Formacion\\Tesis\\Imagenes_Procesadas\\Patologias_Estructurales'

# Crear la carpeta de destino si no existe
if not os.path.exists(carpeta_destino):
    os.makedirs(carpeta_destino)

# Iterar sobre cada archivo en la carpeta de origen
for nombre_archivo in os.listdir(carpeta_origen):
    # Ruta completa del archivo
    ruta_archivo = os.path.join(carpeta_origen, nombre_archivo)

    # Verificar si es un archivo de imagen
    if os.path.isfile(ruta_archivo) and nombre_archivo.lower().endswith(('.png', '.jpg', '.jpeg')):
        # Cargar la imagen en escala de grises
        imagen = cv2.imread(ruta_archivo, cv2.IMREAD_GRAYSCALE)

        imagen_suavizada = cv2.GaussianBlur(imagen, (3, 3), 5)

        # Aplicar el filtro Sobel en la dirección X y Y
        sobel_x = cv2.Sobel(imagen_suavizada, cv2.CV_64F, 1, 0, ksize=3)   #cv2.Sobel(imagen, cv2.CV_64F, x, y, tamaño del kernel
        sobel_y = cv2.Sobel(imagen_suavizada, cv2.CV_64F, 0, 1, ksize=3)   #3x3 datos más finos y sobel mas aburpto

        #Se hace el calculo de las magnitudes usando ambos ejes
        sobel_magnitud = cv2.magnitude(sobel_x, sobel_y)

        #Dilatacion de la imagen
        kernel = np.ones((3, 3), np.uint8)
        imagen_dilatada = cv2.dilate(sobel_magnitud, kernel, iterations=1)

        # Guardar la imagen procesada en la carpeta de destino
        ruta_destino = os.path.join(carpeta_destino, 'sobel_' + nombre_archivo)
        cv2.imwrite(ruta_destino, imagen_dilatada)

        print(f'Imagen procesada y guardada: {ruta_destino}')

print("Proceso completado.")