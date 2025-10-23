from collections import deque

def preorder_traversal(node):
    if node == None:
        return
    print(node.val, end = '')
    preorder_traversal(node.left)
    preorder_traversal(node.right)

def inorder_traversal(node):
    if node == None :
        return
    inorder_traversal(node.left)
    print(node.val, end = '')
    inorder_traversal(node.right)

def postorder_traversal(node):
    if node == None:
        return
    postorder_traversal(node.left)
    postorder_traversal(node.right)
    print(node.val, end = '')

def levelorder_traversal(node):
    if node is None:
        return
    queue = deque()
    queue.append(node)
    while queue:
        current = queue.popleft()
        print(current.val, end = '')
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
