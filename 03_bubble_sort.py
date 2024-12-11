def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(0,len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    return arr

arr=[4,5,2,1,8,9]
res=bubble_sort(arr)
print(res)