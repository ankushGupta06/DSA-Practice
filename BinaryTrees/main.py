from node import Node
from traversals import preorder_traversal, inorder_traversal, postorder_traversal, levelorder_traversal
from properties import height, diameter, is_balanced
from views import topView, bottomView, leftView, leftView2, rightView, rightView2

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
