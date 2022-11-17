#Day 2 coding Statement: Write a program to identify if the character is an alphabet or not.
a=input("Input:")
a=a.lower()
if (ord(a)>=97 and ord(a)<=122 ):
 print("The character is an Alphabet")
else:
 print("Not an Alphabet")    
    