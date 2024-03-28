def MergeSort(A):
    if len(A) > 1:
        middle = len(A)//2
        L = A[:middle]
        R = A[middle:]
        MergeSort(L)
        MergeSort(R)
        i = 0
        j = 0 
        k = 0
        while (i < (len(L)) and j < len(R)):
            if L[i] <= R[j]:
                A[k] = L[i]
                i+=1
            else:
                A[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1
    return A

A = [2,3,4,6,7,4,2,1,3,4,6,7,8,88,12,9,9,94]

MergeSort(A)
print(A)
			