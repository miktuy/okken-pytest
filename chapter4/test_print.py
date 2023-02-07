def test_disabled(capsys):
    with capsys.disabled():
        print("\ncapsys disabled print")