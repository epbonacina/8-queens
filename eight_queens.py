import numpy as np
from numba import jit


def evaluate(individual: np.array):
    """
    Recebe um indivíduo (lista de inteiros) e retorna o número de ataques
    entre rainhas na configuração especificada pelo indivíduo.
    Por exemplo, no individuo [2,2,4,8,1,6,3,4], o número de ataques é 10.

    :param individual:list
    :return:int numero de ataques entre rainhas no individuo recebido
    """
    conflicts = 0
    for i in range(individual.shape[0]):
        for j in range(i+1, individual.shape[0]):
            if individual[i] == individual[j] or abs(i-j) == abs(individual[i] - individual[j]):
                conflicts += 1
    return conflicts


def tournament(participants: np.array):
    """
    Recebe uma lista com vários indivíduos e retorna o melhor deles, com relação
    ao numero de conflitos
    :param participants:list - lista de individuos
    :return:list melhor individuo da lista recebida
    """
    ordered_participants = np.array(sorted(participants, key=evaluate))
    return ordered_participants[0]


def crossover(parent1, parent2, index):
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
    raise NotImplementedError  # substituir pelo seu codigo


def mutate(individual, m):
    """
    Recebe um indivíduo e a probabilidade de mutação (m).
    Caso random() < m, sorteia uma posição aleatória do indivíduo e
    coloca nela um número aleatório entre 1 e 8 (inclusive).
    :param individual:list
    :param m:int - probabilidade de mutacao
    :return:list - individuo apos mutacao (ou intacto, caso a prob. de mutacao nao seja satisfeita)
    """
    raise NotImplementedError  # substituir pelo seu codigo


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
    population = np.random.randint(low = 1, high=9, size=(n, 8), dtype=np.dtype('u1'))

    for i in range(g):
        new_population = np.empty(shape=(0, 0), dtype=np.dtype('u1'))
        while len(new_population) < n:
            participants_idx = np.random.choice(population.shape[0], size=k, replace=False)
            p1 = tournament(population[participants_idx, :])
            participants_idx = np.random.choice(population.shape[0], size=k, replace=False)
            p2 = tournament(population[participants_idx, :])

            break

    print(population)
    print(f"Memory usage: {population.nbytes} bytes")
    
run_ga(10, 10000, 2, 0.3, 5)
