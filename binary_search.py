
def binSearch(arr, key, begin, end):
    if key == arr[begin]:
        return begin
    elif key == arr[end]:
        return end
    elif begin == end:
        return -1
    elif key > arr[end] or key < arr[begin]:
        return -1
    else:
        if key > arr[ (end+begin) /2 - 1]:
            return binSearch(arr, key, (end+begin) /2, end)
        else:
            return binSearch(arr, key, begin, (end+begin) /2 -1 )


test = [0,1,2,3,4,5,6]
print "Index of the Key: ", binSearch(test, 4, 0, len(test)-1)
