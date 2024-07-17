from flask import Flask
import os

app = Flask(__name__)

@app.get("/")
def home():
    str_out = "This is {} server : {}".format(os.getenv("ENV"),os.getenv("VER"))
    return str_out

@app.get("/hello")
def hello():
    str_out = "This is hello route {} server : {}".format(os.getenv("ENV"),os.getenv("VER"))
    return str_out

app.run()
