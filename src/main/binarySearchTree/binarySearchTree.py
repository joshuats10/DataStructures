"""
    Implementation of Binary Search Tree (BST)
    
    @author Joshua Teguh Santoso, joshuateguhsantoso@gmail.com
"""

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.nodeCount = 0
        self.root = None

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return self.nodeCount

    def add(self, elem):
        if self.contains(elem):
            return False
        else:
            self.root = self.__add(self.root, elem)
            self.nodeCount += 1
            return True

    def __add(self, node, elem):
        if node == None:
            node = Node(elem, None, None)
        else:
            if elem < node.data:
                node.left = self.__add(node.left, elem)
            else:
                node.right = self.__add(node.right, elem)

        return node

    def remove(self, elem):
        if self.contains(elem):
            self.root = self.__remove(self.root, elem)
            self.nodeCount -= 1
            return True

        return False

    def __remove(self, node, elem):
        if node == None:
            return None

        cmp = elem < node.data

        if elem == node.data:
            if node.left == None:
                
                rightChild = node.right

                node.data = None
                node = None

                return rightChild

            elif node.right == None:
                
                leftChild = node.left
                
                node.data = None
                node = None

                return leftChild

            else:
                tmp = self.findMin(node.right)

                node.data = tmp.data

                node.right = self.__remove(node.right, tmp.data)

        elif cmp is True:
            node.left = self.__remove(node.left, elem)

        elif cmp is False:
            node.right = self.__remove(node.right, elem)

        else:
            return None
        
        return node

    def contains(self, elem):
        return self.__contains(self.root, elem)

    def __contains(self, node, elem):
        if node is None:
            return False

        cmp = elem < node.data

        if elem == node.data:
            return True 
        elif cmp is True:
            return self.__contains(node.left, elem)
        elif cmp is False:
            return self.__contains(node.right, elem)
        else:
            return True

    def findMin(self, node):
        while node.left is not None:
            node = node.left
        return node

    def findMax(self, node):
        while node.right is not None:
            node = node.right
        return node

    def height(self):
        return self.__height(self.root)

    def __height(self, node):
        if node == None:
            return 0
        return max(self.__height(node.left), self.__height(node.right)) + 1

    def traversal(self, method):
        if method == "preOrder":
            return self.preOrderTraversal()
        elif method == "inOrder":
            return self.inOrderTraversal()
        elif method == "postOrder":
            return self.postOrderTraversal()
        elif method == "levelOrder":
            return self.levelOrderTraversal()

    def preOrderTraversal(self):
        if self.root is None:
            return None
        
        stack, ret = [], []
        stack.append(self.root)

        while True:
            if self.root is None or len(stack) == 0:
                break

            node = stack.pop()
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

            ret.append(node.data)

        return ret

    def inOrderTraversal(self):
        if self.root is None:
            return None
        
        stack, ret = [], []
        stack.append(self.root)

        trav = self.root

        while True:
            if self.root is None or len(stack) == 0:
                break
            
            while trav != None and trav.left != None:
                stack.append(trav.left)
                trav = trav.left

            node = stack.pop()
            if node.right is not None:
                stack.append(node.right)
                trav = node.right

            ret.append(node.data)

        return ret

    def postOrderTraversal(self):
        stack, stack1, ret = [], [], []
        stack.append(self.root)

        while len(stack) != 0:
            node = stack.pop()
            if node is not None:
                stack1.append(node)
                if node.left is not None:
                    stack.append(node.left)
                if node.right is not None:
                    stack.append(node.right)

        while True:
            if self.root == None or len(stack1) == 0:
                break

            node = stack1.pop()

            ret.append(node.data)

        return ret

    def levelOrderTraversal(self):
        queue, ret = [], []
        queue.append(self.root)

        while True:
            if self.root == None or len(queue) == 0:
                break
                
            node = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

            ret.append(node.data)

        return ret

if __name__ == "__main__":
    bst = BinarySearchTree()

    bst.add(11)
    bst.add(6)
    bst.add(15)
    bst.add(3)
    bst.add(17)
    bst.add(8)
    bst.add(13)
    bst.add(1)
    bst.add(5)
    bst.add(12)
    bst.add(14)
    bst.add(19)

    print(bst.traversal("preOrder"))
    print(bst.traversal("inOrder"))
    print(bst.traversal("postOrder"))
    print(bst.traversal("levelOrder"))