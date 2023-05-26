from flask import Flask, render_template, redirect, url_for, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a7a123'

###################################################### Node #######################################################
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.position = (0, 0)  # Initial position of the node
###################################################### BST ######################################################### 
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.inorder_result = []
        self.preorder_result = []
        self.postorder_result = []
        self.search = None

    def add(self, data):
        if(self.root is None):
            self.root = Node(data)
        else:
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

    def _find_min(self):
        node =  self.root
        while node.left is not None:
            node = node.left
        return node.value
    def _find_max(self):
        node = self.root
        while node.right is not None:
            node = node.right
        return node.value

    def searchNode(self, data):
        if self.root is not None:
            self.search = Node(self.root.value)
        else:
            return 
        return self._search_recursive(self.root, data, self.search)

    def _search_recursive(self, root, data, search1):
        if root is None:
            return None
            
        if root.value == data:
            return search1.value

        if data < root.value:
            if root.left is None:
                return None
            search1.left = Node(root.left.value)
            return self._search_recursive(root.left, data, search1.left)
        else:
            if root.right is None:
                return None
            search1.right = Node(root.right.value)
            return self._search_recursive(root.right, data, search1.right)
    
    def inorder_traverse(self):
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, root):
        if root is not None:
            self._inorder_recursive(root.left)
            self.inorder_result.append(root.value)
            self._inorder_recursive(root.right)

    def preorder_traverse(self):
        self._preorder_recursive(self.root)
        print()

    def _preorder_recursive(self, node):
        if node is not None:
            self.preorder_result.append(node.value)
            self._preorder_recursive(node.left)
            self._preorder_recursive(node.right)

    def postorder_traverse(self):
        self._postorder_recursive(self.root)
        print()

    def _postorder_recursive(self, node):
        if node is not None:
            self._postorder_recursive(node.left)
            self._postorder_recursive(node.right)
            self.postorder_result.append(node.value)
            

###################################################### Max Heap ######################################################

class MaxHeap:
    def __init__(self):
        self.heap = []
        self.root = None

    def insert(self, value):
        self.heap.append(value)
        self.max_heapify_up(len(self.heap) - 1)

    def delete(self, value):
        if value not in self.heap:
            flash(str(value) + ' is not in the Max Heap', category='inst')
        else:
            index = self.heap.index(value)
            self.swap(index, len(self.heap) - 1)
            self.heap.pop()
            self.max_heapify_down(index)

    def max_heapify_up(self, index):
        parent_index = self.find_parent(index)
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.swap(index, parent_index)
            self.max_heapify_up(parent_index)

    def max_heapify_down(self, index):
        left_child_index = self.find_left_child(index)
        right_child_index = self.find_right_child(index)
        largest_index = index

        if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest_index]:
            largest_index = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest_index]:
            largest_index = right_child_index

        if largest_index != index:
            self.swap(index, largest_index)
            self.max_heapify_down(largest_index)

    def find_left_child(self, index):
        return (2 * index) + 1

    def find_right_child(self, index):
        return (2 * index) + 2

    def find_parent(self, index):
        return (index - 1) // 2
    
    def find_left_child_element(self, element):
        index = self.heap.index(element)
        return (2 * index) + 1

    def find_right_child_element(self, element):
        index = self.heap.index(element)
        return (2 * index) + 2

    def find_parent_element(self, element):
        index = self.heap.index(element)
        return (index - 1) // 2

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def make_binary_tree(self):
        if len(self.heap) == 0:
            self.root = None
            return None

        self.root = Node(self.heap[0])
        queue = [(self.root, 0)]

        while queue:
            current_node, current_index = queue.pop(0)
            left_child_index = self.find_left_child(current_index)
            right_child_index = self.find_right_child(current_index)

            if left_child_index < len(self.heap):
                left_child = Node(self.heap[left_child_index])
                current_node.left = left_child
                queue.append((left_child, left_child_index))

            if right_child_index < len(self.heap):
                right_child = Node(self.heap[right_child_index])
                current_node.right = right_child
                queue.append((right_child, right_child_index))

        return self.root


