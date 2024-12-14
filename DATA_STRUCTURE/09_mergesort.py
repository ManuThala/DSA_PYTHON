def merge_sort(my_list):
    if len(my_list)==1:
        return my_list
    mid_index=len(my_list)//2
    left=merge_sort(my_list[:mid_index])
    right=merge_sort(my_list[mid_index:])

    return merge(left,right)



def merge(list1,list2):
    combined=[]
    i,j=0,0;
    while(i < len(list1) and j < len(list2)):
        if list1[i]< list2[j]:
            combined.append(list1[i])
            i+=1
        else:
            combined.append(list2[j])
            j+=1
    while i < len(list1):
        combined.append(list1[i])
        i+=1
    while j < len(list2):
        combined.append(list2[j])
        j+=1
    return combined

my_list=[1,2,7,8,3,4,5,6]
sorted_list=merge_sort(my_list)
print('Sorted list is :',sorted_list)