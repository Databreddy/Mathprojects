from scipy.optimize import minimize

# Define the objective function to minimize
def objective_function(x1):
    return (x1+3)*(x1-1)*(x1+4)*(x1-1)*(x1-7)

# Initial guess (starting point for the optimization)
initial_guess = [20.0]

# Perform nonlinear optimization
result = minimize(objective_function, initial_guess, method='BFGS')

# Print the optimization result
print("Optimal solution:", result.x)
print("Optimal objective value:", result.fun)
