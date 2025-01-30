import os

from core.config import Config, initialize_app_testing


cfg = Config()


def test_load_settings():
    cfg.load_settings("testing")
    assert os.getenv("MODE") == "testing"


def test_initialize_app_testing():
    initialize_app_testing()
    assert os.getenv("MODE") == "testing"
