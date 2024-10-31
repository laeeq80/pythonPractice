import heapq

class GreedyBestFirstSearch:
    def __init__(self, grid, start, goal):
        """
        Initialize the search object with the grid, start position, and goal position.
        """
        self.grid = grid
        self.start = start
        self.goal = goal
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Directions: up, down, left, right
        self.visited = set()  # Set to keep track of visited nodes
        self.came_from = {}  # Dictionary to track the path

    def manhattan_distance(self, node):
        """
        Calculate the Manhattan distance between the current node and the goal.
        """
        return abs(node[0] - self.goal[0]) + abs(node[1] - self.goal[1])

    def search(self):
        """
        Perform the Greedy Best-First Search and return the path if found.
        """
        # Priority queue to store nodes to explore, sorted by heuristic value
        priority_queue = []
        # Add the start node with its heuristic value (distance to goal)
        heapq.heappush(priority_queue, (self.manhattan_distance(self.start), self.start))

        # Initialize the visited set and came_from dict
        self.visited.add(self.start)
        self.came_from[self.start] = None

        # Start the search process
        while priority_queue:
            # Pop the node with the lowest heuristic value
            _, current = heapq.heappop(priority_queue)

            # If we reached the goal, reconstruct and return the path
            if current == self.goal:
                return self.reconstruct_path(current)

            # Explore neighbors
            for direction in self.directions:
                neighbor = (current[0] + direction[0], current[1] + direction[1])

                # Check if the neighbor is within bounds and is not blocked
                if 0 <= neighbor[0] < len(self.grid) and 0 <= neighbor[1] < len(self.grid[0]):
                    if self.grid[neighbor[0]][neighbor[1]] == 0 and neighbor not in self.visited:
                        # Mark as visited and add to the queue
                        self.visited.add(neighbor)
                        self.came_from[neighbor] = current
                        heapq.heappush(priority_queue, (self.manhattan_distance(neighbor), neighbor))

        # If no path is found
        return None

    def reconstruct_path(self, current):
        """
        Reconstruct the path from start to goal by tracing the came_from dictionary.
        """
        path = []
        while current is not None:
            path.append(current)
            current = self.came_from[current]
        path.reverse()  # Reverse the path to go from start to goal
        return path


# Example Usage
if __name__ == "__main__":
    # Define the grid, start, and goal
    grid = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]
    start = (0, 0)
    goal = (4, 4)

    # Create an instance of the GreedyBestFirstSearch class
    gbfs = GreedyBestFirstSearch(grid, start, goal)

    # Perform the search
    path = gbfs.search()

    # Print the result
    if path:
        print("Path found:", path)
    else:
        print("No path found.")
