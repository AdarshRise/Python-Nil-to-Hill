# Variables
# As seen so far, we don't put data type for variables, it automatically judges the data type

a=10
b=10.0
c="10"
d='10'
e='''10'''
print(a,b,c,d,e)

# use type() for getting it's type
print(type(a),type(b),type(c),type(d),type(e))

# we can assign values like this also
a,b,c=10,20,30

#this could be used for exchange in 2 numbers
a,b=b,a
print(a,b)


#NOTE-: everything in python is an Object and belong to a class{ more on this later }

#--------------------------------

# variable are of 2 types, global and local

# global variable could be used through out the module{this python file}
# local variable could be used only within some certain bounds

x=10
def val(x):# x in this function will be treated as local
    print(x)
    
def val2():# x in this function will be treated as global x
    global x
    print(x)

def main():
    x=2
    val(x)
    val2()
    
if __name__=="__main__":
    main()
#---------------------------------
# python has many data types
# 1.Tuples
# 2.List
# 3.Dictonary
# 4.set
#---------------------------------
