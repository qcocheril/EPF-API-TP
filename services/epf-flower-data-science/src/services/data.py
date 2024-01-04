import kaggle
import pandas as pd
from sklearn.model_selection import train_test_split
import json
import numpy as np

def download_dataset_kaggle():
    """
    Download the Iris dataset from Kaggle using Kaggle credentials.

    This function authenticates with the Kaggle API using the provided Kaggle credentials and
    downloads the Iris dataset ('uciml/iris') into the 'src/data' directory. The downloaded
    files are then unzipped. 

    Returns:
    str: A message indicating the successful download of the Iris dataset.
    """

    kaggle.api.authenticate()
    dataset_name = "uciml/iris"
    save_dir = "src/data"
    kaggle.api.dataset_download_files(dataset_name, path=save_dir, unzip=True)
    message = "Download successful"
    return message

def load_iris_dataset():
    """
    Load the Iris dataset and return it in JSON format.

    This function reads the Iris dataset from the 'src/data/Iris.csv' file into a pandas DataFrame.
    It then converts the DataFrame to JSON format using the 'records' orientation. 

    Returns:
    str: The Iris dataset in JSON format.
    """

    iris_df = pd.read_csv("src/data/Iris.csv")
    iris_json = iris_df.to_json(orient="records")

    return iris_json

def preprocess_data():
    """
    Load and preprocess the Iris dataset.

    This function utilizes the `load_iris_dataset` function to load the Iris dataset in JSON format.
    It then converts the JSON data into a Python dictionary. 

    Returns:
    dict: The preprocessed Iris dataset.
    """
     
    iris_json = load_iris_dataset()
    iris = json.loads(iris_json)

    return iris

def split_dataset():
    """
    Preprocess the Iris dataset, split it into train and test sets, and save the split dataset in JSON format.

    This function uses the `preprocess_data` function to load and preprocess the Iris dataset. It then splits
    the dataset into training and testing sets. The resulting split dataset is converted into a JSON format 
    and saved to the 'src/data/split_Iris.csv' file. 

    Returns:
    str: A message indicating the successful splitting and saving of the Iris dataset.
    """

    iris = preprocess_data()

    iris_df = pd.DataFrame(iris)

    features = iris_df.drop("Species", axis=1)
    labels = iris_df["Species"]

    X_train, X_test, y_train, y_test = train_test_split(features, labels, train_size=0.8, random_state=42)
    splitted_dataset = {
        "X_train": X_train.to_json(orient="records"),
        "X_test": X_test.to_json(orient="records"),
        "y_train": y_train.to_list(),
        "y_test": y_test.to_list(),
    }

    json_data = json.dumps(splitted_dataset, indent=2)  

    file_path = 'src/data/split_Iris.csv'
    with open(file_path, 'w') as json_file:
        json_file.write(json_data)

    return f"Iris dataset splitted successfully."

