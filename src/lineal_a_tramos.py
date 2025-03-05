import numpy as np
import matplotlib.pyplot as plt

def plot_lineal_a_tramos():
    # Definición de la función lineal a tramos
    def piecewise_function(x):
        return np.piecewise(x, [x < -1, (x >= -1) & (x <= 1), x > 1],
                            [-1, lambda x: x, 1])
    
    # Definición de la derivada de la función lineal a tramos
    def piecewise_derivative(x):
        return np.piecewise(x, [x < -1, (x > -1) & (x < 1), x > 1],
                            [0, 1, 0])
    
    # Genera 600 puntos equidistantes en el rango de -3 a 3
    x = np.linspace(-3, 3, 600)
    y = piecewise_function(x)    # Evalúa la función en los puntos de x
    dy = piecewise_derivative(x) # Evalúa la derivada en los puntos de x
    
    # Configuración de la gráfica
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label='Función a tramos')
    plt.plot(x, dy, label='Derivada', linestyle='--')
    plt.axhline(0, linewidth=0.5)  # Eje x
    plt.axvline(0, linewidth=0.5)  # Eje y
    plt.xlabel('x')
    plt.ylabel('Valor')
    plt.title('Función Lineal a Tramos y su Derivada')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == '__main__':
    plot_lineal_a_tramos()
