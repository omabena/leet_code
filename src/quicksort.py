def quicksort(L):
    return sort(L, 0, len(L)-1)

def sort(L, start, end):
    if start < end:
        index = partition(L, start, end)
        sort(L, start, index - 1)
        sort(L, index + 1, end)
    return L

def partition(L, start, end):
    pivot = L[end]
    index = start
    current = start
    while(current < end):
        if L[current] <= pivot: 
            L[index], L[current] = L[current], L[index]
            index += 1
        current += 1
    L[index], L[end] = L[end], L[index]
    return index 
    

L = [11, 16, 2, 8, 1, 9, 4, 7]
ordered_list = quicksort(L)
print(ordered_list)


L = [11, 16, 2, 8, 5, 29, 1, 60, 9, 4, 7, 34]
ordered_list = quicksort(L)
print(ordered_list)
