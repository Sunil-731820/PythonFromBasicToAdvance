num = int(input("Enter the limit of the Number"))
list1 = []
for i in range(num):
    input1 = int(input("Enter the element in the list "))
    list1.append(input1)
print("the list of the element is ")
print(list1)
sum = 0
#its time to find the sum of the list of the Number is
# for i in range(len(list1)):
#     sum = sum + list1[i]
for  x in list1:
    sum = sum + x
print("the sum of the element is " , sum)

