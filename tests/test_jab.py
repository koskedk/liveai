from loguru import logger
import logging

logging.basicConfig(level=logging.DEBUG)

logging.info("staring,,,")
logging.debug("XX staring,,,")


def test_prompt():
    logging.debug(">>>>>>|||")
    assert True
