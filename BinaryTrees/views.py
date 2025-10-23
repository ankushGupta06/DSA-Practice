from collections import deque

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
  