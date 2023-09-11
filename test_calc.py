import sys
from calc import square
def main():
    test_square()

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
def test_square():
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
#here we nodded to use the  if condition
if __name__ == "__main__":
    main()
#if it is not right n+n    then AssertionError
