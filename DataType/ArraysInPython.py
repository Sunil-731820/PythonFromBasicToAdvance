import  array as arr
a = arr.array('i',[1,2,3,4,5,6])
print("the array is ")
print(a)
print("the new array is ")
for i in range(0,3):
    print(a[i] , end=" ")
print("creating the array of decimal values")

b = arr.array('d',[1.3,2.3,4.5])
print("the array is ")
print(b)
for i in range(0,3):
    print(b[i] , end=" ")

