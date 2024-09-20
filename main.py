import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Generate random data
np.random.seed(42)  # For reproducibility
x = np.random.rand(50) * 10
y = np.random.rand(50) * 10
z = np.random.rand(50) * 10

# Create a figure and a 3D Axes
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot
ax.scatter(x, y, z, c='b', marker='o')

# Set labels
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

# Set title
ax.set_title('3D Scatter Plot Example')

# Show plot
plt.show()