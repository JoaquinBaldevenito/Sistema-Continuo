import numpy as np
import gnuplotlib as gp

# Función para cargar parámetros desde un archivo de texto
def cargar_parametros():
    params = {}
    with open('parametros.txt', 'r') as f:
        for line in f:
            key, value = line.strip().split(' = ')
            params[key] = float(value)
    return params

# Implementación de un paso del método de Euler
def euler(t, h, f,df):
  f[round(t + h, 1)] = f[round(t, 1)] + h * df(t)

# Ejecuta el método de Euler hasta alcanzar el tiempo final
def metodo_Euler(t,h,p,d,time,diferencial_p,diferencial_d):
  while( t<=time):
    euler(t,h,p,diferencial_p)
    euler(t,h,d,diferencial_d)
    t+=h

# Implementación de un paso del método trapezoidal
def trapezoidal(t, h, f,g,df,dg):
  euler(t,h,f,df)
  euler(t,h,g,dg)
  f[round(t + h, 1)] = f[round(t, 1)] + h * 0.5 * ( df(round(t + h,1)) + df(round(t,1)))

# Ejecuta el método trapezoidal hasta alcanzar el tiempo final
def metodo_Trapezoidal(t,h,p,d,time,diferencial_p,diferencial_d):
  while(t<= time):
    trapezoidal(t,h,p,d,diferencial_p,diferencial_d)
    trapezoidal(t,h,d,p,diferencial_d,diferencial_p)
    t+=h

# Grafica las poblaciones d(t) y p(t) en función del tiempo
def graficar_Poblaciones(d,p):
    t_vals = np.array(sorted(d.keys()))
    d_vals = np.array([d[t] for t in t_vals])
    p_vals = np.array([p[t] for t in t_vals])

    # Graficar ambas funciones
    gp.plot((t_vals, d_vals, {'with': 'linespoints', 'legend': 'd(t)'}),
            (t_vals, p_vals, {'with': 'linespoints', 'legend': 'p(t)'}),
            title='Funciones d(t) y p(t)',
            xlabel='Tiempo',
            ylabel='Población')

# Grafica la relación entre p(t) y d(t) en el plano fase
def graficar_relacion(d,p):
    
    t_vals = np.array(sorted(d.keys()))
    d_vals = np.array([d[t] for t in t_vals])
    p_vals = np.array([p[t] for t in t_vals])

    # Graficar ambas funciones
    gp.plot((p_vals, d_vals, {'with': 'linespoints', 'legend': 'Relacion'}),
            title='Relacion plano p-d',
            xlabel='Conejos',
            ylabel='Ciervos')

# Función principal del programa
def main():
  t=0
  d = {} # Poblacion ciervos
  p = {} # Poblacion conejos

  params = cargar_parametros()
  r_1 = params['r_1']
  r_2 = params['r_2']
  k_1 = params['k_1']
  k_2 = params['k_2']
  alpha = params['alpha']
  beta = params['beta']
  h = params['h']
  time = params['time']
  p[0] = params['p_0']
  d[0] = params['d_0']
  grafico = params['grafico']
  metodo = params['metodo']
  
  # Derivada de p(t) según modelo logístico con interacción
  diferencial_p = lambda t: r_1 * p[round(t, 1)] *(1-((p[round(t, 1)] + alpha * d[round(t, 1)])/k_1))

  # Derivada de d(t) según modelo logístico con interacción
  diferencial_d = lambda t: r_2 * d[round(t, 1)] *(1-((d[round(t, 1)] + beta * p[round(t, 1)])/k_2))

  if metodo == 1:
    metodo_Euler(t,h,p,d,time,diferencial_p,diferencial_d)
  else:
    metodo_Trapezoidal(t,h,p,d,time,diferencial_p,diferencial_d)

  if grafico == 1:
    graficar_Poblaciones(d,p)
  else:
    graficar_relacion(d,p)

# Punto de entrada del script
if __name__ == "__main__":
  main()
