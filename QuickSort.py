def quick_sort(A, p, r):
    while p < r:
        q = partition(A,p,r)
        quick_sort(A,p,q-1)
        p=q+1
    return A
        
def partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range (p,r):
        if A[j]<= x:
            i+=1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return i+1

A = [1,5,4,6,4,2,3,1,2,0,3]

print(quick_sort(A,0,len(A)-1))