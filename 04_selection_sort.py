def selection_sort(arr):
    for i in range(len(arr)-1):
        min=i
        for j in range(i,len(arr)):
            if arr[j] < arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]
    return arr

arr=[5,4,2,9,8]
res=selection_sort(arr) 
print(res)