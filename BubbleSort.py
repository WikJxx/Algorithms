def bubble_sort(A):
    for i in range (len(A)):
        for j in range (0, len(A)-i-1):
            if A[j]>A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A

A = [1,4,3,5,2,4,3,8,6,3,2,9,0]
print(bubble_sort(A))

