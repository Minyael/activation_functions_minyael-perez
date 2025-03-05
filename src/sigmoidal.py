import numpy as np
import matplotlib.pyplot as plt

def plot_sigmoidal():
    # Definir la función sigmoidal y su derivada
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))
    
    def sigmoid_derivative(x):
        s = sigmoid(x)
        return s * (1 - s)
    
    # Rango de valores para x
    x = np.linspace(-10, 10, 400)
    
    # Calcular la función sigmoidal y su derivada
    y = sigmoid(x)
    dy = sigmoid_derivative(x)
    
    # Graficar la función sigmoidal y su derivada
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label='Función Sigmoidal: f(x)=1/(1+e^(-x))', linewidth=2)
    plt.plot(x, dy, label="Derivada: f'(x)=f(x)(1-f(x))", linestyle='dashed', linewidth=2)
    
    # Líneas en los ejes para referencia
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.title("Función Sigmoidal y su Derivada")
    plt.xlabel("x")
    plt.ylabel("f(x) y f'(x)")
    plt.show()

if __name__ == '__main__':
    plot_sigmoidal()
