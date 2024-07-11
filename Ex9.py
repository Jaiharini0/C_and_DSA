#9.Write a program  to insert the value at given position in the array.
size=int(input())
arr=[]
for i in range(0,size):
    i=int(input())
    arr.append(i)
print(arr)
position=int(input())
value=int(input())
arr.insert(position,value)
print(arr)
