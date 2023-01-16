import numpy as np    

#Sample Data
e = np.array([-1.70, -1.75, -1.87, -2.00, -2.14, -2.30]) # Price Elasticities
bp = np.array([4.1, 2.3, 3.2, 4.5, 10.1, 5.4]) # Item Current Prices
bq = np.array([100,	120, 340, 50, 25, 150]) # Item Baseline Forecast

#Constraints
price_change = 0.2 # Constraint: Maximum % Price Change allowed per Item
budget = 300 # Constraint: Maximum Budget Available