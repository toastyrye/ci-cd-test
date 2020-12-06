"""Hello world printer"""


def hello(option: str) -> str:
    """Return hello statement

    :param option:
    :return:
    """

    statement = "hello " + option  # TODO change this line to test coverage
    return statement


if __name__ == "__main__":
    world = "world"
    print(hello(world))
