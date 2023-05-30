def partition(l, low, high):
    pivot = l[high]
    i = low-1
    for j in range(low, high):
        if l[j] < pivot:
            i += 1
            # swap l[i], l[j]
            (l[i], l[j]) = (l[j], l[i])
    (l[i+1], l[high]) = (l[high], l[i+1])


    return i+1


def quickSort(l, low, high):
    if low < high:
        pi = partition(l, low, high)

        quickSort(l, low, pi-1)
        quickSort(l, pi+1, high)




if __name__ == "__main__":
    l = [int(i) for i in input().split()]
    quickSort(l, 0, len(l)-1)
    print(*l)

