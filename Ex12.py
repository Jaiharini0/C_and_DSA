#12.Write a program  to left rotate for given times of an array elements
size=int(input())
arr=[]
for i in range(0,size):
    i=int(input())
    arr.append(i)
print(arr)
time=int(input())
while(time>0):
    temp=arr[size-1]
    arr[size-1]=arr[0]
    for i in range(0,size-1):
        for j in range(i+1,i,-1):
            if(i==(size-2)):
                arr[size-2]=temp
                break
            else:
                arr[i]=arr[j]
    time-=1
print(arr)
