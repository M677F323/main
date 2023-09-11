from test_hello_main import hello


def  test_hello():
    assert hello("kin") == "Hello, kin"
def test_argument():
    assert hello() == "Hello, world"