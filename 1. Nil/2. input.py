# input takes input from user

# taking name of the user and printing it
name=input()
print(name)

# giving a message for better understanding
name=input(" Enter your Name :")
print(name)

# taking integer input
num=int(input(" Enter a number "))
print(num)
# by default, input() takes everythin in string

# taking float input
num=float(input(" Enter a number "))
print(num)

# taking either of int and float depending on the value
num=eval(input(" Enter a number "))
print(num)
#eval means evalutaion, It would handle both int and float value
#### warning### eval can't accept numbers starting with 0 , e.g 012 , 033, 007
