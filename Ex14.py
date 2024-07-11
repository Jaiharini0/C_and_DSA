#14.Write a program  to remove the duplicates in an array .
size=int(input())
arr=[]
for i in range(0,size):
    i=int(input())
    arr.append(i)
print(arr)
for i in range(0,size-1):
    for j in range(i+1,size):
        if(arr[i]==arr[j]):
            arr.remove(arr[j])
print(arr)

#doubt

