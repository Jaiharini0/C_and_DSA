#10.Write a program  to delete the value at given position from the array.
size=int(input())
arr=[]
for i in range(0,size):
    i=int(input())
    arr.append(i)
print(arr)
position=int(input())
#value=int(input())
arr.pop(position) #remove deletes the value and pop deletes at specific index 
print(arr)