###################################################### Min Heap #########################################################

class MinHeap:
    def __init__(self):
        self.heap = []
        self.root = None

    def insert(self, value):
        self.heap.append(value)
        self.min_heapify_up(len(self.heap) - 1)

    def delete(self, value):
        if value not in self.heap:
            flash(str(value) + ' is not in the Min Heap', category='inst')
        else:
            index = self.heap.index(value)
            self.swap(index, len(self.heap) - 1)
            self.heap.pop()
            self.min_heapify_down(index)

    def min_heapify_up(self, index):
        parent_index = self.find_parent(index)
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self.swap(index, parent_index)
            self.min_heapify_up(parent_index)

    def min_heapify_down(self, index):
        left_child_index = self.find_left_child(index)
        right_child_index = self.find_right_child(index)
        smallest_index = index

        if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest_index]:
            smallest_index = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest_index]:
            smallest_index = right_child_index

        if smallest_index != index:
            self.swap(index, smallest_index)
            self.min_heapify_down(smallest_index)

    def find_left_child(self, index):
        return (2 * index) + 1

    def find_right_child(self, index):
        return (2 * index) + 2

    def find_parent(self, index):
        return (index - 1) // 2
    
    def find_left_child_element(self, element):
        index = self.heap.index(element)
        return (2 * index) + 1

    def find_right_child_element(self, element):
        index = self.heap.index(element)
        return (2 * index) + 2

    def find_parent_element(self, element):
        index = self.heap.index(element)
        return (index - 1) // 2

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def make_binary_tree(self):
        if len(self.heap) == 0:
            self.root = None
            return None

        self.root = Node(self.heap[0])
        queue = [(self.root, 0)]

        while queue:
            current_node, current_index = queue.pop(0)
            left_child_index = self.find_left_child(current_index)
            right_child_index = self.find_right_child(current_index)

            if left_child_index < len(self.heap):
                left_child = Node(self.heap[left_child_index])
                current_node.left = left_child
                queue.append((left_child, left_child_index))

            if right_child_index < len(self.heap):
                right_child = Node(self.heap[right_child_index])
                current_node.right = right_child
                queue.append((right_child, right_child_index))

        return self.root


###################################################### linked list ######################################################

class SingleNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, data):
        new_node = SingleNode(data)
        new_node.next = self.head
        self.head = new_node
        self.size = self.size  + 1  

    def insert_at_end(self, data):
        new_node = SingleNode(data)
        self.size = self.size  + 1 
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def insert_after_node(self, prev_node, data):
        self.size = self.size  + 1 
        if prev_node is None:
            print("Previous node is not in the list.")
            return
        new_node = SingleNode(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, data):
        if self.head is None:
            print("The linked list is empty.")
            return

        if self.head.data == data:
            self.size = self.size  - 1 
            self.head = self.head.next
            return

        current = self.head
        prev = None
        while current is not None and current.data != data:
            prev = current
            current = current.next

        if current is None:
            print("The specified data is not found in the list.")
            return

        prev.next = current.next

    def search(self, data):
        this = LinkedList()
        this.head = current
        current = self.head
        cur2 = this.head
        while current is not None:
            if current.data == data:
                return this
            current = current.next
            cur2 = cur2.next
        return self

    def display(self):
        if self.head is None:
            print("The linked list is empty.")
            return

        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()



###################################################### Flask ############################################################

bst = BinarySearchTree()
max_heap = MaxHeap()
min_heap = MinHeap()
linked_list = LinkedList()


# Flask route for the main page
@app.route('/')
def main():
    return render_template('main.html')

