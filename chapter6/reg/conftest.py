from pathlib import Path
from tempfile import TemporaryDirectory

import cards
import pytest


def db_scope(fixture_name, config) -> str:
    if config.getoption("--func-db", None):
        return "function"
    return "session"


def pytest_addoption(parser):
    parser.addoption(
        "--func-db",
        action="store_true",
        default=False,
        help="new db for each test"
    )


@pytest.fixture(scope=db_scope)
def db():
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)
        yield db
        db.close()


@pytest.fixture(scope='function')
def cards_db(db):
    db.delete_all()
    return db


@pytest.fixture(scope='session')
def some_cards():
    """List of different Card objects"""
    return [
        cards.Card("write book", "Brian", "done"),
        cards.Card("edit book", "Katie", "done"),
        cards.Card("write 2nd edition", "Brian", "todo"),
        cards.Card("edit 2nd edition", "Katie", "todo"),
    ]


@pytest.fixture(scope='function')
def non_empty_db(cards_db, some_cards):
    for card in some_cards:
        cards_db.add_card(card)
    return cards_db