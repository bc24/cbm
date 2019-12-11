import random

def calc(v1, v2, func):
    return func(v1,v2)
print(calc(10,20,min))
print(calc(10,20,max))

def add (value1, value2):
    return value1 + value2
    
print(calc(10,20,add))
print(calc(10,random.random(),add))    