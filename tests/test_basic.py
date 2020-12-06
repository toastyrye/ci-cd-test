from hello_world.hello_world import hello


def test_hello() -> None:
    assert hello("world") == "hello world"


def test_true() -> None:
    assert 1 == 1
