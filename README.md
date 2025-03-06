# README - Funciones de activación

---

## Descripción general

Este proyecto tiene como objetivo visualizar diferentes funciones de activación utilizadas en redes neuronales, junto con sus respectivas derivadas, haciendo uso de librerías como **NumPy** y **Matplotlib**. Cada función se encuentra implementada en un archivo independiente dentro del directorio `src/`, y el archivo `main.py` se encarga de ejecutar todas las visualizaciones en secuencia. Este proyecto fue realizado con Python 3.12.

---

## Requisitos Previos

Antes de ejecutar el código, asegúrate de tener instaladas las siguientes bibliotecas:

```bash
pip install numpy matplotlib
```

Opcionalmente, puedes usar un entorno virtual para aislar dependencias:

```bash
python -m venv env
source env/bin/activate  # En Linux/macOS
env\Scripts\activate  # En Windows
pip install -r requirements.txt
```

---

## Estructura del Proyecto

```
📂 activation_functions/
├── 📂 src/                      # Códigos fuente
│   ├── escalon.py              
│   ├── gaussiana.py
│   ├── identidad.py
│   ├── lineal_a_tramos.py
│   ├── relu.py
│   ├── sigmoidal.py
│   ├── sinusoidal.py
│   ├── tangente_hiperbolica.py
├── main.py                       # Script principal para ejecutar el modelo
├── requirements.txt              # Dependencias del proyecto
├── README.md                     # Documentación del proyecto
```

---

## Funciones implementadas

### Función escalón

Devuelve 1 si la entrada es mayor o igual a 0, y 0 en caso contrario. Su derivada es 0 en todos los puntos, excepto en la discontinuidad.

```python
def step_function(x):
    return np.where(x >= 0, 1, 0)
```

### Función gaussiana

Define una campana centrada en 0 con la ecuación \( e^{-x^2} \). Su derivada es \( -2x e^{-x^2} \).

```python
def gaussian(x):
    return np.exp(-x**2)
```

### Función identidad

Devuelve el mismo valor de entrada. Su derivada es siempre 1.

```python
def identity(x):
    return x
```

### Función lineal a tramos

Función definida por tramos, con valores constantes en los extremos y una sección lineal en el centro. Su derivada es 1 en la región lineal y 0 en los extremos.

```python
def piecewise_func(x):
    return np.piecewise(x, [x < -1, (x >= -1) & (x <= 1), x > 1], [-1, lambda x: x, 1])
```

### Función ReLu

Devuelve 0 si la entrada es negativa y \( x \) si es positiva. Su derivada es 0 para \( x < 0 \) y 1 para \( x > 0 \).

```python
def relu(x):
    return np.maximum(0, x)
```

### Función sigmoidal

Definida como \( \frac{1}{1 + e^{-x}} \), su derivada es \( f(x)(1 - f(x)) \).

```python
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
```

### Función sinusoidal

Función seno estándar \( \sin(x) \) con derivada \( \cos(x) \).

```python
def sinusoidal(x):
    return np.sin(x)
```

### Función tangente hiperbólica

Definida como \( \tanh(x) \), su derivada es \( 1 - \tanh^2(x) \).

```python
def tanh(x):
    return np.tanh(x)
```

---

## Ejecución

Para entrenar y evaluar el modelo, ejecuta en la terminal:

```bash
python main.py
```

---

## Conclusión

Este proyecto muestra cómo funcionan las distintas funciones de activación haciendo uso de liberías como matplotlib y numpy. Estas funciones son muy útiles para implementaciones en redes neuronales y otras aplicaciones.
