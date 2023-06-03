class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def get_data(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.sentinel = Node(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

    def first_node(self):
        if self.sentinel.next == self.sentinel:
            return None
        else:
            return self.sentinel.next

    def insert_after(self, x, data):
        y = Node(data)

        y.prev = x
        y.next = x.next

        x.next = y

        y.next.prev = y

    def append(self, data):
        last_node = self.sentinel.prev
        self.insert_after(last_node, data)

    def prepend(self, data):
        self.insert_after(self.sentinel, data)

    def delete(self, x):
        if x == None:
            print("Brak elementu na liscie")
            return
        x.prev.next = x.next
        x.next.prev = x.prev

    def find(self, data):
        self.sentinel.data = data

        x = self.first_node()
        while x.data != data:
            x = x.next

        self.sentinel.data = None

        if x == self.sentinel:
            return None
        else:
            return x

    def print(self):
        wynik = []
        x = self.sentinel.next
        while x != self.sentinel:
            wynik.append(x.data)
            x = x.next

        print(wynik)

def bezPowtorzen(lista):
    result = LinkedList()
    cur = lista.sentinel.next
    while cur != lista.sentinel:
        if result.first_node() == None:
            result.append(cur.data)
        elif result.find(cur.data) == None:
            result.append(cur.data)
        cur = cur.next
    return result

def scal(l1,l2):
    cur = l2.sentinel.next
    while cur != l2.sentinel:
        l1.append(cur.data)
        cur = cur.next
    return l1

    

def test():
    l = LinkedList()
    l.append('ala')
    l.append('ma')
    l.append('kota')
    # l.print()

    l.prepend('ma')
    # l.print()

    # print(l.find('ala'))
    # print(l.find('ddd'))

    # l.delete(l.find('nie'))
    # l.print()
    # l.delete(l.find('dd'))

    l2 = bezPowtorzen(l)
    l.print()
    l2.print()

    scal(l, l2)

    l.print()



test()