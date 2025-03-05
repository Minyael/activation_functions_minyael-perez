import numpy as np
import matplotlib.pyplot as plt

def plot_step_function():
    # Definir la función escalón y una aproximación de su derivada
    def step_function(x):
        """Función escalón (Heaviside): retorna 1 si x>=0, 0 si x<0."""
        return np.where(x >= 0, 1, 0)
    
    def step_derivative(x):
        """Derivada de la función escalón."""
        return np.zeros_like(x)
    
    # Definir el rango de valores para x
    x = np.linspace(-10, 10, 400)
    
    # Calcular la función escalón y su derivada
    y = step_function(x)
    dy = step_derivative(x)
    
    # Graficar la función escalón y su derivada
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label='Función Escalón', linewidth=2)
    plt.plot(x, dy, label="Derivada aproximada", linestyle='dashed', linewidth=2)
    
    # Detalles estéticos del gráfico
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.title("Función Escalón y su Derivada Aproximada")
    plt.xlabel("x")
    plt.ylabel("f(x) y f'(x)")
    plt.show()

if __name__ == '__main__':
    plot_step_function()