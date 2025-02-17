import numpy as np
import random

# Define the Stock class
class Stock:
    def __init__(self, name, price, risk, return_rate):
        self.name = name  # Stock name (e.g., "Apple Inc.")
        self.price = price  # Stock price (e.g., 195.10 for Apple)
        self.risk = risk  # Risk factor (between 0 and 1, e.g., 0.75 for Apple)
        self.return_rate = return_rate  # Expected return rate (e.g., 3.00 for Apple)

# Stock Data (Example stocks with their risk and return rates)
data = [
    Stock("Apple Inc.", 195.10, 0.75, 3.00),
    Stock("Microsoft Corp.", 345.30, 0.70, 2.80),
    Stock("Amazon.com Inc.", 138.50, 0.85, 2.50),
    Stock("Alphabet Inc. (GOOGL)", 143.75, 0.65, 3.10),
    Stock("Tesla Inc.", 248.20, 0.90, 4.00),
    Stock("Berkshire Hathaway Inc.", 353.00, 0.50, 1.50),
    Stock("Meta Platforms, Inc.", 358.00, 0.80, 2.00),
    Stock("Johnson & Johnson", 158.60, 0.40, 1.80),
    Stock("Procter & Gamble Co.", 157.75, 0.35, 1.40),
    Stock("Visa Inc.", 233.00, 0.60, 2.30),
    Stock("Walt Disney Co.", 97.25, 0.70, 2.60),
    Stock("JPMorgan Chase & Co.", 142.90, 0.50, 1.90),
    Stock("Coca-Cola Co.", 59.40, 0.30, 1.20),
    Stock("Exxon Mobil Corp.", 116.25, 0.55, 2.00),
    Stock("NVIDIA Corp.", 426.75, 0.95, 5.00),
    Stock("Pfizer Inc.", 34.50, 0.40, 1.00),
    Stock("Intel Corporation", 34.85, 0.70, 1.50),
    Stock("Oracle Corporation", 111.40, 0.60, 2.10),
    Stock("IBM", 143.10, 0.50, 1.30),
    Stock("Cisco Systems, Inc.", 56.75, 0.45, 1.60),
]

# Parameters for Reinforcement Learning (RL)
gamma = 0.9  # Discount factor that weights future rewards
alpha = 0.1  # Learning rate that controls how much new information updates the Q-values
epsilon = 0.1  # Exploration rate that controls the probability of taking random actions
episodes = 1000  # Number of episodes to run the Q-learning process

# Create a Q-table (stocks x actions)
num_stocks = len(data)  # Number of stocks
actions = [-1, 0, 1]  # Possible actions: -1 = reduce allocation, 0 = hold allocation, 1 = increase allocation
Q = np.zeros((num_stocks, len(actions)))  # Initialize Q-table with zeros (stocks x actions)

# Helper function to calculate portfolio reward based on action
def calculate_reward(stock, action):
    # Reward is the return_rate of the stock minus a penalty for risk (scaled by action)
    return stock.return_rate - stock.risk * abs(action)  # Penalize risk when allocating more or less

# Epsilon-greedy action selection (for exploration vs exploitation)
def select_action(state):
    # Epsilon-greedy strategy to balance exploration and exploitation
    if random.uniform(0, 1) < epsilon:
        return random.choice(range(len(actions)))  # Explore: choose a random action (Exploration)
    else:
        return np.argmax(Q[state])  # Exploit: choose the best action based on Q-values  (Exploitation)

# Q-learning loop for multiple episodes
for episode in range(episodes):  # Repeat for a fixed number of episodes
    for stock_index, stock in enumerate(data):  # Iterate through all the stocks
        # Select an action for the current stock using epsilon-greedy policy
        action = select_action(stock_index)

        # Calculate the reward for taking the selected action
        reward = calculate_reward(stock, actions[action])

        # Q-value update using the Bellman equation
        best_future_q = np.max(Q[stock_index])  # Max Q-value for the current stock's next state (future action)
        # Update Q-value based on the observed reward and best future Q-value
        Q[stock_index, action] += alpha * (reward + gamma * best_future_q - Q[stock_index, action])

# After training, display the optimal portfolio rebalancing strategy
print("Optimal Portfolio Rebalancing Strategy:")
for stock_index, stock in enumerate(data):  # For each stock in the portfolio
    best_action = actions[np.argmax(Q[stock_index])]  # Find the best action for the current stock
    # Map the action value to a human-readable string
    action_str = "Increase" if best_action == 1 else "Hold" if best_action == 0 else "Reduce"
    # Print the stock name and the recommended action
    print(f"{stock.name}: {action_str}")
