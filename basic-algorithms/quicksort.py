def quicksort(array):

    # empty arrary and the array with single element is already sorted
    if len(array) < 2:
        return array
    else:
        # take first element as pivot, and keep on swapping
        pivot = array[0]

        # if less than pivot then it'll swap left
        less = [i for i in array[1:] if i <= pivot]

         # if greater than pivot then it'll swap right
        greater = [i for i in array[1:] if i >= pivot]

        # re-run the function for less and greater plus the pivot to sort
        return quicksort(less) + [pivot] + quicksort(greater)
    



print(quicksort([2,3,5,1,4,8,2,9]))