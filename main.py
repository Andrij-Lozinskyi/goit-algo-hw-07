class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(node, key):
    if node is None:
        return Node(key)
    else:
        if key < node.val:
            node.left = insert(node.left, key)
        else:
            node.right = insert(node.right, key)
    return node

def find_max_value(node):
    current = node
    while current.right is not None:
        current = current.right
    return current.val

def find_min_value(node):
    current = node
    while current.left is not None:
        current = current.left
    return current.val

def find_sum_of_values(node):
    if node is None:
        return 0
    return node.val + find_sum_of_values(node.left) + find_sum_of_values(node.right)

root = None
keys = [4, 2, 6, 1, 3, 5, 7]
for key in keys:
    root = insert(root, key)

print("Найбільше значення в BST:", find_max_value(root))
print("Найменше значення в BST:", find_min_value(root))
print("Сума всіх значень в BST:", find_sum_of_values(root))