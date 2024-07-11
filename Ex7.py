#7.Write a program  to replace every element in an array with the sum of its right side elements
size=int(input())
arr=[]
tot=0
for i in range(0,size):
    i=int(input())
    arr.append(i)
print(arr)
for i in range(0,size):
    tot+=arr[i]
for i in range(0,len(arr)):
    tot-=arr[i]
    arr[i]=tot
print(arr)
