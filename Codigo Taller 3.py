
import cv2
import numpy as np

# 1. Abrir la imagen en escala de grises
imagen = cv2.imread("imagen.jpg", cv2.IMREAD_GRAYSCALE)

# 2. Umbralización para eliminar ruido
# THRESH_BINARY_INV: convierte los valores oscuros en blancos
_, imagen_binarizada = cv2.threshold(
    imagen, 120, 255, cv2.THRESH_BINARY_INV
)

# 3. Crear elemento estructurante de 5x5
kernel = np.ones((5, 5), np.uint8)

# 4. Operación de APERTURA
# Erosión seguida de dilatación
imagen_apertura = cv2.morphologyEx(
    imagen_binarizada,
    cv2.MORPH_OPEN,
    kernel,
    iterations=1
)

# 5. Operación de CIERRE
# Dilatación seguida de erosión
imagen_cierre = cv2.morphologyEx(
    imagen_binarizada,
    cv2.MORPH_CLOSE,
    kernel,
    iterations=1
)

# 6. Mostrar las tres imágenes

cv2.imshow("Original Binarizada", imagen_binarizada)
cv2.imshow("Apertura - Erosion + Dilatacion", imagen_apertura)
cv2.imshow("Cierre - Dilatacion + Erosion", imagen_cierre)

# Esperar hasta presionar una tecla
cv2.waitKey(0)
cv2.destroyAllWindows()
