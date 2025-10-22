from collections import deque

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
    
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

def height(node):
    if node is None:
        return 0
    queue = deque()
    queue.append(node)
    height = 0
    while queue:
        level_size = len(queue)
        
        for _ in range(level_size):
            current = queue.popleft()
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        
        height += 1
    return height

def diameter(node):
    current_height = 0
    def height(node):
        nonlocal current_height
        if node is None:
            return 0
        left_height = height(node.left)
        right_height = height(node.right)
        current_height = max(current_height, left_height + right_height)
        return 1 + max(left_height, right_height)
    height(node)
    return current_height

def is_balanced(node):
    if node is None:
        return True
    left_height = is_balanced(node.left)
    if left_height == -1:
        return -1
    right_height = is_balanced(node.right)
    if right_height == -1:
        return -1
    if abs(left_height - right_height) > 1:
        return -1
    return 1 + max(left_height, right_height)

def topView(node):
    if node is None:
        return
    queue = deque()
    result = {}
    queue.append((node, 0))
    
    while queue:
        current, pos = queue.popleft()
        if pos not in result:
            result[pos] = current.val
        if current.left:
            queue.append((current.left, pos - 1))
        if current.right:
            queue.append((current.right, pos + 1))
    for key in sorted(result.keys()):
        print(result[key], end= '')

def bottomView(node):
    if node is None:
        return
    queue = deque()
    result = {}
    queue.append((node, 0))

    while queue:
        current, pos = queue.popleft()
        result[pos] = current.val
        if current.left:
            queue.append((current.left, pos - 1))
        if current.right:
            queue.append((current.right, pos + 1))
    for key in sorted(result.keys()):
        print(result[key], end= '') 

def leftView(node):
    if node is None:
        return
    queue = deque()
    queue.append(node) 
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            current = queue.popleft()
            if i == 0:
                print(current.val, end = ' ')
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

def leftView2(root):
    def DFS(node, level, result):
        if node is None:
            return
        if level == len(result):
            result.append(node.val)
        DFS(node.left, level + 1, result)
        DFS(node.right, level+ 1, result)
    result = []
    DFS(root, 0, result)
    return result

def rightView(node):
    if node is None:
        return
    queue = deque()
    queue.append(node) 
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            current = queue.popleft()
            if i == level_size - 1:
                print(current.val, end = ' ')
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

def rightView2(root):
    def DFS(node, level, result):
        if node is None:
            return
        if level == len(result):
            result.append(node.val)
        DFS(node.right, level +1, result)
        DFS(node.left, level + 1, result)
        return
    result = []
    DFS(root, 0, result)
    return result
    

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print("Preorder Traversal of binary tree is:")
    preorder_traversal(root)
    # Output: 1 2 4 5 3 6 7

    print("\n Inorder Traversal of binary tree is: ")
    inorder_traversal(root)
    # Output: 4 2 5 1 6 3 7

    print("\n Postorder Traversal of binary tree is: ")
    postorder_traversal(root)
    # Output: 4 5 2 6 7 3 1

    print("\n Levelorder Traversal of binary tree is: ")
    levelorder_traversal(root)
    # Output: 1 2 3 4 5 6 7

    print("\n Height of binary tree is: ", height(root))
    # Output: 3
    
    print("\n Diameter of binary tree is: ", diameter(root))
    # Output: 5

    print("\n Is the binary tree balanced?")
    print(is_balanced(root) != -1)
    # Output: True

    print('\n Top view of the binary tree is:')
    topView(root)
    # Output: 4 2 1 3 7

    print('\n Bottom view of the binary tree is:')
    bottomView(root)
    # Output: 4 2 1 3 7

    print('\n Left view of the binary tree is:')
    leftView(root)
    # Output: 1 2 4
    
    print('\n Left view of the binary tree using DFS is:')
    print(leftView2(root))

    print('\n Right view of the binary tree is:')
    rightView(root)
    # Output: 1 3 7

    print('\n Right view of the binary tree using DFS is:')
    print(rightView2(root))

