import cv2
import numpy as np

# Cargar imagen con ruido
imagen = cv2.imread("imagen_ruidosa.jpg")

# 1. Filtro de Media
blur_media = cv2.blur(imagen, (7, 7))

# 2. Filtro Gaussiano
blur_gauss = cv2.GaussianBlur(imagen, (7, 7), 0)

# 3. Filtro de Mediana
blur_mediana = cv2.medianBlur(imagen, 7)

# Mostrar resultados
cv2.imshow("Imagen Original con Ruido", imagen)
cv2.imshow("Filtro de Media", blur_media)
cv2.imshow("Filtro Gaussiano", blur_gauss)
cv2.imshow("Filtro de Mediana", blur_mediana)

cv2.waitKey(0)
cv2.destroyAllWindows()