##################################### Flask route for the Bst page ###############################
@app.route('/tree_visualizer', methods=['GET', 'POST'])
def visualize_tree():
    if request.method == 'POST':
        action = request.form['action']
        if action == 'add':
            node_value = int(request.form['node_value'])
            flash('Adding ' + str(node_value))
            bst.add(node_value)
        if request.method == 'POST':
            action = request.form['action']
            if action == 'Another':
                return redirect(url_for('main'))
            
        elif action == 'remove':
            node_value = int(request.form['node_value'])
            flash('Removing ' + str(node_value))
            bst.remove(node_value)

        elif action == 'Search':
            node_value = int(request.form['node_value'])
            bst2 = BinarySearchTree()
            result = bst.searchNode(node_value)
            bst2.root = bst.search
            if result != node_value:
                flash(str(node_value) + ' is not in the Binary Search Tree')
            else:
                flash('Searching for ' + str(node_value))
                return render_template('tree_visualizer.html', bst=bst2)

        elif action == 'inorder_traverse':
            bst.inorder_result = []  # Clear previous results
            bst.inorder_traverse()
            flash('Inorder Traversal: ' + ', '.join(map(str, bst.inorder_result)))

        elif action == 'preorder_traverse':
            bst.preorder_result = []  # Clear previous results
            bst.preorder_traverse()
            flash('Preorder Traversal: ' + ', '.join(map(str, bst.preorder_result)))

        elif action == 'postorder_traverse':
            bst.postorder_result = []  # Clear previous results
            bst.postorder_traverse()
            flash('Postorder Traversal: ' + ', '.join(map(str, bst.postorder_result)))

        elif action == 'find_min' and bst.root == None:
            flash('Root is Null')

        elif action == 'find_min':
            flash('The Min is ' +  str(bst._find_min()))

        elif action == 'find_Max' and bst.root == None:
            flash('Root is Null')

        elif action == 'find_Max':
            flash('The Max is ' + str(bst._find_max()))

    return render_template('tree_visualizer.html', bst=bst)

##################################### Flask route for the Main page ###############################

# Flask route for handling the button click event
@app.route('/select_data_structure', methods=['POST'])
def select_data_structure():
    data_structure = request.form['data_structure']
    if data_structure == 'BST':
        return redirect(url_for('visualize_tree'))
    elif data_structure == 'Max':
        return redirect(url_for('max_heap_visualizer'))
    elif data_structure == 'Min':
        return redirect(url_for('min_heap_visualizer'))
    elif data_structure == 'Linked':
        return redirect(url_for('linked_list_visualizer'))
    else:
        # Handle other data structures as needed
        return redirect(url_for('main'))
    
    
##################################### Flask route for the Max Heap page ###############################

# Flask route for the Max Heap page
@app.route('/max_heap' , methods=['GET', 'POST'] )
def max_heap_visualizer():
    
    if request.method == 'POST':
        action = request.form['action']
        if action == 'Insert':
            node_value = int(request.form['node_value'])
            max_heap.insert(node_value)
        if action == 'Delete':
            node_value = int(request.form['node_value'])
            max_heap.delete(node_value)
        if request.method == 'POST':
            action = request.form['action']
            if action == 'Another':
                return redirect(url_for('main'))
        if action == 'find-parent':
            node_value = int(request.form['node_value'])
            try:
                parent = max_heap.find_parent_element(node_value)
                flash(f'Index of ({node_value}) is {max_heap.heap.index(node_value)} then the index of the parent is ({max_heap.heap.index(node_value)}- 1) // 2  = {parent} which is {max_heap.heap[parent]}', category='inst')
            except ValueError:
                flash(f'Node {node_value} is not in the max heap.', category='inst')

        if action == 'FindLeftchild':
            node_value = int(request.form['node_value'])
            try:
                parent = max_heap.find_left_child_element(node_value)
                flash(f'Index of ({node_value}) is {max_heap.heap.index(node_value)} then the index of the left child is (2 *{max_heap.heap.index(node_value)}) + 1  = {parent} which is {max_heap.heap[parent]}', category='inst')

            except ValueError:
                flash(f'Node {node_value} is not in the max heap.', category='inst')


        if action == 'FindRightchild':
            node_value = int(request.form['node_value'])
            try:
                parent =  max_heap.find_right_child_element(node_value)
                flash(f'Index of ({node_value}) is {max_heap.heap.index(node_value)} then the index of the left child is ({max_heap.heap.index(node_value)} - 1) // 2  = {parent} which is {max_heap.heap[parent]}', category='inst')

            except ValueError:
                flash(f'Node {node_value} is not in the max heap.', category='inst')
            
    max_heap.make_binary_tree()
    flash('[' + ', '.join(map(str, max_heap.heap)) + ']', category='max_heap_array')
    return render_template('max-heap.html', bst=max_heap)

