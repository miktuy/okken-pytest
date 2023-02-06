import time
import pytest


@pytest.fixture(autouse=True, scope="session")
def footer_session_scope():
    """Report time at the end of session."""
    yield
    now = time.time()
    print("--")
    print(f"finished: {time.strftime('%d %b %X', time.localtime(now))}")


@pytest.fixture(autouse=True)
def footer_function_scope():
    """Report test duration after each use"""
    start = time.time()
    yield
    stop = time.time()
    delta = stop - start
    print(f"\ntest duration : {delta:0.3} seconds")


def test_1():
    time.sleep(1)


def test_2():
    time.sleep(1.23)