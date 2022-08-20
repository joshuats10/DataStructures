class Node:
    def __init__(self, info, priority):
        self.info = info
        self.priority = priority

class PriorityQueue:
    def __init__(self, prop, init_data=None):
        self.prop = prop
        if init_data:
            self.data = init_data
            for i in range((self.qSize()//2)-1, -1, -1):
                self.heapify(i)
        else:
            self.data = []

    def qSize(self):
        return len(self.data)

    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def changeProperty(self, prop):
        self.prop = prop
        for i in range((self.qSize()//2)-1, -1, -1):
            self.heapify(i)

    def peek(self):
        return self.data[0]

    def heapify(self, i):
        
        leftChild = 2 * i + 1
        rightChild = 2 * i + 2
        
        if self.prop == 'max':
            largest = i
            if leftChild < self.qSize() and self.data[largest].priority < self.data[leftChild].priority:
                largest = leftChild
            if rightChild < self.qSize() and self.data[largest].priority < self.data[rightChild].priority:
                largest = rightChild

            if largest != i:
                self.swap(i, largest)
                self.heapify(largest)

        elif self.prop == 'min':
            smallest = i
            if leftChild < self.qSize() and self.data[smallest].priority > self.data[leftChild].priority:
                smallest = leftChild
            if rightChild < self.qSize() and self.data[smallest].priority > self.data[rightChild].priority and self.data[rightChild].priority < self.data[leftChild].priority:
                smallest = rightChild

            if smallest != i:
                self.swap(i, smallest)
                self.heapify(smallest)
    
    def insert(self, new_node):
        self.data.append(new_node)
        if self.qSize() > 1:
            for i in range((self.qSize()//2)-1, -1, -1):
                self.heapify(i)

    def pop(self):
        self.swap(0, -1)
        ret = self.data.pop(-1)
        for i in range((self.qSize()//2)-1, -1, -1):
                self.heapify(i)
        return (ret.info, ret.priority)

    def remove(self, info):
        for i in range(self.qSize()):
            if info == self.data[i].info:
                break

        self.swap(i, -1)
        self.data.pop(-1)

        for i in range((self.qSize()//2)-1, -1, -1):
                self.heapify(i)

    def changePriority(self, info, new_priority):
        for i in range(self.qSize()):
            if info == self.data[i].info:
                self.data[i].priority = new_priority
        
        for i in range((self.qSize()//2)-1, -1, -1):
                self.heapify(i)

if __name__ == "__main__":
    node1 = Node('John', 1)
    node2 = Node('Christina', 5)
    node3 = Node('Albert', 2)
    node4 = Node('Bella', 3) 
    node5 = Node('Peter', 4)

    lst = [node1, node2, node3, node4, node5]
    pQueue = PriorityQueue('min', lst)
    # pQueue.insert(node1)
    # pQueue.insert(node2)
    # pQueue.insert(node3)
    # pQueue.insert(node4)
    # pQueue.insert(node5)

    pQueue.remove('Christina')
    pQueue.changePriority('John', 6)
    pQueue.changeProperty('max')

    while pQueue.qSize() > 0:
        ret = pQueue.pop()
        print(f'{ret[0]}: {ret[1]}')
