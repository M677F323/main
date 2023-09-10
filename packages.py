#packages are third party libraries
#we use pip to install them 
#Eg:cowsay 
#pip install cowsay in cmd
import sys
import cowsay

if len(sys.argv) == 2:
    cowsay.cow("hello ,"+sys.argv[1])  #+sys.argv[1] imp
if len(sys.argv) == 2:
    cowsay.trex("hello ,"+sys.argv[1])