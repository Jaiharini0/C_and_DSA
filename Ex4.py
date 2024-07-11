#4.Write a  Program to print all the repeated elements in a sorted array.
size=int(input())
arr=[]
for i in range(0,size):
    i=int(input())
    arr.append(i)
print(arr)
for i in range(0,size-1):
    for j in range(i+1,size):
        if arr[i]>arr[j]:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
print(arr)
for i in range(0,size-1):
    for j in range(i+1,size):
        if(arr[i]==arr[j]):
           print(arr[i])
        
