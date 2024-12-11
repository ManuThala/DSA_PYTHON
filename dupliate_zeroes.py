def duplicate_zeros(arr): 
        i,j=0,len(arr);
        while(i<j):
            if arr[i]==0:
                arr.insert(i+1,0);
                arr.pop();
                i+=1
            i+=1
arr1 = [1, 0, 2, 3, 0, 4, 5, 0]
duplicate_zeros(arr1)
print(arr1)