class PriorityQueue:
    def __init__(self, prop, q=None):
        self.prop = prop
        if q == None:
            self.q = []
            self.size = len(self.q)
        else:
            self.q = q
            self.size = len(self.q)
            for i in range((self.size//2)-1, -1, -1):
                self.heapify(i)

    def swap(self, i, j):
        self.q[i], self.q[j] = self.q[j], self.q[i]

    def changeProperty(self, prop):
        self.prop = prop
        for i in range((self.size//2)-1, -1, -1):
            self.heapify(i)

    def peek(self):
        return self.q[0]

    def heapify(self, i):
        
        leftChild = 2 * i + 1
        rightChild = 2 * i + 2
        
        if self.prop == 'max':
            largest = i
            if leftChild < self.size and self.q[largest] < self.q[leftChild]:
                largest = leftChild
            if rightChild < self.size and self.q[largest] < self.q[rightChild]:
                largest = rightChild

            if largest != i:
                self.swap(i, largest)
                self.heapify(largest)

        elif self.prop == 'min':
            smallest = i
            if leftChild < self.size and self.q[smallest] > self.q[leftChild]:
                smallest = leftChild
            if rightChild < self.size and self.q[smallest] > self.q[rightChild] and self.q[rightChild] < self.q[leftChild]:
                smallest = rightChild

            if smallest != i:
                self.swap(i, smallest)
                self.heapify(smallest)
    
    def insert(self, new_data):
        self.q.append(new_data)
        self.size = len(self.q)
        if self.size > 1:
            for i in range((self.size//2)-1, -1, -1):
                self.heapify(i)

    def pop(self):
        self.swap(0, -1)
        ret = self.q.pop(-1)
        self.size = len(self.q)
        for i in range((self.size//2)-1, -1, -1):
                self.heapify(i)
        return ret

    def remove(self, data):
        for i in range(self.size):
            if data == self.q[i]:
                break

        self.swap(i, -1)
        self.q.pop(-1)

        self.size = len(self.q)
        for i in range((self.size//2)-1, -1, -1):
                self.heapify(i)