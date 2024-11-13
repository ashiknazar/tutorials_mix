# model.py
import pickle

# Load your trained model (make sure you have trained and saved your model as 'wine_quality_model.pkl')
with open('wine_quality_model.pkl', 'rb') as file:
    model = pickle.load(file)

def test_quality(fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, 
                 free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol):
    # Create a dataframe or numpy array as per your model's requirement
    import numpy as np
    X = np.array([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, 
                   free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]])
    
    # Predict quality
    predicted_quality = model.predict(X)
    
    return predicted_quality[0]
