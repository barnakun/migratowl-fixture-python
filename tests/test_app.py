from app.db import answer
from app.http import build_request
from app.settings import Settings


def test_settings() -> None:
    assert Settings().app_name == "fixture"


def test_db() -> None:
    assert answer() == 42


def test_http() -> None:
    assert build_request("https://example.com").url == "https://example.com/?q=x"
