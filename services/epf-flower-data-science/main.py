import uvicorn
import os
from src.app import get_application

# The following line sets the GOOGLE_APPLICATION_CREDENTIALS variable to the path of my google cloud firestore account key. 
# This is necessary to access the firestore API.
# You will need to fill in your own key to run the firestore related functions

# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'service-account-key.json'

app = get_application()

if __name__ == "__main__":
    uvicorn.run("main:app", debug=True, reload=True, port=8080)
