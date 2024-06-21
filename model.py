import joblib

def load_model(model_path):
    """
    Load a pre-trained model from the specified path.
    
    Args:
        model_path (str): The path to the model file.
    
    Returns:
        Loaded model.
    """
    return joblib.load(model_path)

def predict(model, data):
    """
    Predict using the provided model and input data.
    
    Args:
        model: The loaded model.
        data (DataFrame): The input data for prediction.
    
    Returns:
        predictions (array): Predicted values.
    """
    return model.predict(data)

def predict_proba(model, data):
    """
    Predict probabilities using the provided model and input data.
    
    Args:
        model: The loaded model.
        data (DataFrame): The input data for prediction.
    
    Returns:
        probabilities (array): Probability of each class.
    """
    return model.predict_proba(data)
