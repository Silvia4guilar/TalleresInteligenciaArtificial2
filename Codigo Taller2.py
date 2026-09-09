import cv2
import matplotlib.pyplot as plt

# 1. Cargar imagen RGB
imagen = cv2.imread("fotoelegida.jpg")

# 2. Separar los canales B, G y R
azul, verde, rojo = cv2.split(imagen)

# 3. Calcular el histograma de cada canal
hist_azul = cv2.calcHist([azul], [0], None, [256], [0, 256])
hist_verde = cv2.calcHist([verde], [0], None, [256], [0, 256])
hist_rojo = cv2.calcHist([rojo], [0], None, [256], [0, 256])

# 4. Graficar los tres histogramas superpuestos
plt.figure(figsize=(10, 5))

plt.plot(hist_azul, color='blue', label='Azul')
plt.plot(hist_verde, color='green', label='Verde')
plt.plot(hist_rojo, color='red', label='Rojo')

plt.title("Histogramas de los canales RGB")
plt.xlabel("Valor del píxel (0-255)")
plt.ylabel("Frecuencia (Cantidad de píxeles)")

plt.legend()
plt.grid()
plt.show()
