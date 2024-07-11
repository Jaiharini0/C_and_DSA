#14.Write a program  to remove the duplicates in an array .
size=int(input())
arr=[]
for i in range(0,size):
    i=int(input())
    arr.append(i)
print(arr)
empty=[]
empty=arr
for i in range(0,size-1):
    for j in range(i+1,size):
        if(arr[i]==arr[j]):
            del(arr[i])
            
print(empty)
