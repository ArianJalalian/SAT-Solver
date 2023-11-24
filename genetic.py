import numpy as np
import random

from initialization import initial_cnf   
from cnf_functions import cnf_eval

def reproduce(x, y): 
    """
    do the cross over with a probability of 70 %
    """ 
    if random.random() < 0.3:
        return x

    m = len(x)
    cross_point = random.randint(0, m - 1)  
    
    if cross_point < (m - 1) / 2 : 
        cross_point = m - 1 - cross_point 
    
    child = np.array(x[0:cross_point])  
    child = np.append(child, y[cross_point:]) 
    return child

def selection(cnf, population):
    """
    selects the best 2 individuals of the given population
    """
    individual_fit = {}  

    size = len(population)
    for index in range(size):
        individual_fit[index] = cnf_eval(cnf, population[index])[1] 

    sorted_population = sorted(individual_fit) 
    return population[sorted_population[size - 1]], population[sorted_population[size - 2]]

def random_population(size, m): 
    """
    generate a random population of individuals 
    """
    population = []
    for i in range(size): 
        individual = []
        for j in range(m):
            individual.append(random.sample([-1, 1], 1)[0])
        
        population.append(individual) 

    return np.array(population) 

def mutate(individual): 
    """
    flip a single variable value with probability of 30 %
    """
    if random.random() > 0.3:
        return
    
    index = random.randint(0, len(individual) - 1)
    individual[index] *= -1 


def genetic_algorithm(cnf, m): 
    max = 0
    population = random_population(10, m)
    while(True):
        
        x, y = selection(cnf, population)
        child = reproduce(x, y) 
        mutate(child) 

        evaluation = cnf_eval(cnf, child)

        if evaluation[0]:
            return child
        

        if evaluation[1] > max:
            max = evaluation[1]  
            max_individual = child 

        print(evaluation[1])

        if (len(population) > 200):
            print("max TRUE clauses count is : ", max) 
            print("solution : ", max_individual)
            return max_individual

        child.reshape(1, m) 
        population = np.vstack((population, child)) 



def run():
    cnf, (m, _)= initial_cnf()
    genetic_algorithm(cnf, m)






