#exceptions
'''
x =  int(input("what is x? "))
print(f'x is {x}')
''' 
'''
def return_value():
    while True:
        try :
            x =  int(input("what is x? "))    
        except ValueError:
            print("x is not integer")
            break
        else:
            print(f'x is {x}')
return_value()
'''
'''
def main():
    x = return_value("what is x? ")
    print(f'x is {x}')
def return_value(prompt):
    while True:
        try :
            x =  int(input(prompt))    
        except ValueError:
            print("x is not integer")
            break
main()
'''

def main():
    x = return_value("what is x? ")
    print(f'x is {x}')
def return_value(prompt):
    while True:
        try :
            return(int(input(prompt)))    
        except ValueError:
            pass
main()