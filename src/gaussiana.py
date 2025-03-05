import numpy as np
import matplotlib.pyplot as plt

def plot_gaussian():
    # Definir la función gaussiana y su derivada
    def gaussian(x):
        return np.exp(-x**2)
    
    def gaussian_derivative(x):
        return -2 * x * np.exp(-x**2)
    
    # Rango de valores para x (recomendado centrado en 0)
    x = np.linspace(-3, 3, 400)
    
    # Calcular la función gaussiana y su derivada
    y = gaussian(x)
    dy = gaussian_derivative(x)
    
    # Graficar la función gaussiana y su derivada
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label='Función Gaussiana: $e^{-x^2}$', linewidth=2)
    plt.plot(x, dy, label="Derivada: $-2x e^{-x^2}$", linestyle='dashed', linewidth=2)
    
    # Añadir líneas en los ejes para referencia
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.title("Función Gaussiana y su Derivada")
    plt.xlabel("x")
    plt.ylabel("f(x) y f'(x)")
    plt.show()

if __name__ == '__main__':
    plot_gaussian()