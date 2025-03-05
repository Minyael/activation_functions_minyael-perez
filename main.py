from src.escalon import plot_step_function
from src.gaussiana import plot_gaussian
from src.identidad import plot_identity
from src.lineal_a_tramos import plot_lineal_a_tramos
from src.relu import plot_relu
from src.sigmoidal import plot_sigmoidal
from src.sinusoidal import plot_sinusoidal
from src.tangente_hiperbolica import plot_tanh

if __name__ == "__main__":
    print("Mostrando gráfico de la función escalón...")
    plot_step_function()
    
    print("Mostrando gráfico de la función gaussiana...")
    plot_gaussian()
    
    print("Mostrando gráfico de la función identidad...")
    plot_identity()
    
    print("Mostrando gráfico de la función lineal a tramos...")
    plot_lineal_a_tramos()
    
    print("Mostrando gráfico de la función ReLU...")
    plot_relu()
    
    print("Mostrando gráfico de la función sigmoidal...")
    plot_sigmoidal()
    
    print("Mostrando gráfico de la función sinusoidal...")
    plot_sinusoidal()
    
    print("Mostrando gráfico de la función tangente hiperbólica...")
    plot_tanh()
