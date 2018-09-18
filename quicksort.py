def quicksort(array):
    if len(array)<2:
        return array
    else:
        pivot=array[0]
        less= [i for i in array[1:] if i<=pivot]
        greater= [i for i in array[1:] if i>pivot]
        return quicksort(less)+[pivot]+quicksort(greater)

a=[3,8,5,0,3]
print(quicksort(a))