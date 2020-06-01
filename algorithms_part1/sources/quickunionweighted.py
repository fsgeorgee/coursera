class Weightedquickunion():
    def __init__(self, size):
        self.id = [i for i in range(size)]
        self.szid = [1 for i in range(size)]
    
    def union(self, x: int, y: int):
        if x < len(self.id) and y < len(self.id):
            xroot = self.root(x)
            yroot = self.root(y)
            if xroot == yroot:
                return
            if self.szid[xroot] < self.szid[yroot]:
                self.id[xroot] = yroot
                self.szid[yroot] += self.szid[xroot]
            else:
                self.id[yroot] = xroot
                self.szid[xroot] += self.szid[yroot]
    
    def connected(self, x: int, y: int) -> bool:
        if x < len(self.id) and y < len(self.id):
            return self.root(x) == self.root(y)
        return False
    
    def root(self, i: int) -> int:
        while i != self.id[i]:
            i = self.id[i]
        return i
    
    def printids(self):
        print('[%s]' % ', '.join(str(x) for x in range(len(self.id))))
        print(self.id)

if __name__ == '__main__':
    quickunion = Weightedquickunion(10)
    quickunion.printids()
    print(quickunion.union(4, 3))
    quickunion.printids()
    print(quickunion.union(3, 8))
    quickunion.printids()
    print(quickunion.union(6, 5))
    quickunion.printids()
    print(quickunion.union(9, 4))
    quickunion.printids()
    print(quickunion.union(2, 1))
    quickunion.printids()
    print(quickunion.union(5, 0))
    quickunion.printids()
    print(quickunion.union(7, 2))
    quickunion.printids()
    print(quickunion.union(6, 1))
    quickunion.printids()
    print(quickunion.union(7, 3))
    quickunion.printids()