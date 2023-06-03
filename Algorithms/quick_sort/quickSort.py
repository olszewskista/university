def partition(A,p,r):
    x=A[r] # element wyznaczajacy podział
    i=p-1
    for j in range (p, r+1):
        if A[j]<=x :
            i=i+1
            A[i], A[j] = A[j], A[i]
    if i<r :
        return i
    else:
        return i-1


def quickSort(A,p,r):
    if p<r :
        q = partition(A,p,r)
        quickSort(A,p,q)
        quickSort(A,q+1,r)


tablica = [9,6,1,4,5,2,7]

print(tablica)
quickSort(tablica,0,len(tablica)-1)
print(tablica)