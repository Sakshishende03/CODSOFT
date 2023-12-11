#passward_Genrator.py
import string #Modulo
import random

#main program
s1=string.ascii_lowercase
#print(s1)
s2=string.ascii_uppercase
#print(s2)
s3=string.digits
#print(s3)
s4=string.punctuation
#print(s4)
print("=================================================")
plen=int(input("\tEnter Passward length:"))
print("-----------------------------------")
s=[]#Emplty list
s.extend(s1) #adding the string data to emplty llist
s.extend(s2)
s.extend(s3)
s.extend(s4)
#print(s)
random.shuffle(s)
#print(s)
print("-----------------------------------")
print("\tYour passward is: {}".format("".join(s[0:plen])))
print("=================================================")


