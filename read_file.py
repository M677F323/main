""" with open("names.txt","r") as file:
#readlines from file and store on lines
    lines = file.readlines()
for line in lines:
    #print("hello,",line)
    print("Hello,",line.strip()) """


#we can also write as 
#this can directly read line from file
with open("names.txt","r") as file:
    for line in file:
        print("hello,", line.rstrip())