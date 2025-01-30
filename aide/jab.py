import os
from abc import ABC, abstractmethod

from loguru import logger
from ollama import ChatResponse, Client


class Jab(ABC):
    @abstractmethod
    def get_response(self):
        pass


class OllamaJab(Jab):
    def __init__(self):
        self.api = os.getenv("CHAT")
        self.model = os.getenv("MODEL")
        self.question = None
        try:
            logger.info("initializing...")
            logger.info("********************************")
            logger.info(f"api :{self.api}")
            logger.info(f"model :{self.model}")
            logger.info("********************************")
        except Exception as e:
            logger.error(e)
            raise

    def ask(self, question: str, model: str = None):
        self.question = question
        if model:
            self.model = model

    def get_response(self):
        logger.info("asking...")
        logger.info("********************************")
        logger.info("jab > {self.question}")
        logger.info("********************************")
        self.client = Client(host=self.api)
        res: ChatResponse = self.client.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": self.question,
                }
            ],
        )

        return res.message.content
