A simple 8-queens solver based on Genetic Algorithms.

## Required external packages

No external packages are needed.

## How to use

There are 2 main functions in this project. 
- `evaluate`: takes an individual (which is a list of 8 numbers between 1 and 8) and returns the number of thretens
between queens;
- `run_ga`: takes the parameters listed bellow and returns the best individual found.  
  Parameters:  
    - `g`: `int` -> number of generations;
    - `n`: `int` -> population size;
    - `k`: `int` -> tournament size;
    - `m`: `float` -> mutation probability;
    - `e`: `int` -> number of individuals in the elite group.

## Usage example

```python
  from eight_queens import run_ga, evaluate
  
  POPULATION_SIZE = 1000
  GENERATIONS = 25
  ELITE_SIZE = 5
  TOURNAMENT_SIZE = 5
  MUTATION_PROB = 0.5
  
  best_individual = run_ga(
    GENERATIONS, POPULATION_SIZE, TOURNAMENT_SIZE, MUTATION_PROB, ELITE_SIZE
  )
  fitness = evaluate(best_individual)
  
  print("{best_individual=} -> {fitness=}")
```

## Reasonable parameters

After some analysis sections, we found that the following parameters are capable of solving the game.

```python
POPULATION_SIZE = 1000
GENERATIONS = 25
ELITE_SIZE = 5
TOURNAMENT_SIZE = 5
MUTATION_PROB = 0.5
```

The following figure shows the effect of increasing the value of `GENERATIONS`

![Figure_1](https://user-images.githubusercontent.com/63553534/220207238-06203251-e10c-49d9-ab67-0f48b25c3212.png)

## Developers

- Enzo Pedro Bonacina [Turma B] 00313316;
- Thales Junqueira Albergaria Moraes Perez [Turma B] 00303035;
- Hiram Artnak Martins [Turma B] 00276484;
