#here we are testing logiv not ***code or main_function** only logic N*N
from calc import square
""" def main():
    test_square() """

""" def test_square():
    if square(2)!=4:
        print("2 square was not 4")
    if square(3)!=9:
        print("3 square is not 9")
if __name__ == "__main__":
    main()
 """
# assert  mean make that true  like something is true  it raises errors  if it is false
#to  catch assertioon error
""" def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 square was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 square is not 9")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 square is not 9")   
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 square is not 4")  
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 square is not 0")  
#this is why pytest case so we no ndded to use these many line to test multiple lines
#unit test are tests for function that  you have written 

#here we nodded to use the  if condition
if __name__ == "__main__":
    main()
#if it is not right n+n    then AssertionError """
#pytest
#pip install pytest
from calc import square
def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2)  ==4
    assert square(-3)  == 9
    assert square(0)  == 0

#if we use n + n  the 
'''(base) veerasekhar@veeras-MacBook-Pro python_harvardx_cert % pytest test_calc.py
============================================ test session starts =============================================
platform darwin -- Python 3.11.4, pytest-7.4.0, pluggy-1.0.0
rootdir: /Users/veerasekhar/Desktop/cs50/python_harvardx_cert
plugins: anyio-3.5.0
collected 1 item                                                                                             

test_calc.py F                                                                                         [100%]

================================================== FAILURES ==================================================
________________________________________________ test_square _________________________________________________

    def test_square():
        assert square(2) == 4
>       assert square(3) == 9
E       assert 6 == 9
E        +  where 6 = square(3)

test_calc.py:49: AssertionError
========================================== short test summary info ===========================================
FAILED test_calc.py::test_square - assert 6 == 9
============================================= 1 failed in 0.09s =============================================='''

#check50 is like pytest by harvard