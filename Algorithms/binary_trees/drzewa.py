with open('nazwiska2.txt', 'r') as file:
    people = []
    for line in file:
        line = line.strip()
        people.append(line)

class Node:
    def __init__(self,x):
        self.key = x
        self.left = None # lewy syn
        self.right = None # prawy syn
        self.p = None # ojciec

class BST:
    def __init__(self):
        self.root = None

    def search(self,k):
        # szuka wezla zawierajacego klucz k
        x = self.root
        while x!=None and x.key!=k:
            if k<x.key:
                x=x.left
            else:
                x=x.right
        return x # None oznacza, ze szukanego klucza nie ma w drzewie 
        
    def insert(self, z):
        # wstawia wezel z do drzewa
        x = self.root
        y = None # y jest ojcem x
        while x != None:
            y=x
            if z.key<x.key:
                x=x.left
            else:
                x=x.right
        z.p=y
        if y==None: # drzewo puste
            self.root=z
        else:
            if z.key<y.key:
                y.left=z
            else:
                y.right=z

    def minimum(self,x):
        # zwraca skrajny lewy węzeł w poddrzewie o korzeniu x
        # czyli węzeł o najmniejszym kluczu w tym poddrzewie
        while x.left != None:
            x = x.left
        return x

    def Transplant(self,u,v):
        # podczepia poddrzewo o korzeniu "v" w miejsce wezla u
        if u.p==None: # u jest korzeniem
            self.root=v
        else:
            if u==u.p.left: # u jest lewym synem
                u.p.left=v
            else:
                u.p.right = v # u jest prawym synem
        if v != None:
            v.p=u.p

    def delete(self,z):
        # wersja wg nowszych wydań Cormena
        if z.left == None:
            self.Transplant(z,z.right)
        elif z.right == None:
            self.Transplant(z,z.left)
        else:
            y=self.minimum(z.right)
            if y.p != z:
                self.Transplant(y,y.right)
                y.right=z.right
                y.right.p=y
            self.Transplant(z,y)
            y.left=z.left
            y.left.p=y 

    def printInOrder(self):
        # “d” to głębokość na której jest węzeł “x”
        def help(x, d):
            if x==None: return
            help(x.left, d+1)
            print(x.key, d)
            help(x.right,d+1)
        help(self.root, 0)

    def maxDepth(self):
        depths = []
        def help(n, acc):
            if n == None: return
            help(n.left, acc+1)
            help(n.right, acc+1)
            depths.append(acc)
        help(self.root, 0)
        return max(depths) if (len(depths) != 0) else 0


def zadanie():
    for w in [500, 1000, 2000]:
        t = BST()
        for x in range(0, w):
            if t.search(people[x]) == None:
                t.insert(Node(people[x]))
            if x == 10: t.printInOrder()
        print(f'Dla drzewa {w} elementowego wysokosc to: {t.maxDepth()}')
        print("-"*100)

zadanie()