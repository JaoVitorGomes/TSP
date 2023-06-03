import numpy as np
from platypus import Problem, Algorithm, Real
import matplotlib.pyplot as plt

# algoritmo utilizado: PSO (particle swarm optimization)
# instancia < 50: calculo de função objetivo == 20000
# instancia > 50: calculo de função objetivo == 70000
vetor = [];

def read_archive(x):
    ref_arquivo = open("berlin52.opt.tour","r")

    for linha in ref_arquivo:
        vetor.append(linha);

    ref_arquivo.close()
    return x;

def evaluate(solution):
    # Implemente aqui sua função de avaliação que calcula o valor do objetivo
    # baseado nos valores das variáveis de decisão do "solution"
    # Retorne uma lista contendo os valores dos objetivos
    return [0]


read_archive(1);

value_Instance =  read_archive(0);
max_avaliacoes = 0;
num_variaveis = 0;
num_objetivos = 0;
limite_inferior = 0;
limite_superior = 0;

if(value_Instance < 50):
    max_avaliacoes = 20000;
else:
    max_avaliacoes = 70000;

problem = Problem(num_variaveis, num_objetivos)
problem.types[:] = [Real(limite_inferior, limite_superior)] * num_variaveis
problem.function = evaluate
#algorithm = PSO(max_evaluations=max_avaliacoes)
#algorithm.run(problem)

