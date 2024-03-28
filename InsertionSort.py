def insertion_sort(A):
    n = len(A)
    if n <= 1:
        return A
    for i in range(1,n):
        key = A[i]
        j = i-1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -=1
        A[j+1] = key
    return A

A = [2,3,5,7,2,30,64,12,44,67,3,1,2,3,0,6,54]
print(insertion_sort(A))
