import random

class Stock:
    def __init__(self, name, price_per_stock, risk, monthly_return):
        self.name = name
        self.price_per_stock = price_per_stock
        self.risk = risk
        self.monthly_return = monthly_return

    def __repr__(self):
        return f"{self.name} (Price: {self.price_per_stock}, Risk: {self.risk}, Return: {self.monthly_return})"


class Portfolio:
    def __init__(self, stocks):
        self.stocks = stocks

    def total_value(self):
        return sum(stock.price_per_stock for stock in self.stocks)

    def average_risk(self):
        return sum(stock.risk for stock in self.stocks) / len(self.stocks)

    def average_return(self):
        return sum(stock.monthly_return for stock in self.stocks) / len(self.stocks)


class GeneticAlgorithm:
    def __init__(self, stocks, population_size, portfolio_size):
        self.stocks = stocks
        self.population_size = population_size
        self.portfolio_size = portfolio_size
        self.population = self.initialize_population()

    def initialize_population(self):
        population = []
        for _ in range(self.population_size):
            selected_stocks = random.sample(self.stocks, self.portfolio_size)
            population.append(Portfolio(selected_stocks))
        return population

    def evaluate_portfolio(self, portfolio):
        return portfolio.average_return() / portfolio.average_risk()  # Example fitness function

    def selection(self):
        # Sort portfolios based on their fitness
        self.population.sort(key=self.evaluate_portfolio, reverse=True)  # descending order
        return self.population[:self.population_size // 2]  # Select the top half

    def crossover(self, parent1, parent2):
        child_stocks = list(set(parent1.stocks) | set(parent2.stocks))  # Union of stocks
        return Portfolio(random.sample(child_stocks, self.portfolio_size))

    def mutate(self, portfolio):
        # Check if a random number between 0 and 1 is less than 0.1 (10% chance)
        if random.random() < 0.1:  # 10% chance to mutate
            # Select a new stock randomly from the available stocks that are not already in the portfolio
            new_stock = random.choice([s for s in self.stocks if s not in portfolio.stocks])
            # Replace a random stock in the portfolio with the new stock
            portfolio.stocks[random.randint(0, self.portfolio_size - 1)] = new_stock

    def run(self, generations):
        # Iterate through the number of generations specified
        for _ in range(generations):
            # Select the best-performing portfolios from the current population
            selected = self.selection()
            # Create a new generation list starting with the selected portfolios
            next_generation = selected[:]
            # Continue adding portfolios to the next generation until it reaches the desired population size
            while len(next_generation) < self.population_size:
                # Randomly select two parents from the selected portfolios
                parent1, parent2 = random.sample(selected, 2)
                # Create a child portfolio by crossing over the two selected parents
                child = self.crossover(parent1, parent2)
                # Mutate the child portfolio with a certain probability
                self.mutate(child)
                # Add the child portfolio to the next generation
                next_generation.append(child)
            # Update the population to the newly created next generation
            self.population = next_generation

        # Final selection of the best portfolio
        best_portfolio = max(self.population, key=self.evaluate_portfolio)
        return best_portfolio


# Stock Data
stocks_data = [
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

# User input
population_size = int(input("Enter the population size: "))
portfolio_size = int(input("Enter the portfolio size: "))
generations = int(input("Enter the number of generations: "))  # Set the number of generations

ga = GeneticAlgorithm(stocks_data, population_size, portfolio_size)
best_portfolio = ga.run(generations)

# Output the best portfolio found
print("Best Portfolio:")
for stock in best_portfolio.stocks:
    print(stock)
