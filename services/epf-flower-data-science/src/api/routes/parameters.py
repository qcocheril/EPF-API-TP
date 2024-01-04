from fastapi import APIRouter
from src.services.parameters import create_firestore_doc, retrieve_parameters, add_update_parameters

router = APIRouter()

@router.get("/create_firestore")
def create_firestore():
    """
    This endpoint triggers the creation of a Firestore document by calling the `create_firestore_doc` function.

    Returns:
    str: A message showing the successful creation of the Firestore document.
    """
    return create_firestore_doc()

@router.get("/retrieve_params")
def retrieve_params():
    """
    This endpoint triggers the retrieval of parameters by calling the `retrieve_parameters` function.

    Returns:
    str: A message showing the success of the document retrieval and the retrieved parameters.
    """
    return retrieve_parameters()

@router.get("/add_update_params")
def add_update_params():
    """
    This endpoint triggers the addition or update of parameters by calling the `add_update_parameters` function.

    Returns: 
    str: A message showing the success of the modification of the parameters.
    """
    return add_update_parameters()