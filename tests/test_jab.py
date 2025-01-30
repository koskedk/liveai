import logging

from loguru import logger

from aide.jab import OllamaJab
from core.config import initialize_app_testing


ol = OllamaJab()


def test_get_response():
    ol.ask("does it snow in Nairobi?")
    res = ol.get_response()
    assert res is not None
    logger.info(res)
