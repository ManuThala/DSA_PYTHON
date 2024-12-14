def binary_search(arr,element):
    low,high=0,len(arr)-1;
    while(low<=high):
        mid=(low+high)//2
        if element==arr[mid]:
            return mid
        elif element>arr[mid]:
            low=mid+1
        else:
            high=mid-1
    return -1

arr=[4,5,6,8,9];
element=int(input('enter element to search:'))
res=binary_search(arr,element)
if res==-1:
    print('element not found')  
else:
    print('element found at index',res)
