import cv2
import numpy as np

# 1. Cargar imagen
imagen = cv2.imread('formas.png')

# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# 2. Umbralización
# Objetos claros sobre fondo oscuro
_, binaria = cv2.threshold(gris, 127, 255, cv2.THRESH_BINARY)

# 3. Limpieza morfológica
kernel = np.ones((3, 3), np.uint8)

binaria = cv2.morphologyEx(
    binaria,
    cv2.MORPH_OPEN,
    kernel
)

# 4. Encontrar contornos
contornos, _ = cv2.findContours(
    binaria,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# Convertir imagen original a color
imagen_color = imagen.copy()

# Recorrer cada objeto encontrado
for cnt in contornos:

    # Calcular área
    area = cv2.contourArea(cnt)

    # Ignorar objetos muy pequeños
    if area > 500:

        # Calcular Bounding Box
        x, y, w, h = cv2.boundingRect(cnt)

        # Dibujar Bounding Box
        cv2.rectangle(
            imagen_color,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        # Calcular momentos
        M = cv2.moments(cnt)

        if M["m00"] != 0:

            # Calcular centroide
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])

            # Dibujar centroide
            cv2.circle(
                imagen_color,
                (cx, cy),
                5,
                (0, 0, 255),
                -1
            )

            # Clasificación según el área
            if area > 5000:
                texto = "OBJETO GRANDE"
            else:
                texto = "OBJETO PEQUENO"

            # Escribir información
            cv2.putText(
                imagen_color,
                texto,
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 0, 0),
                2
            )

            # Mostrar información en consola
            print("Objeto encontrado")
            print("Area:", area)
            print("Bounding Box: X =", x,
                  "Y =", y,
                  "W =", w,
                  "H =", h)
            print("Centroide: (", cx, ",", cy, ")")
            print("-------------------------")

# Mostrar resultado
cv2.imshow("Clasificador de formas", imagen_color)
cv2.waitKey(0)
cv2.destroyAllWindows()