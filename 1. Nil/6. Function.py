# Creating Function

# function are created using def

def fun():
    print(" function got created ")


def fun2(x):
    print("value of x is :",x)

# a bit complex use of function

def fun3(x):
    x=x*x
    print("value of x*x is ",x)

# above code will execute from here

x=2
fun()
fun2(x)
fun3(x)
print(x) # the value of x is unaffected by fun3()

#--------------------------------------------------
#   Variable present in the function call are called -: Actual parameters
#   Variable present in the function defintion are called -: Formal parameters
#--------------------------------------------------
# passing parameter in functions

def par(x,y):       # function without default value of y
    print(" value of x ",x,"value of y ",y)

def par2(x,y=10):   # function with default value of y
    print(" value of x ",x," value of y ",y)

# this will execute the code above
x=3
y=4

par(x,y)    # passing 2 parameter to a function without default value
par2(x)     # passing 1 parameter to a function with a default value
par2(x,y)   # passing 2 parameter to a function with a default value
par2(y=50,x=90) # passing values in different order but with the names of Formal parameters

# code below is invalid    
#-----------------------
# def fun(x=10,y):
#   some code....
#-----------------------

#------------------------------------------------------------
# there is No exact main funtion, but we can make one

def main():
    print(" all the exectue statements should go here ")

if __name__="__main__": 
    main()

# the above code works as a sudo-main funtion in python, learn more about __name__



