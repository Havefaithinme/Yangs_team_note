# Tree data structure is a non linear data structure in which the nodes are connected in hierarchichal manner.
# Every Tree data structure has ONE root node that marks the access point of all the other nodes in the tree.
# Binary Tree, Binary Search Tree, AVL Tree, B Tree, B+ Tree, Expression Tree, etc.

# . Binary Tree has following 2 properties.
# 1. All the nodes on the left of the current node has a less value than the current node.
# 2. All the nodes on the right of the current node has a larger value than the current node.

class Node:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, data):
        if data < self.data:
            if self.left:
                print(f"heading left, {data}")
                self.left.insert(data)
            else:
                print(f"inserted as left node, {data}")
                self.left = Node(data)
        else:
            if self.right:
                print(f"heading right {data}")
                self.right.insert(data)
            else:
                print(f"inserted as right node, {data}")
                self.right = Node(data)


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def __repr__(self):
        pass

    def insert(self, data):
        if self.root:
            if self.root.data > data:
                if self.root.left:
                    print(f"heading left {data}")
                    self.root.left.insert(data)
                else:
                    print(f"inserted as left node, {data}")
                    self.root.left = Node(data)
            else:
                if self.root.right:
                    print(f"heading right {data}")
                    self.root.right.insert(data)
                else:
                    print(f"inserted as right node, {data}")
                    self.root.right = Node(data)
        else:
            print(f"inserted as root {data}")
            self.root = Node(data)

    # Naming or the tranversing (in, pre, post) standardized on the root node.
    def inorder_traverse(self, root):
        if root:
            self.inorder_traverse(root.left)
            print(root.data)  # in order
            self.inorder_traverse(root.right)

    def preorder_traverse(self, root):
        if root:
            print(root.data)  # pre order
            self.preorder_traverse(root.left)
            self.preorder_traverse(root.right)

    def postorder_traverse(self, root):
        if root:
            self.postorder_traverse(root.left)
            self.postorder_traverse(root.right)
            print(root.data)  # post order


if __name__ == "__main__":
    root = Node(5)
    tree = BinaryTree(root)
    tree.insert(1)
    tree.insert(6)
    tree.insert(2)
    tree.insert(7)
    # 크기 순서대로 출력이 되는 걸 확인 할 수 있음. 왼쪽 -> 자기자신 -> 오른쪽
    tree.inorder_traverse(tree.root)
    print("*" * 30)
    # 입력된 순서대로 출력이 되는 걸 확인 할 수 있음. 자기자신 -> 왼쪽 -> 오른쪽
    tree.preorder_traverse(tree.root)
    print("*" * 30)
    tree.postorder_traverse(tree.root)  # 왼쪽 -> 오른쪽 -> 자기자신
