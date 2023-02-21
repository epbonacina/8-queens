import random

CROSSOVER_INDEX = 3
CROSSOVER_PROB = 0.5
INDIVIDUAL_SIZE = 8


def top_n(individuals, num):
    """
    Retorna os top num indivíduos de acordo com a função de avaliação. Se num for
    igual a 1, retorna apenas o indivíduo (sem estar contido em uma lista).

    :param individuals: list
    :param num: int
    :return: Union[list[list], list[int]] top n indivíduos
    """
    individuals = individuals.copy()
    individuals.sort(key=evaluate)
    return individuals[:num]


def evaluate(individual):
    """
    Recebe um indivíduo (lista de inteiros) e retorna o número de ataques
    entre rainhas na configuração especificada pelo indivíduo.
    Por exemplo, no individuo [2,2,4,8,1,6,3,4], o número de ataques é 10.

    :param individual:list
    :return:int numero de ataques entre rainhas no individuo recebido
    """
    conflicts = 0
    for i in range(len(individual)):
        for j in range(i+1, len(individual)):
            if individual[i] == individual[j] or abs(i-j) == abs(individual[i] - individual[j]):
                conflicts += 1
    return conflicts


def select(population, k):
    """
    Seleciona os 2 melhores indivíduos de uma fatia aleatória da população.

    :param population: list lista de indivíduos
    :param k: int número de participantes do torneio
    :return: tuple tupla com os 2 melhores indivíduos da fatia selecionada
    """
    participants = random.sample(population, k)
    p1 = tournament(participants)
    participants = random.sample(population, k)
    p2 = tournament(participants)
    return p1, p2


def tournament(participants):
    """
    Recebe uma lista com vários indivíduos e retorna o melhor deles, com relação
    ao numero de conflitos
    :param participants:list - lista de individuos
    :return:list melhor individuo da lista recebida
    """
    return top_n(participants, 1)[0]


def random_crossover(parent1, parent2, index):
    """
    Realiza o crossover de um ponto: recebe dois indivíduos e o ponto de
    cruzamento (indice) a partir do qual os genes serão trocados. Retorna os
    dois indivíduos com o material genético trocado.
    Por exemplo, a chamada: crossover([2,4,7,4,8,5,5,2], [3,2,7,5,2,4,1,1], 3)
    deve retornar [2,4,7,5,2,4,1,1], [3,2,7,4,8,5,5,2].
    A ordem dos dois indivíduos retornados não é importante
    (o retorno [3,2,7,4,8,5,5,2], [2,4,7,5,2,4,1,1] também está correto).
    :param parent1:list
    :param parent2:list
    :param index:int
    :return:list,list
    """
    if random.uniform(0, 1) < CROSSOVER_PROB:
        o1, o2 = crossover(parent1, parent2, index)
    else:
        o1, o2 = parent1, parent2
    return o1, o2


def crossover(parent1, parent2, index):
    o1 = parent1[:index] + parent2[index:]
    o2 = parent2[:index] + parent1[index:]
    return o1, o2


def mutate(individual, mutation_prob):
    """
    Recebe um indivíduo e a probabilidade de mutação (m).
    Caso random() < m, sorteia uma posição aleatória do indivíduo e
    coloca nela um número aleatório entre 1 e 8 (inclusive).
    :param individual:list
    :param m:int - probabilidade de mutacao
    :return:list - individuo apos mutacao (ou intacto, caso a prob. de mutacao nao seja satisfeita)
    """
    new_individual = individual.copy()
    if random.uniform(0, 1) < mutation_prob:
        for i in range(INDIVIDUAL_SIZE):
            if random.uniform(0, 1) < 1/INDIVIDUAL_SIZE:
                new_individual[i] = random.randint(1, INDIVIDUAL_SIZE)
    return new_individual


def run_ga(g, n, k, m, e):
    """
    Executa o algoritmo genético e retorna o indivíduo com o menor número de ataques entre rainhas
    :param g:int - numero de gerações
    :param n:int - numero de individuos
    :param k:int - numero de participantes do torneio
    :param m:float - probabilidade de mutação (entre 0 e 1, inclusive)
    :param e:int - número de indivíduos no elitismo
    :return:list - melhor individuo encontrado
    """
    population = [[random.randint(1, 8) for _ in range(INDIVIDUAL_SIZE)] for _ in range(n)]

    for i in range(g):
        new_population = top_n(population, e)
        new_population = list()
        while len(new_population) < n:
            p1, p2 = select(population, k)
            o1, o2 = random_crossover(p1, p2, CROSSOVER_INDEX)
            m1, m2 = mutate(o1, m), mutate(o2, m)
            new_population.append(m1)
            new_population.append(m2)
        population = new_population.copy()
        avg_fitness = sum([evaluate(individual) for individual in population])/len(population)
    return top_n(population, 1), top_n(population, len(population))[-1], avg_fitness