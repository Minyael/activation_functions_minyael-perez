import numpy as np
import matplotlib.pyplot as plt

def plot_relu():
    # Definir la función ReLU y su derivada
    def relu(x):
        return np.maximum(0, x)
    
    def relu_derivative(x):
        # Derivada de ReLU: 0 para x < 0, 1 para x > 0.
        # Se asigna 0 en x = 0 para efectos de graficación.
        return np.where(x > 0, 1, 0)
    
    # Rango de valores para x
    x = np.linspace(-10, 10, 400)
    
    # Calcular la función ReLU y su derivada
    y = relu(x)
    dy = relu_derivative(x)
    
    # Graficar la función ReLU y su derivada
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label='ReLU: f(x)=max(0,x)', linewidth=2)
    plt.plot(x, dy, label="Derivada: f'(x)", linestyle='dashed', linewidth=2)
    
    # Líneas en los ejes para referencia
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.title("Función ReLU y su Derivada")
    plt.xlabel("x")
    plt.ylabel("f(x) y f'(x)")
    plt.show()

if __name__ == '__main__':
    plot_relu()
