from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def add_neighbor(self, node):
        self.neighbors.append(node)


class BFS:
    def __init__(self, start_node, goal_nodes):
        self.start_node = start_node
        self.goal_nodes = goal_nodes

    def search(self):
        visited = set()  # To keep track of visited nodes
        queue = deque([self.start_node])  # BFS queue starting from initial node

        while queue:    # while queue is not empty
            current_node = queue.popleft()  # Dequeue the first node

            # Check if the current node is one of the goal nodes
            if current_node in self.goal_nodes:
                print(f"Goal node '{current_node.value}' found!")
                return current_node  # Return the goal node

            # Mark the node as visited
            if current_node not in visited:
                visited.add(current_node)

                # Enqueue all non-visited neighbors
                for neighbor in current_node.neighbors:
                    if neighbor not in visited:
                        queue.append(neighbor)

        print("No goal node found.")
        return None

def main():
    # Create the nodes (Initial node and three goal nodes)
    initial_node = Node("A")
    goal_node1 = Node("G1")
    goal_node2 = Node("G2")
    goal_node3 = Node("G3")

    # Create some other nodes for the graph
    node_b = Node("B")
    node_c = Node("C")
    node_d = Node("D")
    node_e = Node("E")
    node_f = Node("F")

    # Build the graph by adding neighbors
    initial_node.add_neighbor(node_b)
    initial_node.add_neighbor(node_c)

    node_b.add_neighbor(node_d)
    node_b.add_neighbor(node_e)

    node_c.add_neighbor(node_f)

    node_d.add_neighbor(goal_node1)
    node_e.add_neighbor(goal_node2)
    node_f.add_neighbor(goal_node3)

    # Define goal nodes as a list
    goal_nodes = [goal_node1, goal_node2, goal_node3]

    # Perform BFS (creating object of the BFS class)
    bfs = BFS(initial_node, goal_nodes)
    goal_node_found = bfs.search()

    # Print result
    if goal_node_found:
        print(f"Traversal successful. Reached goal: {goal_node_found.value}")

# Call the main function to run the program
if __name__ == "__main__":
    main()