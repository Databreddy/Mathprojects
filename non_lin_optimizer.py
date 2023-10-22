from scipy.optimize import minimize

# Define the objective function to minimize
def objective_function(x):
    return x[0]**2 + x[1]**2  # Example objective function (x^2 + y^2)

# Initial guess (starting point for the optimization)
initial_guess = [1.0, 1.0]

# Perform nonlinear optimization
result = minimize(objective_function, initial_guess, method='BFGS')

# Print the optimization result
print("Optimal solution:", result.x)
print("Optimal objective value:", result.fun)
