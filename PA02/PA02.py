def partition_first(A, l, r):
    p=arr[l]
    i=l+1
    for j in  range(l+1, r+1):
        if A[j]<p:
            k=A[j] 
            A[j]=A[i]
            A[i]=k
            i=i+1       
    k=A[i-1]
    A[i-1]=p 
    A[l]=k  
    return i-1

def partition_last(A, l, r):
    A[l],A[r]=A[r], A[l]
    p=arr[l]
    i=l+1
    for j in  range(l+1, r+1):
        if A[j]<p:
            k=A[j] 
            A[j]=A[i]
            A[i]=k
            i=i+1       
    k=A[i-1]
    A[i-1]=p 
    A[l]=k  
    return i-1

def partition_median(A, l, r):
    mid=(r+l)//2
    if A[l] < A[mid] < A[r] or A[r] < A[mid] < A[l]:
        A[l], A[mid] = A[mid], A[l]
    elif A[mid] < A[r] < A[l] or A[l] < A[r] < A[mid]:
        A[l], A[r] = A[r], A[l]
    p=arr[l]
    i=l+1
    for j in  range(l+1, r+1):
        if A[j]<p:
            k=A[j] 
            A[j]=A[i]
            A[i]=k
            i=i+1       
    k=A[i-1]
    A[i-1]=p 
    A[l]=k  
    return i-1

def quick_sort(arr,l,r):
    if l>r:
        return 0    
    cn=len(arr[l:r])
    div= partition_last(arr,l,r)
    cn=cn+quick_sort(arr,l, div-1)
    cn=cn+quick_sort(arr,div+1,r)  
    return cn


with open('C:\Algorithms_1\PA02\QuickSort.txt') as f:
    arr = list(map(int, (line for line in f)))
print (quick_sort(arr, 0, len(arr)-1))

 