from fastapi import FastAPI

from titanic.app.jack_service import JackService

app = FastAPI(title="Titanic (James)")

class JamesController:
    def __init__(self):
        self.jack = JackService()