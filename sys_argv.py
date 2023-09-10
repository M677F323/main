import sys
# print form input
""" print("My name is ", sys.argv[1]) """
#one more method
if len(sys.argv) < 2:
    print("too few arguments")
elif len(sys.argv) >2:
    print("too many argumens")
else:
    print("My name is ", sys.argv[1])

#lets see few more methos
if len(sys.argv) < 2:
    print("too few arguments")
elif len(sys.argv) >2:
    print("too many argumens")
#if we give it will come but if we dont give the input leads to error to overcome this 
#print("My name is ", sys.argv[1])


if len(sys.argv) < 2:
    sys.exit("too few arguments")
elif len(sys.argv) >2:
    sys.exit("too many argumens")
#if we give it will come but if we dont give the input leads to error to overcome this 
print("My name is ", sys.argv[1])

""" import sys
if len(sys.argv) < 2:
    print("too few")
for arg in sys.argv:
    print("hello my name is :", arg)#this also print the file name to over come this """
 #we use slice
import sys
if len(sys.argv) < 2:
    print("too few")
for arg in sys.argv[1:]:#one to end
    print("hello my name is :", arg)#this also print the file name to over come this
 