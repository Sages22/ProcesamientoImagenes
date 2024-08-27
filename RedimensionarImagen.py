import cv2
#Codigo para redimensionamiento de una imagen.
# Cargar la imagen desde su directorio
imagen = cv2.imread( 'C:\\Users\\santi\\OneDrive\\Documentos\\Formacion\\Tesis\\Imagenes_no_Procesadas\\Patologias_Estructurales\\19_comAl.jpeg')

# Definir las nuevas dimensiones
nueva_ancho = 1000
nueva_alto = 600

# Redimensionar la imagen
imagen_redimensionada = cv2.resize(imagen, (nueva_ancho, nueva_alto))

# Guardar la imagen redimensionada en la carpeta deseada
cv2.imwrite( 'C:\\Users\\santi\\Desktop\\ImgNueva.jpeg', imagen_redimensionada)