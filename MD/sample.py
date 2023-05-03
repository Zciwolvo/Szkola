def find_paths(adj_matrix, start_node):
    num_nodes = len(adj_matrix)
    visited = [False] * num_nodes
    path = [start_node]
    dfs(adj_matrix, start_node, visited, path)


def dfs(adj_matrix, current_node, visited, path):
    visited[current_node] = True
    for neighbor in range(len(adj_matrix[current_node])):
        if adj_matrix[current_node][neighbor] == 1 and not visited[neighbor]:
            path.append(neighbor)
            if is_exit(adj_matrix, neighbor):
                print_path(path)
            else:
                dfs(adj_matrix, neighbor, visited, path)
            path.pop()
    visited[current_node] = False


def is_exit(adj_matrix, node):
    return sum(adj_matrix[node]) == 0


def print_path(path):
    print(" -> ".join(str(node) for node in path))


adj_matrix = [[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]]
start_node = 0
find_paths(adj_matrix, start_node)
