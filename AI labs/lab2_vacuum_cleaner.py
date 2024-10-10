# Environment class to represent the 2x2 grid
class Environment:
    def __init__(self):
        # Initialize the grid with clean and dirty states
        self.grid = [['clean', 'dirty'],
                     ['clean', 'dirty']]

    # Function to check the state of the current cell (clean or dirty)
    def get_current_state(self, list_index):
        x, y = list_index
        return self.grid[x][y]

    # Function to clean the current cell
    def clean(self, list_index):
        x, y = list_index
        self.grid[x][y] = 'clean'
        print(f"The vacuum cleaner has cleaned the cell at position {list_index}")


# Agent class to represent the vacuum cleaner
class VacuumCleanerAgent:
    def __init__(self, environment):
        self.environment = environment
        self.list_index = [0, 0]

    # Function to sense the state of the current cell and act accordingly
    def sense_and_act(self):
        # Agent operates until all cells are clean (in this case, 4 cells)
        for i in range(4):
            current_state = self.environment.get_current_state(self.list_index)
            if current_state == 'dirty':
                self.environment.clean(self.list_index)
            self.move()

    # Function to move the agent to the next cell
    def move(self):
        x, y = self.list_index
        if y == 0:  # If on the left column, move right
            self.list_index = [x, y + 1]
        elif x == 0:  # If on the top row, move down after moving right
            self.list_index = [x + 1, y - 1]
        else:  # Move to the last cell
            self.list_index = [x, y + 1]
        print(f"Vacuum Cleaner moved to position {self.list_index}")


# Main simulation
def main():
    # Create the environment
    environment = Environment()

    # Create the intelligent agent
    agent = VacuumCleanerAgent(environment)

    # Let the agent autonomously sense and act until all cells are processed
    agent.sense_and_act()

    # Print the final state of the grid
    print(f"Final grid state: {environment.grid}")


if __name__ == "__main__":
    main()
