def left(i):
    return 2*i +1
def right(i):
    return 2*i+2
def parent(i):
    return(i-1)//2

def heapify(A, n, i):
    l = left(i)
    r = right(i)
    max_ind = i
    if l < n and A[l] > A[max_ind]:
        max_ind = l
    if r < n and A[r] > A[max_ind]:
        max_ind = r
    if max_ind != i:
        a = A[max_ind]
        b = A[i]
        A[max_ind] = b
        A[i] = a
        heapify(A, n, max_ind) 
        
def build_heap(A):
    n = len(A)
    for i in range (parent(n-1),-1,-1):
        heapify(A,n,i)
    return A

def heap_sort(A):
    n = len(A)
    build_heap(A)
    for i in range(n-1,0,-1):
        a = A[0]
        b = A[i]
        A[0] = b
        A[i] = a
        heapify(A,i,0)
    return A
A = [1,234,56,74,23,5,6,2,1,6,7,9]
print(heap_sort(A))