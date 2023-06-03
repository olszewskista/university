from timeit import default_timer as timer
import random
import sys

sys.setrecursionlimit(100000)

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

def InsertionSort(A):
    n = len(A)
    for j in range (1,n):
        pom=A[j]
        i=j-1
        while i>=0 and A[i]>pom:
            A[i+1]=A[i]
            i=i-1
        A[i+1]=pom

def quickSort(A,p,r):
    if p<r :
        q = partition(A,p,r)
        quickSort(A,p,q)
        quickSort(A,q+1,r)

def quickSortZmodyfikowany(A,p,r,c):
    if p<r:
        if c > r-p+1:
            return
        else:
            q = partition(A,p,r)
            quickSortZmodyfikowany(A,p,q,c)
            quickSortZmodyfikowany(A,q+1,r,c)


wielkosci = [1000,5000,10000,15000, random.randint(0,15000)]

def testyLosowe():
    for a in wielkosci:
        tablica = random.sample(range(100000),a)
        tablica2= tablica.copy()

        start = timer()
        # print(tablica)
        quickSortZmodyfikowany(tablica,0,len(tablica)-1,6)
        # print(tablica)
        InsertionSort(tablica)
        # print(tablica)
        stop = timer()
        time = stop-start
        print(f'{time} to czas wykonania dla tablicy o wielkosci {a} quicksorta zmodyfikowanego')

        start2 = timer()
        # print(tablica2)
        quickSort(tablica2,0,len(tablica2)-1)
        # print(tablica2)
        stop2 = timer()
        time2 = stop2-start2
        print(f'{time2} to czas wykonania dla tablicy o wielkosci {a} quicksorta zwyklego')

def testyNiekorzystne():
    for a in wielkosci:
        tablica = random.sample(range(1000000),a)
        tablica.sort()
        tablica2= tablica.copy()

        start = timer()
        # print(tablica)
        quickSortZmodyfikowany(tablica,0,len(tablica)-1,10)
        InsertionSort(tablica)
        # print(tablica)
        stop = timer()
        time = stop-start
        print(f'{time} to czas wykonania dla tablicy o wielkosci {a} quicksorta zmodyfikowanego')

        start2 = timer()
        # print(tablica2)
        quickSort(tablica2,0,len(tablica2)-1)
        # print(tablica2)
        stop2 = timer()
        time2 = stop2-start2
        print(f'{time2} to czas wykonania dla tablicy o wielkosci {a} quicksorta zwyklego')

testyLosowe()
# testyNiekorzystne()

# Czasy losowe:
# 0.0014024999982211739 to czas wykonania dla tablicy o wielkosci 1000 quicksorta zmodyfikowanego
# 0.0016350000005331822 to czas wykonania dla tablicy o wielkosci 1000 quicksorta zwyklego
# 0.01025360000130604 to czas wykonania dla tablicy o wielkosci 5000 quicksorta zmodyfikowanego
# 0.010996299999533221 to czas wykonania dla tablicy o wielkosci 5000 quicksorta zwyklego
# 0.021643700001732213 to czas wykonania dla tablicy o wielkosci 10000 quicksorta zmodyfikowanego
# 0.02373230000011972 to czas wykonania dla tablicy o wielkosci 10000 quicksorta zwyklego
# 0.033723799999279436 to czas wykonania dla tablicy o wielkosci 15000 quicksorta zmodyfikowanego
# 0.03675130000192439 to czas wykonania dla tablicy o wielkosci 15000 quicksorta zwyklego

# Czasy niekorzystne:
# 0.04673960000218358 to czas wykonania dla tablicy o wielkosci 1000 quicksorta zmodyfikowanego
# 0.0457088000002841 to czas wykonania dla tablicy o wielkosci 1000 quicksorta zwyklego
# 1.2465706000002683 to czas wykonania dla tablicy o wielkosci 5000 quicksorta zmodyfikowanego
# 1.1530086999991909 to czas wykonania dla tablicy o wielkosci 5000 quicksorta zwyklego
# 4.786388999997143 to czas wykonania dla tablicy o wielkosci 10000 quicksorta zmodyfikowanego
# 4.710259700001188 to czas wykonania dla tablicy o wielkosci 10000 quicksorta zwyklego
# 11.02269040000101 to czas wykonania dla tablicy o wielkosci 15000 quicksorta zmodyfikowanego
# 10.987493300002825 to czas wykonania dla tablicy o wielkosci 15000 quicksorta zwyklego