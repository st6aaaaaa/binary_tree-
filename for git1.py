##
#
####
# Class Node:
# place is where we store values of Node
#
class Node:
    def __init__(self,i):
        self.rightChild = None
        self.leftChild = None
        self.iData = i


class Tree:
    def __init__(self):
        self.root = None

    def insert(self,iD):
        newNode = Node(iD)

        if self.root is None:
            self.root = newNode

        else:
            current = self.root

            while True:
                parent = current
                if iD < current.iData:
                    current = current.leftChild
                    if current is None:
                        parent.leftchild = newNode
                        return
                else:
                    current = current.rightChild
                    if current is None:
                        parent.rightChild = newNode
                        return

    def inOrder(self,localroot):
        if localroot is not None:
            self.inOrder(localroot.leftChild)
            print(localroot.iData, end = " ")
            self.inOrder(localroot.rightChild)

    # func shows Tree in inOrder order
    def printTree(self):
        self.inOrder(self.root)

  # we find successor . it help us when deleting node with given value
    def getSuccessor(self,delNode):

        successorParent = delNode
        successor = delNode
        current = delNode.rightChild

        while current is not None:
            successorParent = successor
            successor = current
            current = current.leftChild

        if successor is not delNode.rightChild:
            successorParent.leftChild = successor.rightChild
            successor.rightCHild = delNode.rightChild

        return successor

    def delete(self,key):

        current = self.root
        parent = self.root
        isLeftChild = True

        while current.iData != key:
            parent = current
            if key <current.iData:
                isLeftChild = True
                current = current.leftChild
            else:
                isLeftChild = False
                current = current.rightChild

            if current is None:
                return False


        if current.leftChild is None and current.rightChild is None:
            if current is self.root:
                self.root = None

            elif isLeftChild:
                parent.leftChild = None

            else:
                parent.rightChild = None

        elif current.leftChild is None:
            if current is self.root:
                self.root = current.rightChild

            elif isLeftChild:
                parent.leftchild = current.rightChild
            else:
                parent.rightChild = current.rightChild

        else:
            successor = self.getSuccessor(current)
            if current is self.root:
                self.root = successor

            elif isLeftChild:
                parent.leftChild = successor

            else:
                parent.rightChild = successor

            successor.leftChild = current.leftChild

        return True

    def find(self,key):

        current =self.root

        while current.iData != key:
            if key < current.iData:
                current = current.leftChild
            else:
                current = current.rightChild

            if current is None:
                return None

        return current


#            som comments
#            to check hot git-changes work
#
#
#