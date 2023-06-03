def heapify(A, heapSize, i):
    koniec = False
    while not koniec:
        l = 2*i+1 # lewy syn
        r = 2*i+2 # prawy syn
        if l < heapSize and A[l] > A[i]:
            largest = l
        else:
            largest = i
        if r < heapSize and A[r] > A[largest]:
            largest = r
        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            i = largest
        else:
            koniec = True

def buildHeap(A):
    heapSize = len(A)
    k = int((len(A)-2)/2) # ojciec ostatniego węzła
    for i in range(k, -1, -1):
        heapify(A, heapSize, i)
    return A

def heapSort(A):
    A = buildHeap(A)
    heapSize = len(A)
    for i in range(len(A)-1, 0, -1):
        A[0], A[heapSize-1] = A[heapSize-1], A[0]
        heapSize -= 1
        heapify(A,heapSize,0)
    return A


with open('input.txt', 'r') as file:
    tablica = []
    litery = file.read().split('\n')
    for x in litery:
        tablica.append(int(x))

print(tablica)
heapSort(tablica)
print(tablica)

with open('output.txt', 'w') as file:
    for x in tablica:
        file.write(str(x)+'\n')