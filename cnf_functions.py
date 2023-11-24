def cnf_eval(cnf, individual): 
    """
    evalute given individual on the provided cnf
    returns if all clauses are satisfied and total number of 
    satisfied clauses
    """
    
    count = 0   
    for clause in cnf:
        if clause_eval(clause, individual) : 
            count += 1 

    return len(cnf) == count, count

def clause_eval(clause, individual):
    """
    check if provided individual staisfy given clause or not
    """
    
    result = clause * individual
    return 1 in result