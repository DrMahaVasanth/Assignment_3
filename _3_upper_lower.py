#program to count the lowercase and uppercase letters in a string
#Entered original string is The quick Brow Fox
#Number of uppercase characters: 3
#Number of lowercase characters: 12
#org_str=input("Enter any string:")

org_str=input("Enter a string:")

def count(org_str):
    global u,l
    u,l=0,0
    for data in org_str:
        if data.islower():
            l+=1
        elif data.isupper():
            u+=1
    return l,u     
count(org_str)
print("Entered original string is",org_str)
print("Number of uppercase characters:",u,"\nNumber of lowercase characters:",l) 
  
