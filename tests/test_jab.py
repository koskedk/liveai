import logging
import pytest
from loguru import logger

from aide.jab import OllamaJab
from core.config import initialize_app_testing

ol = OllamaJab()


def test_get_models():
    mods = ol.get_models()
    assert len(mods) > 0


@pytest.mark.parametrize("model", [
    "llama3.2:latest",
    "deepseek-r1:7b",
    "phi4:latest"
])
def test_get_response(model):
    ol.ask("does it snow in Nairobi?", model)
    res = ol.get_response()
    assert res is not None
    logger.info(f"||| {model} |||")
    logger.info(res)
