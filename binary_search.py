def binarysearch(arr,x):
    low=0
    high=len(arr)-1
    mid=0

    while(low<=high):
        mid=(high+low)//2

        if(arr[mid]<x):
            low=mid+1

        elif(arr[mid]>x):
            high=mid-1

        else:
            return mid
    return -1

arr=[23,45,67,89,12]
x=int(input("enter a number"))
result=binarysearch(arr,x)
print(result)
if(result!=-1):
    print("the number is present in the index ",str(result))
else:
    print("number not present")
