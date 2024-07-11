#5.Write a program to search an element in the given array and print the searched elements index. If no such elements were found print -1
size=int(input())
key=int(input())
arr=[]
flag=0
for i in range(0,size):
    i=int(input())
    arr.append(i)
#print(arr)
for i in range(0,size):
    if(arr[i]==key):
        flag+=1
        break
    else:
        flag=0
if(flag==1):
    print(i)
else:
    print("-1")

