from test_hello_main import hello


def  test_hello():
    assert hello("kin") == "Hello, kin"
def test_argument():
    assert hello() == "Hello, world"

'''(base) veerasekhar@veeras-MacBook-Pro python_harvardx_cert % python test_hello_main.py
whats is your name? 
Hello, 
(base) veerasekhar@veeras-MacBook-Pro python_harvardx_cert % pytest test_Hello.py     
============================================ test session starts =============================================
platform darwin -- Python 3.11.4, pytest-7.4.0, pluggy-1.0.0
rootdir: /Users/veerasekhar/Desktop/cs50/python_harvardx_cert
plugins: anyio-3.5.0
collected 2 items                                                                                            

test_Hello.py ..                                                                                       [100%]

============================================= 2 passed in 0.01s ==============================================
'''
#if we write them in loops again we need tests for test that will be complicatedcode