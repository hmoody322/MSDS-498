import numpy as np
from scipy.optimize import differential_evolution, NonlinearConstraint, Bounds

def objective_func(x, e, bp, bq):
    perc_qty_change = np.multiply(e,x)
    new_price = bp + np.multiply(bp,x)
    new_qty = bq + np.multiply(perc_qty_change,bq)
    revenue = np.dot(new_price, new_qty)
    return -revenue

def investment(x,bp,bq):
    new_price = bp + np.multiply(bp,x)
    lm = bp - new_price
    investment = np.dot(lm,bq)
    return investment

if __name__ == '__main__':

    #Sample Data
    e = np.array([-1.70, -1.75, -1.87, -2.00, -2.14, -2.30]) # Price Elasticities
    bp = np.array([4.1, 2.3, 3.2, 4.5, 10.1, 5.4]) # Item Current Prices
    bq = np.array([100,	120, 340, 50, 25, 150]) # Item Baseline Forecast

    num_items = e.size # number of items
    
    #Constraints
    max_price_change = 0.2 # Constraint: Maximum % Price Change allowed per Item
    budget = 300 # Constraint: Maximum Budget Available

    #Solver
    best = differential_evolution(
            objective_func,
            x0 = -max_price_change*np.ones(e.size)*0.5,
            args=(e,bp,bq),
            bounds=Bounds(lb=-max_price_change*np.ones(e.size), ub=np.zeros(e.size)),
            constraints=NonlinearConstraint(lambda x: investment(x,bp,bq), lb = 0, ub = budget),
            seed = 1234
    )

    # Print Results
    if best.success:
        new_price = bp + np.multiply(bp,best.x)
        perc_qty_change = np.multiply(e,best.x)
        new_qty = bq + np.multiply(perc_qty_change,bq)
        baseline_revenue = np.dot(bp,bq)
        baseline_qty=sum(bq)

        print(f"Optimal solution found")
        print(f"Baseline Revenue: ${round(baseline_revenue, 0)}, Optimize Revenue: ${-round(best.fun, 0)}, Revenue Increase: {round(((-best.fun/baseline_revenue)-1)*100,1)}%")
        print(f"Baseline Qty: {round(baseline_qty, 0)}, Optimize Qty: {round(sum(new_qty), 0)}, Qty Increase: {round(((sum(new_qty)/baseline_qty)-1)*100,1)}%")
        
        for item in range(0,len(best.x)):
            print(f"Optimal Item {item+1} Price Change: {round(best.x[item]*100,1)}% with New Selling Price: ${round(new_price[item],2)}")

        
    else: 
        print("No solution found to problem")