from matplotlib import pyplot as plt

from eight_queens import run_ga, evaluate

POPULATION_SIZE = 1000
GENERATIONS = 20
ELITE_SIZE = 5
TOURNAMENT_SIZE = 5
MUTATION_PROB = 0.5

avg_fitnesses, worst_fitnesses, best_fitnesses = run_ga(
        GENERATIONS, POPULATION_SIZE, TOURNAMENT_SIZE, MUTATION_PROB, ELITE_SIZE
)
iterations = range(1, GENERATIONS + 1)

plt.title("Fitness score per generations")
plt.ylabel("Fitness score")
plt.xlabel("Generations")
plt.plot(iterations, best_fitnesses, label="Max fitness")
plt.plot(iterations, worst_fitnesses, label="Min fitness")
plt.plot(iterations, avg_fitnesses, label="Average fitness")
plt.axhline(y=0, linestyle='--')

plt.legend()
plt.show()


