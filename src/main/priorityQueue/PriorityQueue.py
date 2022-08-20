'''
    A min-heap priority queue implementation using a binary heap.

    @author Joshua Teguh Santoso, joshuateguhsantoso@gmail.com
'''

class PriorityQueue:
    def __init__(self):
        self.q = []
        self.left = lambda n: 2*n + 1
        self.right = lambda n: 2*n + 2
        self.parent = lambda n: (n-1)//2

    def insert(self, data):
        if len(self.q) == 0:
            self.q.append(data)
        else:
            self.q.append(data)
            size = len(self.q)
            while self.q[self.parent(size-1)] > self.q[size-1]:
                self.q[size-1], self.q[self.parent(size-1)] = self.q[self.parent(size-1)], self.q[size-1]

    def pop(self):
        size = len(self.q)
        self.q[size-1], self.q[0] = self.q[0], self.q[size-1]
        ret = self.q.pop(-1)
        new_size = len(self.q)

        if new_size > 2:
            n = 0
            while self.q[n] > self.q[self.left(n)] or self.q[n] > self.q[self.right(n)]:
                print(f'n: {n}')
                if self.q[self.left(n)] < self.q[self.right(n)]:
                    min_child = self.left(n)
                elif self.q[self.right(n)] <= self.q[self.left(n)]:
                    min_child = self.right(n)
                print(f'min_child: {min_child}')
                self.q[n], self.q[min_child] = self.q[min_child], self.q[n]
                print(self.q)
                if self.left(n) <= new_size or self.right(n) <= new_size:
                    break
                else:
                    n = min_child

        return ret