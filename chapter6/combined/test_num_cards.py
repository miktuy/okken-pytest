import pytest


@pytest.mark.num_cards(3)
def test_three_cards(cards_db):
    assert cards_db.count() == 3