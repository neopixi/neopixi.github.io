from playsound import playsound
from fastapi import FastAPI
app = FastAPI()
@app.get("/playsound")
def play():
    playsound('nananana.mp3')