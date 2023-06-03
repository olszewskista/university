import random

def lcsLength(x,y):
    m=len(x)
    n=len(y)
    c = [[0 for i in range(n+1)] # utworzenie tablic
        for j in range(m+1)] # i wypełnienie zerami
    b = [[0 for i in range(n+1)]
        for j in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]: # x[i-1] == y[j-1] przy
                c[i][j] = c[i-1][j-1] + 1 # indeksowaniu x,y od 0
                b[i][j] = "\\"
            else:
                if c[i-1][j] >= c[i][j - 1]:
                    c[i][j] = c[i-1][j]
                    b[i][j] = "|"
                else:
                    c[i][j] = c[i][j-1]
                    b[i][j] = "-"
    return c, b


def PrintLCS(x,b,i,j):
    if i==0 or j==0 :
        return
    if b[i][j] == "\\" :
        PrintLCS(x,b,i-1,j-1)
        print(x[i-1]) # x[i-1] przy indeksowaniu x,y od 0
    elif b[i][j] == "|":
        PrintLCS(x,b,i-1,j)
    else:
        PrintLCS(x,b,i,j-1)

def dlugoscNWP(x, y):
    m = len(x)
    n = len(y)

    # Inicjalizacja dwóch wierszy tablicy c
    prev_row = [0] * (n + 1)
    curr_row = [0] * (n + 1)
    for i in range(1, m + 1):
        # Przełączanie aktualnego wiersza i poprzedniego wiersza
        prev_row, curr_row = curr_row, prev_row

        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                curr_row[j] = prev_row[j - 1] + 1
            else:
                curr_row[j] = max(curr_row[j - 1], prev_row[j])

    # Zwracanie ostatniej wartości w ostatnim wierszu jako długość NWP
    return curr_row[n]

# 1.
x = "abcde"
y = "race"

c, b = lcsLength(x, y)
PrintLCS(x, b, len(x), len(y))

# 2.
print("Długość NWP:", dlugoscNWP(x, y))

# 3.
k = [2, 4, 8, 16]
n = [100, 500, 1000]
litery = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def z3():
    print("-" * 100)
    for dlugosc in n:
        print("Dla dlugosci slowa:", dlugosc)
        for znaki in k:
            slowo1 = ""
            slowo2 = ""
            for tworzenieSlowa in range(0, dlugosc):
                slowo1 += litery[random.randint(0, znaki-1)]
                slowo2 += litery[random.randint(0, znaki-1)]
            print("Dlugosc NWP to:", dlugoscNWP(slowo1, slowo2), "a iloraz to:", dlugoscNWP(slowo1, slowo2)/dlugosc, "  liczba znakow:", znaki)
        print("-" * 100)
z3()