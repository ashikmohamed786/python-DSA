class treenode:
    def __init__(self,value):
        self.right=None
root=treenode(1)
root.left=treenode(2)
root.right=treenode(3)
root.left.left=treenode(4)
root.left.right=treenode(5)
root.right.left=treenode(6)
root.right.right=treenode(7)
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Create Nodes
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Preorder Traversal
def preorder(node):
    if node:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)

# Inorder Traversal
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

# Postorder Traversal
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")

# Level Order Traversal
def levelorder(root):
    if not root:
        return

    queue = [root]

    while queue:
        node = queue.pop(0)
        print(node.data, end=" ")

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

print("Preorder:")
preorder(root)

print("\nInorder:")
inorder(root)

print("\nPostorder:")
postorder(root)

print("\nLevel Order:")
levelorder(root)

