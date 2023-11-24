import numpy as np

def initial_cnf(): 
    """
    put cnf clauses in an 1D numpy array, cnf 2D numpy 
    array consist of multiple clauses
    """

    file = open("Input.cnf", "r") 
    lines = file.readlines()  

    m, n = int(lines[3].split()[2]), int(lines[3].split()[3])  
    lines = lines[4:] 

    cnf = []

    for line in lines:
        line = list(map(lambda s : int(s), line.split()[:3]))  
        bool_values = np.zeros(m)  

        for v in line:
            if v < 0: 
                bool_values[-v - 1] = -1 
            else: 
                bool_values[v - 1] = 1        
    

        cnf.append(bool_values) 
    
    return cnf, (m, n)   
    


