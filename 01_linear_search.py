def liner_search(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return  i
    return -1

arr=[4,3,5,7,9,1]
key=int(input('Enter a element to search:'))
res=liner_search(arr,key)
if res!=-1:
    print('the element present at index:',res)
else:
    print('Element not Found')
    
