import numpy as np

# 1. Matriz de imagen (I)
imagen = np.array([
    [100, 100, 100],
    [100, 200, 100],
    [100, 100, 100]
])

# 2. Kernel (K) de Realce
kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

# 3. Producto Hadamard: elemento por elemento
resultado = imagen * kernel

# 4. Sumar todos los valores
pixel_central = np.sum(resultado)

# 5. Mostrar resultados
print("Resultado del producto Hadamard:")
print(resultado)

print("\nValor del píxel central:", pixel_central)
