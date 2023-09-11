def main():
    name = input("whats is your name? ")
    #here we are printing
    print(hello(name))

def hello(to="world"):
    #this is printing not returning so unable to test
    #print("Hello ",name)
    return f"Hello, {to}"

if __name__ == "__main__":
    main()

"""(base) veerasekhar@veeras-MacBook-Pro python_harvardx_cert % python  test_hello_main.py
whats is your name? veera
Hello, veera"""