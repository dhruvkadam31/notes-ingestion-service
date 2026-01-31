from fastapi import FastAPI
from pydantic import BaseModel
from app.cleaning.cleaner import clean_text

app = FastAPI()

@app.get("/")
def root():
    return {"message":"Server is running"}

@app.get("/health")
def health_check():
    return {"status":"ok"}

class TextInput(BaseModel):
    text: str 

@app.post("/upload/text")  
def upload_text(data: TextInput): 
    cleaned = clean_text(data.text)
    return {
        "raw_text": data.text,
        "cleaned_text":cleaned
        } 
