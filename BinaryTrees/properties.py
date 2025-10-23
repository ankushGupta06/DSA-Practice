from collections import deque

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
