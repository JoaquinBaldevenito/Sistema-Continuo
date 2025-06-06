---

# Simulación de Interacción de Poblaciones

Este proyecto implementa un modelo basado en ecuaciones diferenciales para simular la interacción entre dos especies usando el **método de Euler**. Los resultados se grafican con `gnuplotlib`.

## Requisitos

Antes de ejecutar el código, asegúrate de tener instalado Python 3 y las siguientes dependencias:

```bash
pip install numpy gnuplotlib
```

> ⚠️ `gnuplotlib` requiere que tengas instalado **Gnuplot** en tu sistema. En Debian/Ubuntu puedes instalarlo con:

```bash
sudo apt install gnuplot
```

## Estructura del Proyecto

* `main.py` – Código principal del modelo.
* `parametros.txt` – Archivo de texto con los parámetros de la simulación.

## Formato del archivo `parametros.txt`

Este archivo debe contener los siguientes parámetros, uno por línea, con el formato `clave = valor`:

```
r_1 = 1.0
r_2 = 0.8
k_1 = 500
k_2 = 300
alpha = 0.5
beta = 0.7
h = 0.1
time = 50
p_0 = 50
d_0 = 100
grafico = 1
metodo = 1
```

### Descripción de los parámetros

* `r_1`, `r_2`: Tasas de crecimiento de las especies.
* `k_1`, `k_2`: Capacidad de carga de cada especie.
* `alpha`, `beta`: Factores de competencia entre especies.
* `h`: Tamaño del paso para el método numérico.
* `time`: Tiempo total de simulación.
* `p_0`, `d_0`: Valores iniciales de población para cada especie.
* `grafico`: Tipo de gráfico a mostrar:

  * `1` → Poblaciones en función del tiempo.
  * `0` → Relación entre poblaciones (`p` vs `d`).
* `metodo`: Método numérico a utilizar:

  * `1` → Método de Euler (explícito).
  * `0` → Método de Backward-Euler.


> Puedes modificar estos valores para experimentar con distintos escenarios de simulación.

## Ejecución

Una vez configurado el entorno y creado el archivo `parametros.txt`, simplemente ejecuta el script:

```bash
python main.py
```

Esto simulará el comportamiento de las poblaciones a lo largo del tiempo y mostrará una gráfica de la relación entre ambas en el plano.

