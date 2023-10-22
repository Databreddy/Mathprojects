import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def generate_mandelbrot(width, height, xmin, xmax, ymin, ymax, max_iter):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    mandelbrot_set = np.zeros((width, height))
    for i in range(width):
        for j in range(height):
            mandelbrot_set[i, j] = mandelbrot(x[i] + 1j*y[j], max_iter)
    return mandelbrot_set

# Set the dimensions and parameters of the fractal
width, height = 1000, 1000
xmin, xmax = -2, 2
ymin, ymax = -2, 2
max_iter = 256

# Generate the Mandelbrot Set
mandelbrot_set = generate_mandelbrot(width, height, xmin, xmax, ymin, ymax, max_iter)

# Display the Mandelbrot Set
plt.figure(figsize=(10, 10))
plt.imshow(mandelbrot_set.T, extent=(xmin, xmax, ymin, ymax), cmap='hot', origin='lower')
plt.title('Mandelbrot Set')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.show()
