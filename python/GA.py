import numpy as np
import deap as dp
import tsplib95 as tsp

def ReadInput(file):
    problem = tsp.load('input/'+file)
    problem.get_graph()
    return problem

def GetDist(value,A,B):
    if value.type == 'ATSP': 
        return value.get_weight(A,B) 
    if value.type == 'TSP':
        return np.linalg.norm(np.array(value.node_coords[A]) - np.array(value.node_coords[B]))


inputFiles = {'berlin52.tsp','br17.atsp','ch130.tsp','ftv70.atsp'}
for i in inputFiles:
    problem = ReadInput(i)
    dist = GetDist(problem,1,2)
    print("distancia do ",i,": ",dist)
    


