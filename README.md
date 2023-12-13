# EPF-API-TP

- **Question 1:** _Which Python library/framework is often used to create fast, simple REST APIs?_

  - Django

  - Flask

  - FastAPI

  - All of the above

- **Question 2:** _What's the main difference between Django, Flask and FastAPI in terms of performance and speed?_

  - Django is generally faster than Flask and FastAPI.

  - Flask outperforms Django and FastAPI.

  - FastAPI is renowned for its increased speed and performance compared with Django and Flask.

  - Django, Flask and FastAPI have equivalent performance.

- **Question 3:** What is an endpoint in the context of REST APIs?\*

  - A unique IP address associated with an API.

  - A breakpoint in the code where the API can be interrupted.

  - A specific URL to which a request can be sent to interact with the API.

  - A unique identifier assigned to each incoming request.

- **Question 4:** _What are the main HTTP verbs used to define REST API methods?_

  - GET, POST, PUT, PATCH, DELETE

  - SEND, RECEIVE, UPDATE, REMOVE

  - READ, WRITE, MODIFY, DELETE

  - FETCH, INSERT, UPDATE, DELETE

- **Question 5:** _In the context of REST APIs, what does the term "middleware" mean?_

  - A component that processes data sent by the user.

  - An external library used to speed up API development.

  - Intermediate software that processes the request before it reaches the main application.

  - A method for securing data stored in the database.

- **Question 6:** _Which Python library is often used to serialize and deserialize JSON data in the context of REST APIs?_

  - JSONify

  - PyJSON

  - json.dumps() and json.loads()

  - serializeJSON

- **Question 7:** _What is the main use of the HTTP "PUT" method in the context of REST APIs?_

  - Create a new resource.

  - Update an existing resource, or create one if it doesn't exist.

  - Delete a resource.

  - Read a specific resource.

- **Question 8:** In FastAPI, how do you define an endpoint to handle a POST request with JSON data?\*

  - @app.post("/endpoint")

  - @app.get("/endpoint")

  - @app.request("/endpoint")

  - @app.update("/endpoint")

# Creating an API with FastAPI

### Introduction

In this exercice you are going to develop an API with fastAPI for getting machine learning prediction and interact with a firestore database.

### Few elements to remember about the REST Protocol

REST (Representational State Transfer) is an architectural style for designing networked applications. RESTful APIs (Application Programming Interfaces) conform to the principles of REST, allowing systems to communicate over HTTP in a stateless manner; Some important aspects are:

- **Resources:** Everything is a resource, identified by a unique URI.

- **HTTP Methods:** CRUD operations are performed using standard HTTP methods (GET, POST, PUT, DELETE).

- **Stateless:** Each request from a client contains all the information needed to understand and fulfill the request.

### Key Concepts in FastAPI:

- **Endpoint:**

- **Basic HTTP Methods:**

- **Request and Response:**

### Objective

- **Step 1: Installing libraries:** Make sure you have FastAPI, Uvicorn, Pandas, Scikit-learn and Firestore libraries installed.

- **Step 2: Project initialization:** Create a main.py file, initialize the application and launch it with uvicorn.

- **Step 3: Project initialization:** Create a main.py file, initialize the application and launch it with uvicorn.

- **Step 4: Loading the Iris Flower dataset:** Add an endpoint to load the "Iris Flowwer" dataset and return it.

- **Step 5: Processing the dataset:** Add an endpoint to be able to perform the necessary processing on the data before being able to train a model with it.

- **Step 6: Training the classification model:** Add an endpoint to train a classification model with the processed dataset as input (take a simple model to start with).

- **Step 7: Create the Firestore collection:** Create the firestore collection "parameters" with the following parameters: "n_estimators", "criterion".

- **Step 8: Retrieve parameters from Firestore:** Add an endpoint to retrieve parameters from Firestore.

- **Step 9: Update and add Firestore parameters:** Add endpoints to update or add parameters in Firestore.

- **Step 10: Prediction with Trained Model:** Add endpoint to make predictions with trained model and parameters

- **Step 11: Swagger documentation:** Access automatically generated Swagger documentation. Add a route that returns an OPENAPI YAML schema for a static version of the schema.

### Evaluation requirements

The evaluation criteria will be as follows:

- Proper functioning of endpoints
- Clear documentation of code, use of explicit names and compliance with REST naming conventions
- Static swagger generation through an API route
- Completion of unit tests

The completion of this TP is relatively long and may overtake TP3, but steps 1-5 and 10-12 must be completed in TP2 in order to have a correct basis for TP3.

### Documentation link :

- FastApi: https://fastapi.tiangolo.com/

- Google Cloud Firestore: https://cloud.google.com/python/docs/reference/firestore/latest/index.html

- Scikit-Learn: https://scikit-learn.org/stable/index.html

- Pandas: https://pandas.pydata.org/docs/
