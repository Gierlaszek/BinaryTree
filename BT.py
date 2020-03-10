import  statistics

# example tree:
#               5
#           /       \
#          3          7
#         /  \      /   \
#        2    5    1     0
#                       / \
#                      2   8
#                           \
#                           5

#################################
# Represent a node of binary tree
#################################
class Node:
    def __init__(self, data):
        # Assign data to the new node, set left and right children to None
        self.data = data
        self.left = None
        self.right = None


###################################
# Represent the root of binary tree
###################################
class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)
        self.result = {}

    def print_tree(self):
        return self.pre_order(tree.root, [])

    ####################################
    # method which create tree traversal
    ####################################
    def pre_order(self, start, traversal):
        """Root->Left->Right"""
        if start:
            traversal.append(start.data)
            traversal = self.pre_order(start.left, traversal)
            traversal = self.pre_order(start.right, traversal)
        return traversal

    ##########################################
    # method to search node in the binary tree
    ##########################################
    def searchNode(self, temp, value):
        # Check whether tree is empty
        if (self.root == None):
            print("Tree is empty")

        else:
            # If value is found
            if (temp.data == value):
                global result
                result = self.calculations(temp)
                return

                # Search in left subtree
            if (temp.left != None):
                self.searchNode(temp.left, value)

                # Search in right subtree
            if (temp.right != None):
                self.searchNode(temp.right, value)

    #######################################################
    # calculates the sum, average value, and median subtree
    #######################################################
    def calculations(self, value):
        subtree = (self.pre_order(value, []))
        sum_subtree = sum(subtree)
        averageValue = sum_subtree / len(subtree)
        median = statistics.median(subtree)
        result = {"sum": sum_subtree, "average":averageValue, "median":median}
        return result



global result
# #create root of Tree and add start value
tree = BinaryTree(5)
# # # Add nodes to the binary tree
tree.root.left = Node(3)
tree.root.right = Node(7)
tree.root.left.left = Node(2)
tree.root.left.right = Node(5)
tree.root.right.left = Node(1)
tree.root.right.right = Node(0)
tree.root.right.right.left = Node(2)
tree.root.right.right.right = Node(8)
tree.root.right.right.right.right = Node(5)

resul = tree.searchNode(tree.root, 3)
print(result)
