class Node:
    def __init__(self,x):
        self.key = x
        self.next = None
        self.prev = None 


class LinkedList:
    def __init__(self):
        self.head = None

    def listInsert(self, x):
    # wstawia wezel x do listy L
    # lista dwukierunkowa niecykliczna bez wartownika
        x.next = self.head  
        if self.head != None:
           self.head.prev = x 
        self.head = x
        x.prev = None

    def listPrint(self):
        # x = self.head
        current = self.head
        wynik = []
        while current:
            wynik.append(current.key)
            current = current.next
        print(wynik)
        
        # uzupelnic

    def listSearch(self,k):
    # szuka wezla zawierajacego klucz k
    # lista dwukierunkowa niecykliczna bez wartownika
        x = self.head
        while x!=None and x.key!=k:
            x = x.next
        return x   # None oznacza, ze szukanego klucza
                   # nie ma na liscie

    def listDelete(self,x):
    # usuwa wezel x z listy
    # lista dwukierunkowa niecykliczna bez wartownika        
        if x.prev != None:
           x.prev.next = x.next
        else:
           self.head = x.next
        if x.next != None:
           x.next.prev = x.prev

    def append(self,x):
        cur = self.head
        if cur:
            while cur.next:
                cur = cur.next
            cur.next = x
        else:
            self.head = x

    def bezPowtorzen(self):
        new = LinkedList()
        cur = self.head
        while cur:
            if new.listSearch(cur.key) == None:
                new.append(Node(cur.key))
            cur = cur.next
        return new
    
    def scal(self, lista):
        cur = lista.head
        while cur:
            self.append(Node(cur.key))
            cur = cur.next
            
l = LinkedList()
l.listInsert(Node('ala'))
l.listInsert(Node('ma'))
l.listInsert(Node(2))
l.listInsert(Node(2))
l.listPrint()
print(l.listSearch('alaj'))
l.listDelete(l.listSearch('ala'))
l.append(Node(2))
l.listPrint()
nowa = l.bezPowtorzen()
nowa.listPrint()
l.scal(nowa)
l.listPrint()