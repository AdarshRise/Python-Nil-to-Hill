# Boolean

# eg of True in variable
fast=True
slow=True
if(fast):
    print(" it is fast")

if (slow):
    print(" it is slow")

# eg of False in variable

sleeping=False 
running=False

if(sleeping):
    print(" is sleeping ")
else:
    print(" is not sleeping ")

if(running):
    print(" is running ")
else:
    print(" is not running ")

# variable assinged as 0 is equal to false
x=0
if(x):
    print(" is True")
else:
    print(" is False")

# variable assinged as anything other than 0 is True
a1=1
a2=2
a3=100
a4=-1
a5=-2
a6=-100
if(a1 and a2 and a3 and a4 and a5 and a6):
    print(" these all are True ")
else:
    print(" one was false ")

# numbers and boolean

x=1+True
print(x) # True is treated as 1
x=1+False
print(x) # False is treated as 0
x=False+True
print(x) # result is 1
