import os
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return "wena Cabros"


if __name__ == '__main__':
    print("Wena cabros")
