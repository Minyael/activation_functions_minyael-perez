import numpy as np
import matplotlib.pyplot as plt

def plot_identity():
    # Definir la función identidad y su derivada
    def identity(x):
        return x
    
    def identity_derivative(x):
        return np.ones_like(x)  # La derivada de f(x) = x es 1 para todo x
    
    # Definir el rango de valores para x
    x = np.linspace(-10, 10, 400)
    
    # Calcular la función identidad y su derivada
    y = identity(x)
    dy = identity_derivative(x)
    
    # Graficar la función identidad y su derivada
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label='Función Identidad: f(x) = x', linewidth=2)
    plt.plot(x, dy, label="Derivada: f'(x) = 1", linestyle='dashed', linewidth=2)
    
    # Líneas en los ejes para referencia
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.title("Función Identidad y su Derivada")
    plt.xlabel("x")
    plt.ylabel("f(x) y f'(x)")
    plt.show()

if __name__ == '__main__':
    plot_identity()