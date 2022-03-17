from playsound import playsound
from fastapi import FastAPI
app = FastAPI()
@app.get("/add")
def play():
    with open('elvis.csv', 'a')