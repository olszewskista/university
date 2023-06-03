import random

with open('nazwiska.txt', 'r') as f:
    people = []
    for line in f:
        line = line.strip()
        parts = line.split()
        person = {'ilosc': int(parts[0]), 'nazwisko': parts[1]}
        people.append(person)

def hashD(s):
    h = 0
    for c in s:
        h += 111*ord(c)
    return h

proby = 0

class HashTable():
    def __init__(self, m):
        self.m = m
        self.table = [None for _ in range(m)]

    def __getitem__(self, i):
        return self.table[i]
    
    def __str__(self):
        return str(self.table)
    
    def len(self):
        l = 0
        for x in self.table:
            if x == None:
                pass
            elif x == 'DEL':
                pass
            else:
                l += 1
        return l
    
    def delCount(self):
        count = 0
        for x in self.table:
            if x == 'DEL': count += 1
        return count

    def insert(self, k, H):
        # wstawia klucz k do tablicy z haszowaniem T
        # wartość None w tablicy to miejsce wolne
        # wartość DEL w tablicy to miejsce po usuniętym elemencie
        i=0 #numer próby
        while True:
            global proby
            proby += 1
            j=H(k['nazwisko'] ,i)
            if self.table[j] == None or self.table[j] == "DEL":
                self.table[j]=k
                return j # wstawienie na znalezionej wolnej pozycji
            i=i+1
            if i == self.m: 
                print('błąd: brak miejsca')
                break # i = 0,1,2,...,m-1

    def search(self, k, H):
        # szuka klucza k w tablicy z haszowaniem T
        i=0
        while True:
            global proby
            proby += 1
            j=H(k['nazwisko'], i)
            if self.table[j] == k:
                return j # znaleziony szukany klucz
            i=i+1
            if self.table[j] == None or i == self.m:
                return None # None jako wynik oznacza, że nie znaleziono szukanego klucza

    def delete(self, j):
        # usuwa element z pozycji j w tablicy T
        # wpisując na tę pozycję znacznik DEL
        self.table[j]="DEL"

    def liniowe(self, k, i):
        return ((hashD(k) % self.m) + i) % self.m
    
    def kwadratowe(self, k, i):
        return ((hashD(k) % self.m) + i**2) % self.m
    
    def dwukrotne(self, k, i):
        return ((hashD(k) % self.m) + i * (1 + (hashD(k) % (self.m - 2)))) % self.m
    

w = 8009

# 1. Wstaw
def wstaw():
    global proby
    for wypelnienie in [0.5, 0.7, 0.9]:
        proby = 0
        tablica = HashTable(w)
        for x in range(0, int(w * wypelnienie)):
            tablica.insert(people[x], tablica.liniowe)
        srednia_prob = proby / w * wypelnienie
        print(f'srednia ilosc prob dla wypelnienia {wypelnienie} to: {srednia_prob}')

# wstaw()

# 2. Szukaj

def szukaj():
    global proby
    tablica2 = HashTable(w)
    for x in range(0, int(w * 0.8)):
        tablica2.insert(people[x], tablica2.liniowe)
    for s in range(int(w * 0.8) - 21, int(w * 0.8)):
        proby = 0
        tablica2.search(people[s], tablica2.liniowe)
        print(f'dla {people[s]} liczba prob to: {proby}')

# szukaj()

# 3. Usun
def usun():
    tablica3 = HashTable(w)
    for x in range(0, int(w * 0.8)):
        tablica3.insert(people[x], tablica3.liniowe)
    half_lenght = tablica3.len() // 2 

    while True:
        if half_lenght >= tablica3.len():
            break

        x = random.randint(0, w - 1)
        if tablica3[x] != None and tablica3[x] != 'DEL':
            tablica3.delete(x)

    while True:
        if tablica3.len() >= int(w * 0.8):
            break
        tablica3.insert(people[random.randint(0, len(people) - 1)], tablica3.liniowe)

    print(f"liczba 'del' to {tablica3.delCount()}")

usun()