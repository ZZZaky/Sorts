count_if = 0
count_change_main = 0
count_change_temp = 0

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self, value):
        global count_if
        global count_change_temp
        if self.value:
            count_if += 1
            if value < self.value:
                count_if += 1
                if self.left is None:
                    count_if += 1
                    self.left = Node(value)
                    count_change_temp += 1
                else:
                    count_if += 1
                    self.left.insert(value)
            elif value > self.value:
                count_if += 1
                if self.right is None:
                    count_if += 1
                    self.right = Node(value)
                    count_change_temp += 1
                else:
                    count_if += 1
                    self.right.insert(value)
        else:
            self.value = value
            count_change_temp += 1

def tree_to_array(root, result):
    global count_if
    global count_change_temp
    if root:
        count_if += 1
        tree_to_array(root.left, result)
        result.append(root.value)
        count_change_temp += 1
        tree_to_array(root.right, result)

def Tree_sort(array):
    global count_if
    if len(array) == 0:
        count_if += 1
        return array
    
    root = Node(array[0])
    for i in range(1, len(array)):
        root.insert(array[i])
    result = []
    tree_to_array(root, result)

    return {'comparsion': int(count_if), 'change in main array': int(count_change_main), 'change in temporary array': int(count_change_temp)}