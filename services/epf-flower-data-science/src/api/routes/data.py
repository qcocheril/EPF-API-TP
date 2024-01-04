from fastapi import APIRouter
from src.services.data import download_dataset_kaggle, load_iris_dataset, split_dataset, preprocess_data

router = APIRouter()

@router.get("/download_dataset")
def download_dataset():
    """
    Endpoint to download a dataset from Kaggle using Kaggle credentials.

    This endpoint triggers the dataset download process by calling the `download_dataset_kaggle` function.

    Returns:
    str: A message indicating the successful download of the Iris dataset.
    """

    return download_dataset_kaggle()

@router.get("/load_dataset")
def load_dataset():
    """
    Endpoint to load and retrieve the Iris dataset in JSON format.

    This endpoint triggers the process of loading the Iris dataset by calling the `load_iris_dataset` function.

    Returns:
    str: The Iris dataset in JSON format.
    """
    return load_iris_dataset()

@router.get("/preprocess")
def preprocess():
    """
    Endpoint to load and preprocess the Iris dataset.

    This endpoint triggers the process of loading and preprocessing the Iris dataset by calling the `preprocess_data` function.

    Returns:
    dict: The preprocessed Iris dataset.
    """
    return preprocess_data()

@router.get("/split")
def split():
    """
    Endpoint to preprocess and split the Iris dataset into train and test sets.

    This endpoint triggers the process of preprocessing and splitting the Iris dataset by calling the `split_dataset` function.

    Returns:
    str: A message indicating the successful splitting and saving of the Iris dataset.
    """
    return split_dataset()


        