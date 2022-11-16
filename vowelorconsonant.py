#Codingstatement1
#Take an input from the user and check if it is vowel or constant
#if user inputs a number, output should be invalid input
vc=input("Input:")
vc=vc.lower()
if(ord(vc)>=97 and ord(vc)<=122):
    if (vc=='a' or vc=='e' or vc=='i' or vc=='o' or vc=='u'):
        print("Vowel")
    else:
        print("Consonant")
else:
 print("Invalid input")        