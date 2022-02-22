from fastapi import FastAPI

app = FastAPI()

@app.get('/', response_description="Root")
def root():
   return {"Status": "Connected"}