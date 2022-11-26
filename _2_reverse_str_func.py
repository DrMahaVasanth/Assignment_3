#program to reverse a string
#Output:
#Enter any string:1234abcd
# The reversed string is dcba4321
org_str=input("Enter any string:")

def reverse(org_str):
    rev_str=""
    for i in org_str:
        a=org_str[-1]
        org_str=org_str[:-1]
        rev_str+=a
    return rev_str
print ("The reversed string is", reverse(org_str))
