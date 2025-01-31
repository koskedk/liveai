import pytest
import os
from loguru import logger

from core.config import initialize_app_testing

os.environ['MODE'] = 'testing'


def pytest_configure():
    initialize_app_testing()


@pytest.fixture(autouse=True)
def log_test(request):
    logger.info(f"start {request.node.name}...")
    yield
    logger.info(f"end {request.node.name}")
