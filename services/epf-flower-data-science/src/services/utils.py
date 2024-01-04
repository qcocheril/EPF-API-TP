from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
import pickle
import json
import pandas as pd


def train_save_model():
    """
    Train a logistic regression model using the pre-split Iris dataset and save the trained model to a file.

    Returns:
    str: A message indicating the success of the training and the path where the model is saved.
    """

    file_path = "src/data/split_Iris.csv"
    with open(file_path, 'r') as json_file:
        splitted_data = json.load(json_file)
    
    X_train = splitted_data["X_train"]
    y_train = splitted_data["y_train"]
    X_train = json.loads(X_train)


    X_train_df = pd.DataFrame(X_train)
    y_train_df = pd.DataFrame({"label": y_train})

    json_file_path = 'src/config/model_parameters.json'  

    with open(json_file_path, 'r') as json_file:
        model_params = json.load(json_file)

    logistic_regression_params = model_params["logistic_regression_parameters"]

    penalty =  logistic_regression_params["penalty"]
    solver =  logistic_regression_params["solver"]
    random_state = logistic_regression_params["random_state"]
    max_iter =  logistic_regression_params["max_iter"]
    verbose =  logistic_regression_params["verbose"]

    model = LogisticRegression(penalty=penalty, solver=solver, random_state=random_state, max_iter=max_iter, verbose=verbose)
    model.fit(X_train_df,y_train_df)

    model_filename = 'src/models/model.pkl' 

    with open(model_filename, 'wb') as model_file:
        pickle.dump(model, model_file)

    return f"The model was successfully trained and saved in {model_filename}"


def make_prediction():
    """
    Make predictions using a pre-trained logistic regression model on the test set and calculate accuracy.

    The function loads the pre-split Iris test dataset and a pre-trained logistic regression model
    from the specified files. It then uses the model to make predictions on the test set and calculates
    the accuracy using 5-fold cross-validation.

    Returns:
    str: A message indicating the accuracy of the model on the test set.
    """

    file_path = "src/data/split_Iris.csv"
    with open(file_path, 'r') as json_file:
        splitted_data = json.load(json_file)
    
    X_test = splitted_data["X_test"]
    y_test = splitted_data["y_test"]
    X_test = json.loads(X_test)

    X_test_df = pd.DataFrame(X_test)
    y_test_df = pd.DataFrame({"label": y_test})

    with open('src/models/model.pkl', 'rb') as model_file:
        loaded_model = pickle.load(model_file)
    
    score = cross_val_score(loaded_model, X_test_df, y_test_df, cv=5)

    return f"The model's accuracy is {score[2]}"

    
    