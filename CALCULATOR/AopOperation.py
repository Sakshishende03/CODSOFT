#AopOperation.py
def readvalues(op):
    print("Enter Two Values For {} Operation".format(op))
    a,b=float(input("Enter value of a:")),float(input("Enter Value of b:"))
    return a,b

def addop():
    a,b=readvalues("Addtion")
    print("sum({},{})={}".format(a,b,a+b))

def subop():
    a,b=readvalues("Subtraction")
    print("substraction({},{})={}".format(a,b,a-b))

def mulop():
    a,b=readvalues("Multiplication")
    print("mutiplication({}.{})={}".format(a,b,a*b))

def divop():
    a,b=readvalues("Division")
    print("division({},{})={}".format(a,b,a/b))

def moddiv():
    a,b=readvalues("Modulo Divivsion")
    print("modulo division({},{}) = {}".format(a,b,a%b))

def Frdivop():
    a,b=readvalues("Floor Division")
    print("floor division({},{})={}".format(a,b,a//b))

def Expop():
    a,b=float(input("Enter Base:")),float(input("Enter power:"))
    print("exponentiation({},{})={}".format(a,b,a**b))



