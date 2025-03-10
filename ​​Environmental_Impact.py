# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1doljiSilJ6MnMWahmM8YrvZVy4K02yZA
"""

from sklearn.preprocessing import MinMaxScaler, LabelEncoder

# Select relevant columns for sustainability and environmental impact analysis
relevant_columns = [
    "rainfall", "soil_moisture", "irrigation_frequency", "fertilizer_usage",
    "organic_matter", "urban_area_proximity", "pest_pressure", "water_usage_efficiency", "label"
]
data_subset = data[relevant_columns]

# Encode the 'label' column (categorical data)
# Encode the 'label' column (categorical data)
# Encode the 'label' column (categorical data)
# Encode the 'label' column (categorical data)
label_encoder = LabelEncoder()
data_subset["label_encoded"] = label_encoder.fit_transform(data_subset["label"])
data_subset.drop("label", axis=1, inplace=True)

# Normalize numerical features
scaler = MinMaxScaler()
numerical_columns = [
    "rainfall", "soil_moisture", "irrigation_frequency", "fertilizer_usage",
    "organic_matter", "urban_area_proximity", "pest_pressure", "water_usage_efficiency"
]
data_subset[numerical_columns] = scaler.fit_transform(data_subset[numerical_columns])

# Display the processed dataset
data_subset.head()

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

# Load the data
df = pd.read_csv('/content/Environmental Impact.csv')

# Prepare the dataset
X = df[["rainfall", "soil_moisture", "irrigation_frequency", "fertilizer_usage",
        "organic_matter", "urban_area_proximity", "pest_pressure", "label"]]
y = df['water_usage_efficiency']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Preprocess the data
X_train_numeric = X_train.drop('label', axis=1)
X_test_numeric = X_test.drop('label', axis=1)

# Convert to numeric and handle non-numeric values
X_train_numeric = X_train_numeric.apply(pd.to_numeric, errors='coerce')
X_test_numeric = X_test_numeric.apply(pd.to_numeric, errors='coerce')

# Fill NaN values with mean
X_train_numeric = X_train_numeric.fillna(X_train_numeric.mean())
X_test_numeric = X_test_numeric.fillna(X_test_numeric.mean())

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_numeric)
X_test_scaled = scaler.transform(X_test_numeric)

# Belief Rule-Based Expert System (BRBES) Model
def belief_rule_model(X, weights=None):
    if weights is None:
        weights = np.ones(X.shape[1]) / X.shape[1]

    scores = np.sum(X * weights, axis=1)
    return scores

# Evaluate models
models = {
    "BRBES": belief_rule_model(X_test_scaled),
    "Linear Regression": LinearRegression().fit(X_train_scaled, y_train).predict(X_test_scaled),
    "Random Forest": RandomForestRegressor(random_state=42).fit(X_train_scaled, y_train).predict(X_test_scaled),
    "Decision Tree": DecisionTreeRegressor(random_state=42).fit(X_train_scaled, y_train).predict(X_test_scaled),
    "Neural Network": MLPRegressor(random_state=42, max_iter=500).fit(X_train_scaled, y_train).predict(X_test_scaled)
}

# Compute metrics
results = []
for name, predictions in models.items():
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    rmse = np.sqrt(mse)
    results.append({
        "Model": name,
        "Accuracy %": r2 * 100,
        "RMSE": rmse
    })

# Create results DataFrame
results_df = pd.DataFrame(results)
print(results_df)

