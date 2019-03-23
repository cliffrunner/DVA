from util import entropy, information_gain, partition_classes, find_best_split, class_counts
import numpy as np 
import ast

class DecisionTree(object):
    def __init__(self):
        # Initializing the tree as an empty dictionary or list, as preferred
        #self.tree = []
        #self.tree = {}
        self.tree = None
        pass

    def learn(self, X, y):
        # TODO: Train the decision tree (self.tree) using the the sample X and labels y
        # You will have to make use of the functions in utils.py to train the tree
        
        # One possible way of implementing the tree:
        #    Each node in self.tree could be in the form of a dictionary:
        #       https://docs.python.org/2/library/stdtypes.html#mapping-types-dict
        #    For example, a non-leaf node with two children can have a 'left' key and  a 
        #    'right' key. You can add more keys which might help in classification
        #    (eg. split attribute and split value)
        best_gain, best_attr, best_val = find_best_split(X,y)
        if best_gain == 0:
            return Leaf(y)
        
        X_left, X_right, y_left, y_right = partition_classes(X, y, best_attr, best_val)
        left = self.learn(X_left, y_left)
        right = self.learn(X_right, y_right)
        self.tree = Node([best_attr,best_val], left, right)
        return self.tree


    def classify(self, record):
#        preds = []
#        for record in records:
#            preds.append(self._classify(record))
#        return preds
        tree = self.tree
        while True:
            best_attr, best_val = tree.split[0], tree.split[1]
            if type(record[best_attr])==str:
                if record[best_attr]==best_val:
                    if isinstance(tree.left, Leaf):
                        return tree.left.predictions
                    else:
                        tree = tree.left
                else:
                    if isinstance(tree.right, Leaf):
                        return tree.right.predictions
                    else:
                        tree = tree.right
            else:
                if record[best_attr]<=best_val:
                    if isinstance(tree.left, Leaf):
                        return tree.left.predictions
                    else:
                        tree = tree.left
                else:
                    if isinstance(tree.right, Leaf):
                        return tree.right.predictions
                    else:
                        tree = tree.right
    
#    def _classify(self, record):
#        tree = self.tree
#        while True:
#            best_attr, best_val = tree.split[0], tree.split[1]
#            if type(record[best_attr])==str:
#                if record[best_attr]==best_val:
#                    if isinstance(tree.left, Leaf):
#                        return tree.left.predictions
#                    else:
#                        tree = tree.left
#                else:
#                    if isinstance(tree.right, Leaf):
#                        return tree.right.predictions
#                    else:
#                        tree = tree.right
#            else:
#                if record[best_attr]<=best_val:
#                    if isinstance(tree.left, Leaf):
#                        return tree.left.predictions
#                    else:
#                        tree = tree.left
#                else:
#                    if isinstance(tree.right, Leaf):
#                        return tree.right.predictions
#                    else:
#                        tree = tree.right
        

class Leaf(object):
    def __init__(self, y):
        self.predictions = round(sum(y)/len(y)) # class_counts(y)


class Node(object):
    def __init__(self, split, left, right):
        self.split = split
        self.left = left
        self.right = right