##################################### Flask route for the Min Heap page ###############################

# Flask route for the min Heap page
@app.route('/min_heap' , methods=['GET', 'POST'] )
def min_heap_visualizer():
    
    if request.method == 'POST':
        action = request.form['action']
        if action == 'Insert':
            node_value = int(request.form['node_value'])
            min_heap.insert(node_value)
        if action == 'Delete':
            node_value = int(request.form['node_value'])
            min_heap.delete(node_value)
        if action == 'find-parent':
            node_value = int(request.form['node_value'])
            try:
                parent = min_heap.find_parent_element(node_value)
                flash(f'Index of ({node_value}) is {min_heap.heap.index(node_value)} then the index of the parent is ({min_heap.heap.index(node_value)}- 1) // 2  = {parent} which is {min_heap.heap[parent]}', category='inst')
            except ValueError:
                flash(f'Node {node_value} is not in the min heap.', category='inst')

        if action == 'FindLeftchild':
            node_value = int(request.form['node_value'])
            try:
                parent = min_heap.find_left_child_element(node_value)
                flash(f'Index of ({node_value}) is {min_heap.heap.index(node_value)} then the index of the left child is (2 *{min_heap.heap.index(node_value)}) + 1  = {parent} which is {min_heap.heap[parent]}', category='inst')

            except ValueError:
                flash(f'Node {node_value} is not in the min heap.', category='inst')


        if action == 'FindRightchild':
            node_value = int(request.form['node_value'])
            try:
                parent =  min_heap.find_right_child_element(node_value)
                flash(f'Index of ({node_value}) is {min_heap.heap.index(node_value)} then the index of the left child is ({min_heap.heap.index(node_value)} - 1) // 2  = {parent} which is {min_heap.heap[parent]}', category='inst')

            except ValueError:
                flash(f'Node {node_value} is not in the min heap.', category='inst')

        if request.method == 'POST':
            action = request.form['action']
            if action == 'Another':
                return redirect(url_for('main'))
            
    min_heap.make_binary_tree()
    flash('[' + ', '.join(map(str, min_heap.heap)) + ']', category='min_heap_array')
    return render_template('min-heap.html', bst=min_heap)

#######################################################################################################
@app.route('/linked-list', methods=['GET', 'POST'])
def linked_list_visualizer():
    # Perform operations on the linked list (insertion, deletion, etc.)
    # ...
    
    if request.method == 'POST':
        action = request.form['action']
        if action == 'Another':
            return redirect(url_for('main'))
        
        if action == 'Insert_at_beginning':
            node_value = int(request.form['node_value'])
            linked_list.insert_at_beginning(node_value)

        if action == 'Insert_at_end':
            node_value = int(request.form['node_value'])
            linked_list.insert_after_node(node_value)

        if action == 'Insert_after_node':
            node_value = int(request.form['node_value'])
            node_value2 = int(request.form['node_value2'])
            linked_list.insert_after_node(node_value, node_value2)

        if action == 'Delete_node':
            node_value = int(request.form['node_value'])
            linked_list.delete_node(node_value)

        if action == 'Search':
            node_value = int(request.form['node_value'])
            linked_list.search(node_value)
        
    linked_list.display()  # Output: 22 15 10

    return render_template('linked-list.html', linked_list=linked_list)


###################################################### Main ######################################################
if __name__ == '__main__':
    app.run()
