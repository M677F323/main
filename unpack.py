def f(*args,**kwargs):
    #print("positional",args)
    print("named: " ,kwargs)

#f(10,29,89)
#f(12,23,2223,23,382)
#here we can pass any number of values
f(galleons=100,sickles=50,knuts=25)