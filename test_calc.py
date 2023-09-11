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
def test_square():
    assert square(2) == 4
    assert square(3) == 9
#here we nodded to use the  if condition
if __name__ == "__main__":
    main()
#if it is not right n+n    then AssertionError