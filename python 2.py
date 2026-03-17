# Day 2  python learning    
# Topic : Variables and Data Types in Python


# variables  
x=10 # int 
y=20  # int 
name= "nisarga"  # string 
print(x) # 10 
print(y) # 20
print(name) #nisarga 
print("x","+" ,"y") # x+y
print(x+y) # 30

# variable assigment
x , y, z=10,20,30
a=b=c=100
print(x,y,z) # 10 20 30
print(a, b, c) # 100 100 100

# variable naming rules 
AGE1=25
age=45
_age=55
print(AGE1) # 25
print(age) #45
print(_age) # 55 

# /age=50 # invalid variable name

name ="sunanda"
_name="thippeshappa"
print(name) # sunanda
print(_name) # thippeshappa

#7name="bbhhhs" # invalid variable name

name= "nisarga"# case sensitive
Name="nisha"
print(name) # nisarga
print(Name) # nisha

# data types
name="nisarga"# string  # built in data types in python 
age=20 # int 
is_student=True # bool
weight =49.5 # float 

# type checking type()
print(type(name)) # <class 'str'
print(type(age)) # <class 'int'>
print(type(is_student)) # <class 'bool'>
print(type(weight))# <class 'float'>
# va
is_student=3.0 # variable ressigment 
print(type(is_student)) # type checking  # <class 'float'>

age_float=float(age)
print(age_float)

s="100" # string 
print(s) # 100
print(type(s)) # <class 'str'>
v=int(s)# type coversion 
print(v)
print(type(v))

#age=30  # int
#n="nisha"   # string            
#  unsupported operand type(s) for +: 'int' and 'str'
#print(age+n)


age=30 
n="nisha"              
print(str(age)+n)
'''
name ="nishu" # string
print(type(name)) 
print(int(name))# ValueError: invalid literal for int() with base 10: 'nishu'
'''


# arthimetic opertors 
a=10
b=3
print(a+b) # addtion 
print(a-b)  #  subtraction 
print(a*b)  # multiplication 
print(a/b) # division 
print ( a//b) # floor division 
print(a%b)   # modulus 
print(a**b) # exponentional 

print(a*b ,+2 /2**3  % 6, a+b ,a-b ,a/b )


# swapping of variables
a=5
b=4
temp=a
a=b
b=temp 
print(a)
print(b)

# day 2 is done 
# swapping without temp variable


a=5   # extra mining of day 2
b=4
a,b=b,a
print(a)
print(b)    

Python Practice - Day 2
Topic

Variables and Data Types in Python

Description

This program demonstrates the use of variables, data types, type checking, type conversion, arithmetic operations, and swapping of variables in Python.

Concepts Covered

Variables and variable assignment

Variable naming rules

Data types (int, float, string, boolean)

Type checking using type()

Type conversion (int(), float(), str())

Arithmetic operators

Swapping variables (with and without temporary variable)

Example Code
x = 10
y = 20
name = "nisarga"

print(x + y)

age = 20
age_float = float(age)
print(age_float)

a = 5
b = 4
a, b = b, a
print(a, b)
Output

Demonstrates variable usage and operations

Shows different data types

Displays results of arithmetic operations

Swaps values of variables

Author

Nisarga M T

