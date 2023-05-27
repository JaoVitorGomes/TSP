import numpy as np
import pyswarms as ps

# Ler o arquivo de instância
file_path = "berlin52.tsp"
with open(file_path, "r") as file:
    lines = file.readlines()

# Obter as coordenadas das cidades
coord_section_start = lines.index("NODE_COORD_SECTION\n") + 1
coord_section_end = lines.index("EOF\n")
coords = []
for line in lines[coord_section_start:coord_section_end]:
    city, x, y = line.strip().split()
    coords.append((float(x), float(y)))

# Calcular a matriz de distâncias
num_cities = len(coords)
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        x1, y1 = coords[i]
        x2, y2 = coords[j]
        distance_matrix[i][j] = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Função de avaliação para o PSO
def evaluate_tsp(position):
    tour = np.argsort(position) + 1
    total_distance = 0
    num_cities = len(tour)

    for i in range(num_cities - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        total_distance += distance_matrix[city1 - 1][city2 - 1]

    return total_distance

# Definir os limites inferiores e superiores para as variáveis
lb = np.zeros(num_cities)
ub = np.ones(num_cities) * (num_cities - 1)

# Configurar e executar o PSO
options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}
optimizer = ps.single.GlobalBestPSO(n_particles=100, dimensions=num_cities, options=options)
best_cost, best_pos = optimizer.optimize(evaluate_tsp, iters=100)

# Imprimir a melhor solução encontrada
best_tour = np.argsort(best_pos) + 1
print("Melhor solução encontrada:")
print(best_tour)
print("Distância total:", best_cost)