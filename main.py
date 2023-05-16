import numpy as np
from platypus import Problem, Algorithm, PSO, Real
import matplotlib.pyplot as plt

# algoritmo utilizado: PSO (particle swarm optimization)
# instancia < 50: calculo de função objetivo == 20000
# instancia > 50: calculo de função objetivo == 70000


def read_archive(x):
    return x;



def alternate_dimensions():
    global d_index
    d_index = (d_index + 1) % len(dims)
    return dims[d_index]


def test_fun(x):
    x = np.array(x).reshape(1, dims[d_index])
    i = functions_list[f_index]
    for xi in enumerate(x):
        f = functions.all_functions[i](x)
    return f




