import pandas as pd
import numpy as np

# Set a random seed for reproducibility
np.random.seed(42)

# Generate random data for the dataset
num_samples = 100  # Number of rows in the dataset

bedrooms = np.random.randint(1, 6, size=num_samples)  # 1 to 5 bedrooms
sizes = np.random.randint(800, 3500, size=num_samples)  # Size in square feet
ages = np.random.randint(0, 30, size=num_samples)  # House age in years
prices = (sizes * 120) - (ages * 2500) + (bedrooms * 10000) + np.random.randint(-10000, 10000, size=num_samples)

# Create a DataFrame
data = pd.DataFrame({
    'Bedrooms': bedrooms,
    'Size': sizes,
    'Age': ages,
    'Price': prices
})

# Save the dataset to a CSV file
data.to_csv(r'D:\UET\Fall2024\Teaching\ArtificialIntelligence\Lab\week8Lab7\housing_prices.csv', index=False)

print("Dataset created and saved as 'housing_prices.csv'.")
