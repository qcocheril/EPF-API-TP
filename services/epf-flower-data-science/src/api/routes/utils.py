from fastapi import APIRouter
from src.services.utils import train_save_model, make_prediction

router = APIRouter()

@router.get("/train_model")
def train_model():
    """
    Endpoint to train a machine learning model.

    This endpoint triggers the training process by calling the `train_save_model` function.

    Returns:
    str: A message indicating the success of the model training and the path where the model is saved.
    """

    return train_save_model()

@router.get("/predict")
def predict():
    """
    Endpoint to make predictions using a pre-trained machine learning model.

    This endpoint triggers the prediction process by calling the `make_prediction` function.

    Returns:
    str: A message indicating the accuracy of the model on the test set.
    """

    return make_prediction()