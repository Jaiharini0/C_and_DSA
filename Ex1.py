#1.Write a program to accept N values into an integer array and display the contents of the array in the reverse order.
size=int(input())
arr=[]
for i in range(0,size):
    i=int(input())
    arr.append(i)
print(arr)
for i in range(size-1,-1,-1):
    print(arr[i],end=" ")
    
    
