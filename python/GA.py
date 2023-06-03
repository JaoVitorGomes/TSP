import numpy as np
import tsplib95 as tsp
from deap import creator, base, tools
import random
import os

def ReadInput(file):
    problem = tsp.load('input/'+file)
    problem.get_graph()
    return problem

def GetDist(problem,A,B): 
    if problem.type == 'TSP':
        return np.linalg.norm(np.array(problem.node_coords[A]) - np.array(problem.node_coords[B]))
    if problem.type == 'ATSP': 
        return problem.get_weight(A,B)

def Evaluation(problem,tour):
    if(problem.type == "TSP"):
        sumValue = sum(GetDist(problem,tour[i], tour[i - 1]) for i in range(len(tour)))

    if(problem.type == "ATSP"):



input_dir = 'input/'
files = os.listdir(input_dir)

for filename in files:
    if not (filename.endswith('.tsp') or filename.endswith('.atsp')):
        continue

    problem = ReadInput(filename)
    dist = GetDist(problem,1,2)
    print("distancia do ",filename,": ",dist)
    
    creator.create("FitnessMin",base.Fitness,weights=(-1.0))
    creator.create("Individual", list, fitness=creator.FitnessMin)
    
    toolbox = base.Toolbox()
    toolbox.register("indices", random.sample, range(0, problem.dimension), problem.dimension)
    toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    toolbox.register("evaluate", evaluation)
    toolbox.register("mate", tools.cxOrdered)
    toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
    toolbox.register("select", tools.selTournament, tournsize=3)

    pop = toolbox.population(n=100)
    gens = 20000 if problem.dimension < 50 else 70000
    hof = tools.HallOfFame(1)

    statistics = tools.Statistics(key=operator.attrgetter("fitness.values"))
    statistics.register('mean', np.mean)
    statistics.register('min', np.min)
    statistics.register('max', np.max)

    result, log = algorithms.eaSimple(pop, toolbox, cxpb=0.7, mutpb=0.05, ngen=gens, verbose=False, stats=statistics, halloffame=hof)

    best_individual = tools.selBest(result, k=1)[0]
    best_possible_values = {'berlin52.tsp': 7542, 'ch130.tsp': 6110, 'br17.atsp': 39, 'ftv70.atsp': 1950}
    print('Best tour found: ', evaluation(best_individual)[0])
    print('Best tour existent: ', best_possible_values[filename])
    print('Best tour: ', best_individual)
    print('Average fitness: ', np.mean(log.select('mean')))
    # print('Execution time: ', execution_time, 'seconds')
    print('Relative error: ',(evaluation(best_individual)[0] - best_possible_values[filename]) / best_possible_values[filename] * 100, '%')




