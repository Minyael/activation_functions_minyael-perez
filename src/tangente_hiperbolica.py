import numpy as np
import matplotlib.pyplot as plt

def plot_tanh():
    # Definir la función tangente hiperbólica y su derivada
    def tanh(x):
        return np.tanh(x)
    
    def tanh_derivative(x):
        return 1 - np.tanh(x)**2
    
    # Definir el rango de valores para x
    x = np.linspace(-5, 5, 400)
    
    # Calcular la función tangente hiperbólica y su derivada
    y = tanh(x)
    dy = tanh_derivative(x)
    
    # Graficar la función tangente hiperbólica y su derivada
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label='Tangente Hiperbólica: tanh(x)', linewidth=2)
    plt.plot(x, dy, label="Derivada: 1 - tanh²(x)", linestyle='dashed', linewidth=2)
    
    # Líneas en los ejes para referencia
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.title("Función Tangente Hiperbólica y su Derivada")
    plt.xlabel("x")
    plt.ylabel("f(x) y f'(x)")
    plt.show()

if __name__ == '__main__':
    plot_tanh()
