from numpy import random
from scipy.optimize import minimize

def geneate_starting_points(number_of_points):

    starting_points = []
    for point in range(number_of_points):
        starting_points.append((random.random(), random.random()))
        
    return starting_points

def objective_func(x):
    return (4*x[0]**2) - (4*x[0]**4) + (x[0]**(6/3) + (x[0]*x[1]) - (4*x[1]**2) + (4*x[1]**4))

def bounds():
    boundaries = [(0,1), (0,1)]
    return boundaries


if __name__ == '__main__':
    starting_points = geneate_starting_points(50)
    cons = [
        {'type': 'ineq', 'fun': lambda x: x[0] - 0.1}, 
        {'type': 'ineq', 'fun': lambda x: x[1] - 0.25} 
    ]
    first_iteration = True
    for point in starting_points:
        # for each point run the algorithim
        res = minimize(
            objective_func,
            [point[0], point[1]],
            method='SLSQP',
            bounds=bounds(),
            constraints=cons
        )
        # first iteration always gonna be the best so far
        if first_iteration:
            better_solution_found = False
            best = res
        else:
            # if we find a better solution, lets use it
            if res.success and res.fun < best.fun:
                better_solution_found = True
                best = res
                
    # print results if algorithim was successful
    if best.success:
        print(f"""Optimal solution found:
        -  Proportion of indoor seating to make available: {round(best.x[0], 3)}
        -  Proportion of outdoor seating to make available: {round(best.x[1], 3)}
        -  Risk index score: {round(best.fun, 3)}""")
    else: 
        print("No solution found to problem")