def left(i):
    return (2*i + 1)

def right(i):
    return (2*i + 2)

def parent(i):
    return (i/2)

def max_heapify(test, i):
    l = left(i)
    r = right(i)
    
    if(l < len(test) and test[i] < test[l]):
        largest = l
    else:
        l = 0
        largest = i

    if(r < len(test) and test[largest] < test[r]):
        largest = r
    else:
        r = 0

    if(largest != i):
        temp = test[i]
        test[i] = test[largest]
        test[largest] = temp
        max_heapify(test, largest)

def build_max_heap(test):
    for i in range (len(test)/2, -1, -1):
        max_heapify(test, i)

def heapsort(test):
    for i in range(len(test)-1, 0, -1):
        temp = test[0]
        test[0] = test[i]
        test[i] = -100000000
        ans.append(temp)
        max_heapify(test, 0)

    ans.append(test[0])

test = [1,4,5,2,3,8,7]
ans = []
print "Input: " + str(test)
build_max_heap(test)
heapsort(test)
print "Sorted: " + str(ans)
