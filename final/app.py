from flask import Flask, render_template

app = Flask(__name__)

###################################################### Node ######################################################
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.position = (0, 0)  # Initial position of the node

###################################################### BST ###################################################### 
class BinarySearchTree:
    def __init__(self, root):
        self.root = root


    def add(self, data):
        self.root = self._add_recursive(self.root, data)

    def _add_recursive(self, root, data):
        if root is None:
            return Node(data)

        if data < (root.value):
            root.left = self._add_recursive(root.left, data)
        elif data > (root.value):
            root.right = self._add_recursive(root.right, data)

        return root


    def remove(self, data):
        self.root = self._remove_recursive(self.root, data)

    def _remove_recursive(self, root, data):
        if root is None:
            return root
        
        if data < root.value:
            root.left = self._remove_recursive(root.left, data)
        elif data > root.value:
            root.right = self._remove_recursive(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                min_value = self._find_min(root.right)
                root.value = min_value
                root.right = self._remove_recursive(root.right, min_value)
        
        return root

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node.value

    def search(self, data):
        return self._search_recursive(self.root, data)

    def _search_recursive(self, root, data):
        if root is None or root.value == data:
            return root
        
        if data < root.value:
            return self._search_recursive(root.left, data)
        else:
            return self._search_recursive(root.right, data)

    def inorder_traverse(self):
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, root):
        if root is not None:
            self._inorder_recursive(root.left)
            print(root.value, end=' ')
            self._inorder_recursive(root.right)


###################################################### Max Heap ######################################################






###################################################### Min Heap ######################################################



###################################################### linked list ######################################################




###################################################### static ######################################################
root = Node(15)
bst = BinarySearchTree(root)

bst.add(7)
bst.add(3)
bst.add(11)
bst.add(1)
bst.add(5)
bst.add(9)
bst.add(13)
bst.add(2)
bst.add(4)
bst.add(6)
bst.add(8)
bst.add(10)
bst.add(12)
bst.add(14)
bst.add(23)
bst.add(19)
bst.add(17)
bst.add(21)
bst.add(25)
bst.add(27)
bst.add(16)
bst.add(18)
bst.add(20)
bst.add(22)
bst.add(24)
bst.add(26)
bst.add(28)
bst.remove(25)
bst.add(25)
bst.add(26)
bst.remove(27)
bst.add(27)
bst.add(30)
bst.add(0)
bst.add(23.5)

###################################################### Flask ######################################################
# Flask route for the visualization page
@app.route('/')
def visualize_tree():
    return render_template('tree_visualizer.html', bst=bst)
###################################################### Main ######################################################
if __name__ == '__main__':
    app.run()
