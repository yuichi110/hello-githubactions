import main


def test_get_hello():
    message = main.get_hello()
    assert "hello" == message
