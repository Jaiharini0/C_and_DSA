#11.Write a program  to swap every pair of  adjacent array elements
size=int(input())
arr=[]
for i in range(0,size):
    i=int(input())
    arr.append(i)
print(arr)
for i in range(0,size-1,2):
    for j in range(i+1,i,-1):
        temp=arr[i]
        arr[i]=arr[j]
        arr[j]=temp
print(arr)
