class Quickfind():
    def __init__(self, size: int):
        self.id = [i for i in range(size)]
    
    def connected(self, x: int, y: int) -> bool:
        if x < len(self.id) and y < len(self.id):
            return self.id[x] == self.id[y]
        return False

    def union(self, x: int, y: int):
        idx = self.id[x]
        idy = self.id[y]
        unions = self.id.count(idy)
        unifed = 0
        i = -1
        while unifed < unions:
            i = self.id.index(idy, i+1)
            self.id[i] = idx
            unifed += 1
    
    def printids(self):
        print(self.id)

if __name__ == '__main__':
    quickfind = Quickfind(10)
    quickfind.printids()
    print(quickfind.connected(1, 2))
    print(quickfind.union(2, 1))
    quickfind.printids()
    print(quickfind.union(4, 5))
    quickfind.printids()
    print(quickfind.union(3, 1))
    quickfind.printids()