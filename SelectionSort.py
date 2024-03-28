def selection_sort(A):
    for i in range((len(A))):
        min_ind = i
        for j in range(i+1, len(A)):
            if A[j] < A[min_ind]:
                min_ind = j
        (A[i], A[min_ind]) = (A[min_ind],A[i])
    return A

A = [2,1,3,4,2,5,6,8,53,2,4,6,10]
print(selection_sort(A))