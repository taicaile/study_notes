class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        curNode = self.root

        while True:
            if new_val <= curNode.value:
                if curNode.left:
                    curNode = curNode.left
                else:
                    curNode.left = Node(new_val)
                    break
            else:
                if curNode.right:
                    curNode = curNode.right
                else:
                    curNode.right = Node(new_val)
                    break

    def search(self, find_val):
        curNode = self.root

        while curNode:
            if curNode.value == find_val:
                return True
            elif find_val < curNode.value:
                curNode = curNode.left
            else:
                curNode = curNode.right

        return False


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))
