import numpy as np
import matplotlib.pyplot as plt


def julia(c, max_iter):
    def func(z):
        n = 0
        while abs(z) <= 2 and n < max_iter:
            z = z * z + c
            n += 1
        return n

    return func


def generate_julia_set(width, height, x_min, x_max, y_min, y_max, c, max_iter, cmap):
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    julia_set = np.empty((width, height))

    julia_func = julia(c, max_iter)

    for i in range(width):
        for j in range(height):
            julia_set[i, j] = julia_func(complex(x[i], y[j]))

    plt.imshow(julia_set.T, extent=[x_min, x_max, y_min, y_max], cmap=cmap)
    plt.colorbar()
    plt.title(f"Conjunto de Julia para c = {c}")
    plt.show()


# Parámetros del fractal
width, height = 800, 800
x_min, x_max = -1.5, 1.5
y_min, y_max = -1.5, 1.5
c = complex(-0.7, 0.27015)
max_iter = 256

# Paletas de colores disponibles
# paletas = ["hot", "viridis", "plasma", "inferno", "magma", "cividis"]

# Generar fractal con diferentes paletas de colores
generate_julia_set(width, height, x_min, x_max, y_min, y_max, c, max_iter, "hot")
