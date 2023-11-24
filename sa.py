import numpy as np 
import random 
import math
  
from initialization import initial_cnf   
from cnf_functions import cnf_eval

def schedule(t, alpha): 
    """
    manipulate the tempature in a linear manner
    """
    return t - alpha

def child_generator(parent): 
    index = random.randint(0, len(parent) - 1) 
    parent[index] *= -1 
    return parent  

 
def simulated_anealing(root, cnf): 
    t = 400 
    current = root 
    alpha = 2 

    while t > alpha:  
        
        current_evaluation = cnf_eval(cnf, current)
        if current_evaluation[0]:
            return current
         
        t = schedule(t, alpha)  

        child = child_generator(root) 
        child_evaluation = cnf_eval(cnf, child)
        delta_e = child_evaluation[1] - current_evaluation[1] 

        if delta_e > 0 or random.random() < math.exp((-1 * abs(delta_e)) / t): 
            print(child_evaluation[1]) 
            current = child 

    return current


def run():
    cnf, (m, n) = initial_cnf()
    root = np.ones(100)  
    solution = simulated_anealing(root, cnf)

    print("final solituon : ",solution)
    print("count : ", cnf_eval(cnf, solution)[1])
        



