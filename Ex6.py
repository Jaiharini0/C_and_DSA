#6.You are given an array of 0s and 1s in random order. Segregate 0s on left side and 1s on right side of the array .
size=int(input())
arr=[]
for i in range(0,size):
    i=int(input())
    arr.append(i)
print(arr)
for i in range(0,size-1):
    for j in range(i+1,size):
        if(arr[i]==1):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
print(arr)
