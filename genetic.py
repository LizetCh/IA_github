import random

def generate_population(size, gene_length): #generate starting population 
		population = []
		for _ in range(size):
				individual = [random.randint(0, 1) for _ in range(gene_length)]
				population.append(individual)
		return population
def evaluate_fitness(individual):
    # En este ejemplo, la aptitud será simplemente la suma de los genes
    # (maximizar la cantidad de unos)
    return sum(individual)

def select_parents(population, fitnesses):
    # Selección por torneo: elegir dos individuos al azar y quedarnos con el mejor
    tournament_size = 3
    selected = random.sample(list(zip(population, fitnesses)), tournament_size) #selects 3 ppl
    best_individual = max(selected, key=lambda x: x[1]) #chooses the most apt
    return best_individual[0]

def crossover(parent1, parent2):
    # Punto de cruce en un punto aleatorio
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(individual, mutation_rate):
    # Mutación: recorrer cada gen y mutarlo con una probabilidad igual a mutation_rate
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]  # Cambia de 1 a 0 o de 0 a 1

def genetic_algorithm(population_size, gene_length, generations, mutation_rate):
		population = generate_population(population_size, gene_length)
		for generation in range(generations):
				fitnesses = [evaluate_fitness(individual) for individual in population]
				new_population = []
				for _ in range(population_size // 2):
						parent1 = select_parents(population, fitnesses)
						parent2 = select_parents(population, fitnesses)
						child1, child2 = crossover(parent1, parent2)
						mutate(child1, mutation_rate)
						mutate(child2, mutation_rate)
						new_population.extend([child1, child2])
				population = new_population
				print(f"Generation {generation}: Best fitness = {max(fitnesses)}")
		best_individual = max(population, key=evaluate_fitness)
		return best_individual

# Example of a call to the genetic algorithm
best_solution = genetic_algorithm(population_size=10, gene_length=5, generations=20, mutation_rate=0.01)
print("Best solution found:", best_solution)