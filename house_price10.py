# 🏠 House Price Prediction
# Author: Sreya
# A simple linear regression model to predict house prices based on area.

import pandas as pd
from sklearn.linear_model import LinearRegression

# Step 1: Create sample data
data = {
    'area': [1200, 1500, 1800, 2000, 2300],
    'price': [150000, 180000, 210000, 240000, 270000]
}

# Step 2: Convert data to DataFrame
df = pd.DataFrame(data)

# Step 3: Prepare training data
X = df[['area']]  # Features
y = df['price']   # Target

# Step 4: Train the model
model = LinearRegression()
model.fit(X, y)

# Step 5: Make a prediction
new_area = [[1750]]
predicted_price = model.predict(new_area)
print(f"Predicted price for {new_area[0][0]} sq.ft: ₹{predicted_price[0]:,.2f}")
