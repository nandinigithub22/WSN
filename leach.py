import random
import numpy as np
import matplotlib.pyplot as plt

# Constants
NUM_NODES = int(input("Enter no of nodes : "))
AREA_SIZE = int(input("Size of Area (NxN) : "))
cluster_head_probability = float(input(("Enter Probability of being a cluster head : ")) # Probability of being a cluster head

# Initialize nodes
def initialize_nodes(num_nodes, area_size):
    nodes = [(random.uniform(0, area_size), random.uniform(0, area_size)) for _ in range(num_nodes)]
    return nodes
# Select cluster heads
def select_cluster_heads(nodes, prob):
    cluster_heads = []
    for node in nodes:
        if random.random() < prob:
            cluster_heads.append(node)
     return cluster_heads

# Assign nodes to cluster heads
def assign_to_cluster_heads(nodes, cluster_heads):
    assignments = {}
    for node in nodes:
        if node not in cluster_heads:
            min_dist = float('inf')
            closest_cluster_head = None
            for ch in cluster_heads:
                dist = np.sqrt((node[0] - ch[0])**2 + (node[1] - ch[1])**2)
                if dist < min_dist:
                    min_dist = dist
                    closest_cluster_head = ch
            assignments[node] = closest_cluster_head
    return assignments

# Plotting the network
def plot_network(nodes, cluster_heads, assignments):
    plt.figure(figsize=(10, 10))
    for node in nodes:
        if node in cluster_heads:
            plt.scatter(node[0], node[1], c='red', marker='^')  # Cluster heads in red
        else:
            plt.scatter(node[0], node[1], c='blue', marker='o')  # Regular nodes in blue
            if node in assignments:
                plt.plot([node[0], assignments[node][0]], [node[1], assignments[node][1]], 'k--')  # Connect to cluster head

    plt.title('LEACH Protocol - Cluster Formation')
    plt.xlabel('X-coordinate')
    plt.ylabel('Y-coordinate')
    plt.show()

nodes = initialize_nodes(NUM_NODES, AREA_SIZE)
cluster_heads = select_cluster_heads(nodes, cluster_head_probability)
assignments = assign_to_cluster_heads(nodes, cluster_heads)
plot_network(nodes, cluster_heads, assignments)
