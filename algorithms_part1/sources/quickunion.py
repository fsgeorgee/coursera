class Quickunion():
    def __init__(self, size):
        self.id = [i for i in range(size)]
    
    def union(self, x: int, y: int):
        if x < len(self.id) and y < len(self.id):
            xroot = self.root(x)
            yroot = self.root(y)
            self.id[xroot] = yroot
    
    def connected(self, x: int, y: int) -> bool:
        if x < len(self.id) and y < len(self.id):
            return self.root(x) == self.root(y)
        return False
    
    def root(self, i: int) -> int:
        while i != self.id[i]:
            i = self.id[i]
        return i
    
    def printids(self):
        print(self.id)

if __name__ == '__main__':
    quickunion = Quickunion(10)
    quickunion.printids()
    print(quickunion.connected(1, 2))
    print(quickunion.union(2, 1))
    quickunion.printids()
    print(quickunion.union(4, 5))
    quickunion.printids()
    print(quickunion.union(3, 1))
    quickunion.printids()