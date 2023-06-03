# funkcje hashujace
def hashD(s):
    h = 0
    for c in s:
        h += 111*ord(c)
    return h

def hashS(s):
    return ord(s[0])

# tablica hash
class HashTable:
    def __init__(self, m):
        self.m = m
        self.table = [[] for _ in range(m)]
        
    def add(self, key, h = hash):
        i = h(key) % self.m
        self.table[i].append(key)
        
    def hash(self, key):
        return hash(key) % self.m
        
    def __str__(self):
        return str(self.table)
    
    def __getitem__(self, i):
        return self.table[i]
    
    def empty(self):
        result = 0
        for x in self.table:
            if len(x) == 0:
                result += 1
        return result

    def max(self):
        result = 0
        for x in self.table:
            if len(x) > result:
                result = len(x)
        return result
    
    def avg(self):
        result = 0
        niepuste = 0
        for x in self.table:
            if len(x) > 0:
                result += len(x)
                niepuste += 1
        return result/niepuste

with open('3700.txt', 'r') as f:
    keys = [line.strip() for line in f]

# test
for m in [17, 1031, 1024]:
    for h in [hash, hashD, hashS]:
        ht = HashTable(m)
        for key in range(0, m*2):
            ht.add(keys[key], h)
        
        # print(ht)
        print(f"Dla wielkosci {m} i funkcji {h}:")
        print(f"ilosc pustych tablic: {ht.empty()}")
        print(f"najdluzsza tablica: {ht.max()}")
        print(f"srednia dlugosc tablicy: {ht.avg()}")
        print(30*'-')


# Dla wielkosci 17 i funkcji <built-in function hash>:
# ilosc pustych tablic: 2
# najdluzsza tablica: 5
# srednia dlugosc tablicy: 2.2666666666666666
# ------------------------------
# Dla wielkosci 17 i funkcji <function hashD at 0x000001C591A404A0>:
# ilosc pustych tablic: 1
# najdluzsza tablica: 4
# srednia dlugosc tablicy: 2.125
# ------------------------------
# Dla wielkosci 17 i funkcji <function hashS at 0x000001C591CF8B80>:
# ilosc pustych tablic: 2
# najdluzsza tablica: 5
# srednia dlugosc tablicy: 2.2666666666666666
# ------------------------------
# Dla wielkosci 1031 i funkcji <built-in function hash>:
# ilosc pustych tablic: 164
# najdluzsza tablica: 8
# srednia dlugosc tablicy: 2.378316032295271
# ------------------------------
# Dla wielkosci 1031 i funkcji <function hashD at 0x000001C591A404A0>:
# ilosc pustych tablic: 325
# najdluzsza tablica: 13
# srednia dlugosc tablicy: 2.9206798866855523
# ------------------------------
# Dla wielkosci 1031 i funkcji <function hashS at 0x000001C591CF8B80>:
# ilosc pustych tablic: 981
# najdluzsza tablica: 183
# srednia dlugosc tablicy: 41.24
# ------------------------------
# Dla wielkosci 1024 i funkcji <built-in function hash>:
# ilosc pustych tablic: 150
# najdluzsza tablica: 10
# srednia dlugosc tablicy: 2.34324942791762
# ------------------------------
# Dla wielkosci 1024 i funkcji <function hashD at 0x000001C591A404A0>:
# ilosc pustych tablic: 325
# najdluzsza tablica: 13
# srednia dlugosc tablicy: 2.9298998569384835
# ------------------------------
# Dla wielkosci 1024 i funkcji <function hashS at 0x000001C591CF8B80>:
# ilosc pustych tablic: 974
# najdluzsza tablica: 183
# srednia dlugosc tablicy: 40.96

# wielkosci 1031 i 1024 daja bardzo podobne wyniki
# wybór rodzaju funkcji hszującej (W, D, S) wpływał na jakość wyniku