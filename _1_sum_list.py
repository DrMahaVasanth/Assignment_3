#Program to sum all the numbers in a list
size=int(input("Enter the size of the list to be entered: "))
lst=[]
for i in range(size):
    num=int(input("Enter the number:"))
    lst.append(num)
print("Created list of entered numbers: ", lst)
def find_sum():
    global result
    result=0
    for num in lst:
        result+=num
    return result
find_sum()
print("The sum of all numbers in the list is", result)

