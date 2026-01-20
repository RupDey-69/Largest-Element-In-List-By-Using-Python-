#predefine

# list1=[1,2,3,4,56,6]
# list2=max(list1)
# print("The Larger Elemnet is:",list2)


#user Define 

n=int(input("Enter the Size List : "))
num=[]
for i in range (n):
    element=int(input("Enter the number:"))
    num.append(element)


max_number=max(num)
print("The List Is :",num)
print("The Largest Element is:",max_number)