def insertion_sort(arr):
    for i in range(1,len(arr)):
        j=i;
        while((arr[j-1]> arr[j]) and j > 0):
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
    return arr

arr=[3,2,5,6,4,1]
res=insertion_sort(arr)
print(res);
