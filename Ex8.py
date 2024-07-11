#8.Write a program  to reverse the array elements
size=int(input())
arr=[]
for i in range(0,size):
    i=int(input())
    arr.append(i)
print(arr)
for i in range(size-1,-1,-1):
    print(arr[i],end=" ")
