
# Parametros (Pasar a otro archivo txt) 
import numpy as np
import gnuplotlib as gp


#r_1 = 1.0
#r_2 = 0.8  
#k_1 = 500
#k_2 = 300  
#alpha = 0.5
#beta = 0.7
#h = 0.1
#time = 50

def cargar_parametros():
    params = {}
    with open('parametros.txt', 'r') as f:
        for line in f:
            key, value = line.strip().split(' = ')
            params[key] = float(value)
    return params

t=0
d = {}
p = {}

# Cargar parámetros
params = cargar_parametros()

# Asignar parámetros a variables
r_1 = params['r_1']
r_2 = params['r_2']
k_1 = params['k_1']
k_2 = params['k_2']
alpha = params['alpha']
beta = params['beta']
h = params['h']
time = params['time']
p_0 = params['p_0']
d_0 = params['d_0']

diferencial_p = lambda t: r_1 * p[round(t, 1)] *(1-((p[round(t, 1)] + alpha * d[round(t, 1)])/k_1))

diferencial_d = lambda t: r_2 * d[round(t, 1)] *(1-((d[round(t, 1)] + beta * p[round(t, 1)])/k_2))

def euler1(t, h, p):
  p[round(t + h, 1)] = p[round(t, 1)] + h * diferencial_p(t)
  
    
def euler2(t, h, d):
  d[round(t+h,1)] = d[round(t, 1)] + h * diferencial_d(t)


def main():
    t = 0
    cargar_parametros()
    while( t<=time):
      euler1(t,h,p)
      euler2(t,h,d)
      t+=h
    
    graficar_relacion()
    #graficar_Poblaciones()
    
    
  #charge params and run simulation

def graficar_Poblaciones():
    
    t_vals = np.array(sorted(d.keys()))
    d_vals = np.array([d[t] for t in t_vals])
    p_vals = np.array([p[t] for t in t_vals])

    # Graficar ambas funciones
    gp.plot((t_vals, d_vals, {'with': 'linespoints', 'legend': 'd(t)'}),
            (t_vals, p_vals, {'with': 'linespoints', 'legend': 'p(t)'}),
            title='Funciones d(t) y p(t)',
            xlabel='Tiempo',
            ylabel='Población')


def graficar_relacion():
    
    t_vals = np.array(sorted(d.keys()))
    d_vals = np.array([d[t] for t in t_vals])
    p_vals = np.array([p[t] for t in t_vals])

    # Graficar ambas funciones
    gp.plot((p_vals, d_vals, {'with': 'linespoints', 'legend': 'Relacion'}),
            title='Relacion plano p-d',
            xlabel='Conejos',
            ylabel='Ciervos')


if __name__ == "__main__":
  main()
