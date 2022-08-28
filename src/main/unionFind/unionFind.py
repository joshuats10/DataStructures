"""
    Implementation of Union Find (disjoint set) data structure.

    @author Joshua Teguh Santoso, joshuateguhsantoso@gmail.com
"""

class UnionFind:
    def __init__(self, n):
        self.id = [i for i in range(n)]
        self.sz = [1 for i in range(n)]

    def find(self, i):
        
        root = i
        while(root != self.id[root]):
            root = self.id[root]

        while (i != root):
            next = self.id[i]
            self.id[i] = root
            i = next

        return root

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def unify(self, x, y):

        if self.connected(x, y):
            return

        root1 = self.find(x)
        root2 = self.find(y)

        if self.sz[root1] < self.sz[root2]:
            self.sz[root2] += self.sz[root1]
            self.id[root1] = root2
            self.sz[root1] = 0
        else:
            self.sz[root1] += self.sz[root2]
            self.id[root2] = root1
            self.sz[root2] = 0

if __name__ == "__main__":
    
    uf = UnionFind(6)
    uf.unify(1,2)
    uf.unify(3,5)
    uf.unify(4,5)
    uf.unify(0,5)
    uf.unify(0,2)
    print(uf.id)