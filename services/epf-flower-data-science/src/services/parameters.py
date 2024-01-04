from google.cloud import firestore

def create_firestore_doc():
    """
    Create a Firestore document in the 'parameters' collection with predefined parameters.

    This function initializes a connection to Firestore, specifies the collection ('parameters')
    and document ('parameters') names, and sets predefined parameters (e.g., 'n_estimators' and 'criterion').
    The document is then created in Firestore with the specified parameters.

    Returns:
    str: A message indicating the successful creation of the Firestore document.
    """

    db = firestore.Client()

    collection_name = 'parameters'
    document_name = 'parameters'

    params = {
        'n_estimators': 100,
        'criterion': 'gini'
    }

    doc_ref = db.collection(collection_name).document(document_name)

    doc_ref.set(params)

    return f'Document created'
    

def retrieve_parameters():
    """
    Retrieve parameters from a Firestore document in the 'parameters' collection.

    This function initializes a connection to Firestore, specifies the collection ('parameters')
    and document ('parameters') names, and retrieves the document from Firestore. If the document
    exists, its data is converted to a dictionary and returned as part of a success message.
    If the document does not exist, an appropriate message is returned.

    Returns:
    str: A message showing the success of the document retrieval and the retrieved parameters.
    """

    db = firestore.Client()

    collection_name = 'parameters'
    document_name = 'parameters'

    doc_ref = db.collection(collection_name).document(document_name)

    doc = doc_ref.get()

    if doc.exists:

        parameters_data = doc.to_dict()

        message = f"Retrieved parameters:, {parameters_data}"
    else:
        message = f"Document {document_name} does not exist in collection {collection_name}"

    return message

def add_update_parameters():
    """
    Add or update parameters in a Firestore document in the 'parameters' collection.

    This function initializes a connection to Firestore, specifies the collection ('parameters')
    and document ('parameters') names, and updates the document with new parameters. If the
    document does not exist, a new one is created. The updated or added parameters are printed.

    Returns:
    str: A message showing the success of the modification of the parameters.
    """
    db = firestore.Client()

    collection_name = 'parameters'
    document_name = 'parameters'

    document_ref = db.collection(collection_name).document(document_name)

    new_parameters = {
        'new_parameter1': 'value1',
        'new_parameter2': 'value2'
    }

    document_ref.update(new_parameters)

    message = f'Parameters updated or added to document {document_name} in collection {collection_name}: {new_parameters}'
    return message
