# Making choices with If else
x=4

# x equal to desire number
if x==4:
    print(" it was equal ")
else:
    print(" it was not equal ")
    
# x greater than desire number

if (x>4):
    print(" x is  more than 4 ")
else:
    print(" x is not more than 4 " )

# x less than desire number
if(x<4):
    print(" x is lower ")
else:
    print(" x is greater ")

# x not equal to desire number

if (x!=4):
    print(" x is not 4")
else:
    print(" x is 4 ")

# using && and , || or , != is not , == is

if x is not 4: # x!=4
    print(" x not 4")
else:
    print(" x is 4 ")

if x is 4:  # x==4
    print("yes")
else:
    print("not")

if x >0 and x==4: # x>0 && x==4
    print(" x is postive and equal to 4")
else:
    print(" either it's not positive or not equal to 4")

if x>0 or x==4: # x>0 || x==4
    print(" x is either postive or equal to 4 ")
else:
    print( "x is not postive and neither 4 ")

# nesting of if and else
if (x==4):
    print(" x is 4 ")
else:
    if(x>4):
        print(" x is greater than 4 ")
    else:
        if (x<4):
            print(" x is smaller than 4")
        else:
            print(" x is positive probably")

# nesting if else , using elif
if (x==4):
    print(" x is 4 ")
elif(x>4):
    print(" x is greater than 4 ")
elif (x<4):
    print(" x is smaller than 4")
else:
    print(" x is positive probably")        
        
    

    
    
