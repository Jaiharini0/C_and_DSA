#2.Write a  program to count the number of 0s and 1s in an array that is in random order. You may assume that the array consists of only 0s and 1s.
size=int(input())
arr=[]
count=0
for i in range(0,size):
    i=int(input())
    arr.append(i)
print(arr)
for i in range(0,size):
    if arr[i]==0:
        count+=1
print("0s:",count)
print("1s:",size-count)


        
