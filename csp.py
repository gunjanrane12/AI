# Function to check if the current color assignment is safe for a given vertex
def is_safe(graph, color, vertex, c):
    for i in range(len(graph)):
        if graph[vertex][i] == 1 and color[i] == c:  # Check adjacency
            return False
    return True

# Utility function to solve the graph coloring problem
def graph_coloring_util(graph, m, color, vertex):
    if vertex == len(graph):  # If all vertices are colored, return True
        return True
    
    # Try assigning each color to this vertex
    rgb = ["Red","Green","Blue"]
    for c in rgb:
        if is_safe(graph, color, vertex, c):
            color[vertex] = c  # Assign the color
            if graph_coloring_util(graph, m, color, vertex + 1):  # Recur to assign colors to the next vertex
                return True
            color[vertex] = 0  # Backtrack if assigning this color doesn't lead to a solution

    return False

# Main function to solve the graph coloring problem using backtracking
def graph_coloring(graph, m):
    n = len(graph)  # Number of vertices in the graph
    color = [0] * n  # Color array to store colors assigned to vertices
    
    # Call the utility function to solve the problem
    if not graph_coloring_util(graph, m, color, 0):
        print("Solution does not exist")
        return False
    
    # Print the solution
    print("Solution exists. Assigned colors are:")
    for i in range(n):
        print(f"Vertex {i} ---> Color {color[i]}")
    
    return True

# Driver code
if __name__ == "__main__":
    # Example graph represented as an adjacency matrix
    graph = [
        [0, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 1, 1, 0]
    ]
    
    m = 3  # Number of colors
    
    # Solve the graph coloring problem
    graph_coloring(graph, m)
