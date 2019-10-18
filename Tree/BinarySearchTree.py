class Node:
    def __init__(self, data=None):
        self.data=data
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def insert(self, data):
        if self.root is None:
            self.root=Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left=Node(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right=Node(data)
            else:
                self._insert(data, cur_node.right)
        else:
            print("Values are already Present in BST")

    def find(self, data):
        if self.root:
            is_found = self._find(data, self.root)
            if is_found:
                return True
            return False
        else:
            return None
    def _find(self, data, cur_node):
        if data > cur_node.data and cur_node.right:
            return self._find(data, cur_node.right)
        elif data < cur_node.data and cur_node.left:
            return  self._find(data, cur_node.left)
        if data == cur_node.data:
            return True
    def inorder_printtree(self):
        if self.root:
            self._inorder_printtree(self.root)

    def _inorder_printtree(self, node):
        if node:
            self._inorder_printtree(node.left)
            print(str(node.data))
            self._inorder_printtree(node.right)
    def bstcheck(self):
        if self.root:
            is_satisfy=self._bstcheck(self.root, self.root.data)
            if is_satisfy is None:
                return True
            return False
    def _bstcheck(self, node, data):
        if node.left:
            if data > node.left.data:
                return self._bstcheck(node.left, node.left.data)
            else:
                return False
        if node.right:
            if data < node.right.data:
                return self._bstcheck(node.right, node.right.data)
            else:
                return False
bst=BST()
bst.insert(4)
bst.insert(2)
bst.insert(8)
bst.insert(5)
bst.insert(10)

