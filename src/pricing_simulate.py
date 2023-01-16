import numpy as np
import config as sp

def price_change(n):
    user_list=[]
    i=0
    while i<n:
        price = float(input("Enter item_" + str(i+1) + " % price reduction (Ex: 0.1 is 10% price reduction): "))
        user_list.append(price)
        i=i+1
    return np.array(user_list)

def simulate(x, e, bp, bq):
    perc_qty_change = np.multiply(e,x)
    new_price = bp + np.multiply(bp,x)
    new_qty = bq + np.multiply(perc_qty_change,bq)
    sim_revenue = np.dot(new_price, new_qty)
    baseline_revenue = np.dot(bp,bq)
    baseline_qty=sum(bq)
    sim_qty=sum(new_qty)
    lm = bp - new_price
    investment = np.dot(lm,bq)
    return [baseline_revenue, sim_revenue, baseline_qty, sim_qty, investment, new_price]

if __name__ == '__main__':

    num_items = sp.e.size # number of items
    user_price = price_change(num_items)

    baseline_revenue, sim_revenue, baseline_qty, new_qty, investment, new_price = simulate(-user_price,sp.e,sp.bp,sp.bq) 
    
    print(f"Simulation Results:")
    print(f"Baseline Revenue: ${round(baseline_revenue, 0)}, Simulated Revenue: ${round(sim_revenue, 0)}, Revenue Increase: {round(((sim_revenue/baseline_revenue)-1)*100,1)}%")
    print(f"Baseline Qty: {round(baseline_qty, 0)}, Simulated Qty: {round(new_qty, 0)}, Qty Increase: {round(((new_qty/baseline_qty)-1)*100,1)}%")
        
    for item in range(0,num_items):
        print(f"Scenario Item {item+1} Price Change: {round(-user_price[item]*100,1)}% with New Selling Price: ${round(new_price[item],2)}")
        