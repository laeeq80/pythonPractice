import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Step 1: Load the dataset from the CSV file
# Replace 'path_to_your_file.csv' with the actual file path of your dataset
file_path = r'D:\UET\Fall2024\Teaching\ArtificialIntelligence\Lab\week8Lab7\housing_prices.csv'
data = pd.read_csv(file_path)

# Display the first few rows
print("Loaded Data:")
print(data.head())

# Step 2: Split the dataset into training and testing sets
features = data[['Bedrooms', 'Size', 'Age']]
target = data['Price']
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Step 3: Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)    #For training, we use both input and output

# Step 4: Make predictions
y_pred = model.predict(X_test)   #For testing, we only give 20% input data to the model

# Step 5: Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"\nModel Evaluation:")
print(f"Mean Squared Error (MSE): {mse}")
print(f"R² Score: {r2}")

# Step 6: Visualize the predicted vs. actual values
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, color='blue', alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.title('Actual vs Predicted Housing Prices')
plt.show()
