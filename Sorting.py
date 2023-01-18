jo = [4,54,1,67,90,2,100,0]
#BUBBLE SORT >> O(N^2)
def bubblesort(arr):
    for x in range(len(arr)-1,0,-1):
        for i in range(x):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
#Call the function
bubblesort(jo)
print(jo)

#SELECTION SORT >> O(N^2)
def selectionsort(arr):
    for x in range(len(arr)):
        minpos = x
        for i in range(x,len(arr)):
            if arr[i]<arr[minpos]:
                minpos = i
        arr[x],arr[minpos]=arr[minpos],arr[x]
#Call Function
selectionsort(jo)
print(jo)

#INSERTION SORT >> O(N^2)
def insertionsort(arr):
    for i in range(1,len(arr)):
        j = i
        while arr[j-1] > arr[j] and j > 0:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j -= 1
#Call function
insertionsort(jo)
print(jo)

#MERGE SORT >> O(NLOGN)
def mergesort(arr):
    x = len(arr)
    if x > 1:
        leftarr = arr[ : x//2 ]
        rightarr = arr[x//2 : ]
        #recurison
        mergesort(leftarr)
        mergesort(rightarr)
        #merge
        i = 0 #leftarr index
        j = 0 #rightarr index
        k = 0 #merged arr index
        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                arr[k] = leftarr[i]
                i += 1
            else:
                arr[k] = rightarr[j]
                j += 1
            k += 1
        while i < len(leftarr):
            arr[k] = leftarr[i]
            i += 1
            k += 1
        while j < len(rightarr):
            arr[k] = rightarr[j]
            j += 1
            k += 1
#Call function
mergesort(jo)
print(jo)

#some sorting algo(IN PLACE SORTING)
def linearsort(nums):
    i = 0
    while i<len(nums):#find next smallest val
        min_index = i
        j = i+1
        while j < len(nums):
            if nums[j]<nums[min_index]:
                min_index = j
            j += 1
        if min_index != i: #swap if new minimum found
            nums[i],nums[min_index]=nums[min_index],nums[i]
        i += 1