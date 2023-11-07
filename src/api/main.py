from fastapi import FastAPI
from utils import get_popular_words


app = FastAPI()


@app.get('/getWords')
def read_words():
    return get_popular_words()
