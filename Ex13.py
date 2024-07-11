#13.Given an array X with n number of elements, return true if the given array X is sorted else return false. You may consider multiple positions may be shifted in the array X. 
size=int(input())
arr=[]
flag=0
for i in range(0,size):
    i=int(input())
    arr.append(i)
print(arr)
for i in range(0,size-1):
    for j in range(i+1,size):
        if(arr[i]<arr[j]):
            flag+=1
        else:
            flag=0
if(flag==(size-1)):
    print("true")
else:
    print("false")
