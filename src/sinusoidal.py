import numpy as np
import matplotlib.pyplot as plt

def plot_sinusoidal():
    # Definir la función sinusoidal y su derivada
    def sinusoidal(x):
        return np.sin(x)
    
    def sinusoidal_derivative(x):
        return np.cos(x)
    
    # Definir el rango de valores para x: se muestran varios ciclos
    x = np.linspace(-2 * np.pi, 2 * np.pi, 400)
    
    # Calcular la función sinusoidal y su derivada
    y = sinusoidal(x)
    dy = sinusoidal_derivative(x)
    
    # Graficar la función sinusoidal y su derivada
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label='Función Sinusoidal: sin(x)', linewidth=2)
    plt.plot(x, dy, label="Derivada: cos(x)", linestyle='dashed', linewidth=2)
    
    # Líneas en los ejes para referencia
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.title("Función Sinusoidal y su Derivada")
    plt.xlabel("x")
    plt.ylabel("f(x) y f'(x)")
    plt.show()

if __name__ == '__main__':
    plot_sinusoidal()

