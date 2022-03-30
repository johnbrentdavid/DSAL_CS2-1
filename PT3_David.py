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
            print("------------------------\nData Already Existing!\nFailed to Insert!\n------------------------")
            return
        elif data < self.data:
            #add data to the left subtree
            if self.left:
                self.left.add_child(data)#recursive call till it is the left leaf
            else:
                self.left = BinarySearchTreeNode(data)#command to add the data to the node
                print("------------------------\nSuccessfully Inserted!\n------------------------")
        #add data to the right subtree
        elif data >self.data:
            if self.right:
                self.right.add_child(data)#recursive call till it is the right leaf
            else:
                self.right = BinarySearchTreeNode(data)#command to add the data to the node
                print("------------------------\nSuccessfully Inserted!\n------------------------")

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

    #these 2 functions can be used alternatively for deleting functions 
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
        #the first 'if' is to recursion call the left subtree
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        #the 2nd 'if' is to recursion call the right subtree
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        #if for if the delete value == current value
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right
            #gets the right sub tree min val then swap
            min_val=self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        return self

#function call for the building the tree can can also be used for string values
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range (1,len(elements)):
        root.add_child(elements[i])

    return root

#START
if __name__ == '__main__':
    #NOTES: I initialized a tree that is evenly spread so that the time complexity is better
    #Set 50 as the root node so that it would be even from the beginning
    numbers = [50,30,80,20,70,90,40,10,60]
    numbers_tree = build_tree(numbers)
    repeat = True
    while repeat:
        app = int(input("What application would you like to use?\n[1]Search\t[2]Insert\n[3]Delete\t[4]Print Tree\n[0]EXIT\nDecision : "))
        if app == 1:
            print("------------------------")
            num = int(input("Search : "))
            if numbers_tree.search(num):
                print("========================\nYES! It is on the list :D\n========================")
            else:
                print("========================\nNO! It is not on the list T_T\n========================")
        elif app == 2:
            print("------------------------")
            num = int(input("Insert : "))
            numbers_tree.add_child(num)
        elif app == 3:
            print("------------------------")
            num = int(input("Delete : "))
            numbers_tree.delete(num)
            print("========================\nIO : ",numbers_tree.in_order_traversal(),"\n========================")
        elif app == 4:
            print("========================\nIO : ",numbers_tree.in_order_traversal())
            print("Pre-O : ",numbers_tree.pre_order_traversal())
            print("Post-O : ",numbers_tree.post_order_traversal(),"\n========================")
        elif app == 0:
            break