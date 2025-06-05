# Parametros (Pasar a otro archivo txt) 
import numpy as np
import gnuplotlib as gp

def cargar_parametros():
    params = {}
    with open('parametros.txt', 'r') as f:
        for line in f:
            key, value = line.strip().split(' = ')
            params[key] = float(value)
    return params

def euler_p(t, h, p,diferencial_p):
  p[round(t + h, 1)] = p[round(t, 1)] + h * diferencial_p(t)
  
    
def euler_d(t, h, d,diferencial_d):
  d[round(t+h,1)] = d[round(t, 1)] + h * diferencial_d(t)

def metodo_Euler(t,h,p,d,time,diferencial_p,diferencial_d):
  while( t<=time):
        euler_p(t,h,p,diferencial_p)
        euler_d(t,h,d,diferencial_d)
        t+=h

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

def graficar_relacion(d,p):
    
    t_vals = np.array(sorted(d.keys()))
    d_vals = np.array([d[t] for t in t_vals])
    p_vals = np.array([p[t] for t in t_vals])

    # Graficar ambas funciones
    gp.plot((p_vals, d_vals, {'with': 'linespoints', 'legend': 'Relacion'}),
            title='Relacion plano p-d',
            xlabel='Conejos',
            ylabel='Ciervos')

def main():
  
  t=0
  d = {}
  p = {}

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
  
  diferencial_p = lambda t: r_1 * p[round(t, 1)] *(1-((p[round(t, 1)] + alpha * d[round(t, 1)])/k_1))

  diferencial_d = lambda t: r_2 * d[round(t, 1)] *(1-((d[round(t, 1)] + beta * p[round(t, 1)])/k_2))

  if metodo == 1:
    metodo_Euler(t,h,p,d,time,diferencial_p,diferencial_d)
  else:
    metodo_Backward_Euler()


  if grafico == 1:
    graficar_Poblaciones(d,p)
  else:
    graficar_relacion(d,p)
    
if __name__ == "__main__":
  main()
