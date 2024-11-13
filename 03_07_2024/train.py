# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load your dataset
data = pd.read_csv('winequality-red.csv')

# Features and target
X = data[['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 
          'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 
          'pH', 'sulphates', 'alcohol']]
y = data['quality']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the model and hyperparameters
rf = RandomForestClassifier(random_state=42)
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [10, 20, 30],
    'min_samples_split': [2, 5, 10]
}

# Perform hyperparameter tuning using GridSearchCV
grid_search = GridSearchCV(rf, param_grid, cv=5, n_jobs=-1, verbose=1)
grid_search.fit(X_train, y_train)

# Get the best model
best_rf = grid_search.best_estimator_

# Save the model
with open('wine_quality_model.pkl', 'wb') as file:
    pickle.dump(best_rf, file)

print("Model trained and saved as wine_quality_model.pkl")
