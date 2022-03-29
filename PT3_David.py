class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def in_order_traversal(self):
        elements = []
        #visit left tree first
        if self.left:
            elements += self.left.in_order_traversal()
        #visit the base node
        elements.append(self.data)
        #visit the right subtree
        if self.right:
            elements += self.right.in_order_traversal()
        return elements
    
    def pre_order_traversal(self):
        elements = []
        #visit the base node
        elements.append(self.data)
        #visit left tree first
        if self.left:
            elements += self.left.in_order_traversal()
        #visit the right subtree
        if self.right:
            elements += self.right.in_order_traversal()
        return elements
    
    def post_order_traversal(self):
        elements = []
        #visit left tree first
        if self.left:
            elements += self.left.in_order_traversal()
        #visit the right subtree
        if self.right:
            elements += self.right.in_order_traversal()
        #visit the base node
        elements.append(self.data)
        return elements
    
    #INSERT FUNCTION
    def add_child(self,data):
        if data == self.data:
            return
        elif data < self.data:
            #add data to the left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        elif data >self.data:
            #add data to the right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    #SEARCH FUNCTION
    def search(self,val):
        if val==self.data:
            return True
        elif val < self.data:
            #the value might be on the left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False
        elif val > self.data:
            #the value might be on the right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    def find_max(self):
        if self.right is None:
            return self.data
        return self.left.find_max()

    #DELETE FUNCTION
    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right
            #Kinukuha nya yung right mini value tas ipapalit dun sa idedelete
            min_val=self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
            
        return self

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range (1,len(elements)):
        root.add_child(elements[i])

    return root

#START
if __name__ == '__main__':
    numbers = [17,4,1,20,9,23,18,34]
    numbers_tree = build_tree(numbers)
    print("IO : ",numbers_tree.in_order_traversal())
    print("Pre-O : ",numbers_tree.pre_order_traversal())
    print("Post-O : ",numbers_tree.post_order_traversal())