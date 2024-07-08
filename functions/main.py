import firebase_admin
import uvicorn
from fastapi import FastAPI
from firebase_admin import credentials, firestore

cred = credentials.Certificate("D:/Git_Hub/kkumool-backend/functions/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/add-user")
def add_user(user_id: str, name: str):
    doc_ref = db.collection('users').document(user_id)
    doc_ref.set({
        'name': name
    })
    return {"message": "User added successfully"}

@app.get("/get-user/{user_id}")
def get_user(user_id: str):
    doc_ref = db.collection('users').document(user_id)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    else:
        return {"message": "User not found"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)