# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 17:05:41 2025

@author: Teena Sharma
"""


"""# Question 1
"""

import numpy as np
import matplotlib.pyplot as plt

def generate_points_around_line(a, b, n):
    x_values = np.linspace(-15, 15, n)
    noise = np.random.normal(0, 1, n)
    y_values = a * x_values + b + noise
    return x_values, y_values

# Parameters
a = -5
b = 7
n = 200

# Generate points around the line
x_values, y_noisy_values = generate_points_around_line(a, b, n)

# Compute the values of y for each x as yi = 2xi + 3
y_values = a*x_values + b

# Plot the line y = 2x + 3 in black color
plt.plot(x_values, y_values, color='black', label='y = -5x + 7')

# Show the scatter plot of the noisy points in red color
plt.scatter(x_values, y_noisy_values, color='red', label='Noisy Points')

# Add labels and legend
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Show the plot
plt.show()

"""# Question 2
"""

from mpl_toolkits.mplot3d import Axes3D

def generate_points_around_line(a, b, n):
    x_values = np.linspace(-15, 15, n)
    noise = np.random.normal(0, 1, n)
    y_values = a * x_values + b + noise
    return x_values, y_values

def compute_elementwise_error(a, b, x_values, y_values):
    y_hat = a * x_values + b
    return y_values - y_hat

def compute_average_error(errors):
    return np.mean(errors**2)

# Parameters
n = 200
interval = np.arange(-15, 15.2, 0.2)

# Generate grid of a and b values
a_values, b_values = np.meshgrid(interval, interval)

# Initialize an array to store average errors for each combination of a and b
average_errors = np.zeros_like(a_values)

# Loop through all combinations of a and b
for i in range(len(interval)):
    for j in range(len(interval)):
        a = a_values[i, j]
        b = b_values[i, j]

        # Generate noisy points around the line y = ax + b
        x_values, y_values = generate_points_around_line(a, b, n)

        # Compute element-wise errors
        errors = compute_elementwise_error(a, b, x_values, y_values)

        # Compute average error for this combination of a and b
        average_errors[i, j] = compute_average_error(errors)

# Plot the error surface
fig = plt.figure(figsize=(16, 14))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(a_values, b_values, average_errors, cmap='viridis')
ax.set_xlabel('a')
ax.set_ylabel('b')
ax.set_zlabel('Average Error (E)')
ax.set_title('Average Error Surface')
plt.show()
