#3. Write a  program to print the count of the elements in an array whose values are lesser than a key element in an unsorted array.
size=int(input())
key=int(input())
arr=[]
count=0
for i in range(0,size):
    i=int(input())
    arr.append(i)
print(arr)
for i in range(0,size):
    if arr[i]<key:
        count+=1
print(count)
