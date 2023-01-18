jo = [4,54,1,67,90,2,100,0]
l = 90
#LINEAR SEARCH >> O(N)
def linearsearch(arr,n):
    m = 0
    while m <len(arr):
        if arr[m] == n:
            return True
        m = m + 1
    return False
#Call function
if linearsearch(jo,l):
    print("Found")
else:
    print("Not Found")

#BINARY SEARCH >> O(LogN)
def binarysearch(arr,n):
    l = 0
    u = len(arr)-1
    while l <= u:
        mid = (l+u)//2
        if arr[mid]==n:
            print("Found")
            return True
        else:
            if arr[mid]<n:
                l = mid + 1
            else:
                u = mid - 1
    return False
#Remember binary only holds sorted arr so we use a sort algo
def bubblesort(arr):
    for x in range(len(arr)-1,0,-1):
        for i in range(x):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
#Call function
bubblesort(jo)#so there's need to first sort
if binarysearch(jo,l):
    print("Found")
else:
    print("Not Found")
#jump search,finonacci search try them algo in other programs