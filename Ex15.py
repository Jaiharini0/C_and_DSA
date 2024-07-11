#15.Write a program  to find second largest and second smallest in array
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
print("Second largest:",arr[size-2])
print("Second smallest:",arr[1])
