import typing
from following import *

def main() -> None:
    x = int(input("Enter integer: "))
    y = int(input("Enter integer: "))
    print(following(x, y))

#in Python there is no default "main" function
#we need to indicate what to do if this file is run.
if __name__=="__main__": 
    main() 
