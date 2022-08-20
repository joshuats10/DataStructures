'''
    A priority queue implementation using a binary heap that
    able to do both min- and max-heap.

    Input data: Node(info, priority)

    @author Joshua Teguh Santoso, joshuateguhsantoso@gmail.com
'''

class Node:
    """
        This class acts as a container for the input data with
        an info (can be anything but in this case name) with its priority level.
    """
    def __init__(self, info, priority):
        self.info = info
        self.priority = priority

class PriorityQueue:
    """
        This class is the implementation of priority queue using a binary heap
        that able to do both min- and max-heap. 
    """
    def __init__(self, prop, init_data=None):
        
        # Set the property of the priority queue
        # whether it's a min- or max-heap.
        self.prop = prop

        # Initialize the priority queue.
        if init_data:
            self.data = init_data
            for i in range((self.qSize()//2)-1, -1, -1):
                self.heapify(i)
        else:
            self.data = []

    # Obtain the size of the priority queue
    def qSize(self):
        return len(self.data)

    # Function to swap the data in the binary tree
    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    # Change the property of the priority queue from max- to min-heap
    # or the other way around.
    def changeProperty(self, prop):
        self.prop = prop
        for i in range((self.qSize()//2)-1, -1, -1):
            self.heapify(i)

    # Peek the root of the priority queue
    def peek(self):
        return self.data[0]

    # Function to make the priority queue fulfills
    # the binary heap condition
    def heapify(self, i):
        
        leftChild = 2 * i + 1
        rightChild = 2 * i + 2
        
        if self.prop == 'max':
            largest = i 

            # See if left child of root exists and is greater than root
            if leftChild < self.qSize() and self.data[largest].priority < self.data[leftChild].priority:
                largest = leftChild
            
            # See if right child of root exists and is greater than root
            if rightChild < self.qSize() and self.data[largest].priority < self.data[rightChild].priority:
                largest = rightChild

            # Swap root if needed
            if largest != i:
                self.swap(i, largest)
                self.heapify(largest)

        elif self.prop == 'min':
            smallest = i

            # See if left child of root exists and is less than root
            if leftChild < self.qSize() and self.data[smallest].priority > self.data[leftChild].priority:
                smallest = leftChild

            # See if right child of root exists and is less than root
            if rightChild < self.qSize() and self.data[smallest].priority > self.data[rightChild].priority:
                smallest = rightChild

            # Swap root if needed
            if smallest != i:
                self.swap(i, smallest)
                self.heapify(smallest)
    
    # Insert a new node into the priority queue
    def insert(self, new_node):
        self.data.append(new_node)
        if self.qSize() > 1:
            for i in range((self.qSize()//2)-1, -1, -1):
                self.heapify(i)

    # Extracting the max/min of the priority queue
    def pop(self):
        self.swap(0, -1)
        ret = self.data.pop(-1)
        for i in range((self.qSize()//2)-1, -1, -1):
                self.heapify(i)
        return (ret.info, ret.priority)

    # Removing a specific data from the priority queue
    def remove(self, info):
        for i in range(self.qSize()):
            if info == self.data[i].info:
                break

        self.swap(i, -1)
        self.data.pop(-1)

        for i in range((self.qSize()//2)-1, -1, -1):
                self.heapify(i)

    # Change the priority of a specific data in the priority queue
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
