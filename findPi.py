import random

def estimate_pi(num_points):
    points_inside_circle = 0
    total_points = num_points

    for _ in range(num_points):
        x = random.uniform(0, 1)  # Random x-coordinate between 0 and 1
        y = random.uniform(0, 1)  # Random y-coordinate between 0 and 1
        distance = x**2 + y**2  # Distance from the origin (0, 0)

        if distance <= 1:
            points_inside_circle += 1

    pi_estimate = 4 * points_inside_circle / total_points
    return pi_estimate

# Example usage:
num_points = int(input("Enter the number of random points to estimate pi: "))
pi_estimate = estimate_pi(num_points)
print(f"Estimated value of pi using {num_points} points: {pi_estimate}")
