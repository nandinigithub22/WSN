import matplotlib.pyplot as plt
import numpy as np


def generate_random_coordinates(num_points, x_max, y_max):
    """Generate random (x, y) coordinates within the specified region."""
    x_coordinates = np.random.randint(0, x_max, num_points)
    y_coordinates = np.random.randint(0, y_max, num_points)
    return x_coordinates, y_coordinates


def calculate_distances(x_coords, y_coords, bs_point):
    """Calculate distances from each point to the base station (BS) point."""
    distances = np.sqrt((x_coords - bs_point[0]) ** 2 + (y_coords - bs_point[1]) ** 2)
    return distances


def plot_points_and_bs(x_coords, y_coords, bs_point, x_max, y_max):
    """Plot the points and the BS point, and draw lines connecting them."""
    plt.scatter(x_coords, y_coords, marker='*', color='red', label='Random Points')
    plt.scatter(bs_point[0], bs_point[1], marker='o', color='green', label='BS Point')

    for i in range(len(x_coords)):
        plt.plot([bs_point[0], x_coords[i]], [bs_point[1], y_coords[i]], linestyle='--', color='black')

    plt.xlim(0, x_max)
    plt.ylim(0, y_max)
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.title('Random Points and BS Point')
    plt.legend()
    plt.show()


# Taking input from user
x = int(input("Enter the number of x Co-ordinates: "))
y = int(input("Enter the number of y Co-ordinates: "))
x_area = int(input("Enter the length of x Region: "))
y_area = int(input("Enter the length of y Region: "))

# Generate random coordinates
x_coordinates, y_coordinates = generate_random_coordinates(x, x_area, y_area)

# BS point
bs_point = (x_area / 2, y_area / 2)

# Calculate distances
distances = calculate_distances(x_coordinates, y_coordinates, bs_point)

# Plot points and BS point
plot_points_and_bs(x_coordinates, y_coordinates, bs_point, x_area, y_area)

# Output distances
for i in range(len(distances)):
    print(f"Distance between point {i} and BS: {distances[i]}")
