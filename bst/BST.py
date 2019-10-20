#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 10:27:21 2019

@author: ben
"""
import queue

class TreeNode():
    def __init__(self, value):
        self.value = value 
        self.left = None
        self.right = None

#cancel the root? 
class BST():
    def __init__(self):
        self.root = None
    def find(self, root, v):
        if not root:
            return None
        if root.value == v:
            return root
        # left
        if v < root.value:
            return self.find(root.left, v)
        #right
        return self.find(root.right, v)
    
    def insert(self, root, v):
        if not root:
            return TreeNode(v)
        
        if v < root.value:
            root.left = self.insert(root.left, v)
            
        if v > root.value:
            root.right = self.insert(root.right, v)
        return root
    
    def maximum(self, root) :
        if not root:
            return None
        if not root.right:
            return root
        return self.maximum(root.right)
    
    def minimum(self, root):
        if not root:
            return None
        
        if not root.left:
            return root
        
        return self.minimum(root.left)
        

    def predecessor(self, root, v):
        r = self.find(root, v)
        if not root :
            return None
        
        return self.maximum(r.left)
    
    ### this program has a problem 
    def successor_recursive(self, parent, root, v):    
        if not root:
            return None
        
        if root.value == v:
            if not root.right:
                return parent if parent.value > v else None
            else:    
                return self.minimum(root.right)
        #right
        if v > root.value :
            return self.successor_recursive(root, root.right, v)
        
        #left
        return self.successor_recursive(root, root.left, v)
            
        
    def successor(self, root, v):
        return self.successor_recursive(None, root, v)

    def delete(self, root, v):
        return self.delete_recursive(None, root, v)
        
    ## totally three cases 
    def delete_recursive(self, parent, root, v):
        if not root:
            return False 
        
        if v < root.value:
            return self.delete_recursive(root, root.left, v)
        if v > root.value:
            return self.delete_recursive(root, root.right, v)
        
        #root.value= v, begin delete, three cases
        if not root.left and not root.right:
            self.delete_node_no_child(parent, root)
        elif not root.left or not root.right:
            self.delete_node_one_child(parent, root)
        else:
            self.delete_node_two_child(parent, root)
        
        return True
    
    
    def delete_node_no_child(self, parent, root):
        if root.value > parent.value:
            parent.right = None
        else:
            parent.left = None
        
    ## here may has some problems
    def delete_node_one_child(self, parent, root):
        child = root.left if root.left != None else root.right
        if root.value > parent.value:
            parent.right = child
        else:
            parent.left = child
    
    def delete_node_two_child(self, parent, root):
        l = self.findSuccessor(root, root.right)

        suc_parent = l[0]
        suc = l[1]
        
        suc_value  = suc.value
        if not suc.left and not suc.right:
            self.delete_node_no_child(suc_parent, suc) 
        else: 
            self.delete_node_one_child(suc_parent, suc)
        root.value = suc_value
        
    def findSuccessor(self, parent, root):
        if not root.left:
            return [parent, root]
        
        return self.findSuccessor(root, root.left)



## this is for test
def is_binary_tree(root):
    if not root:
        return True
    if root.left != None and root.left.value >= root.value:
        return False
    if root.right != None and root.right.value <= root.value:
        return False
    
    return is_binary_tree(root.left) and is_binary_tree(root.right)

## this is for test too
def BFS(root):
    q = queue.Queue()
    
    q.put(root)
    while not q.empty():
        buffer=[]
        while not q.empty():
            buffer.append(q.get())
        
        for i in buffer:
            print(i.value,  end = ' ')
            if i.left:
                q.put(i.left)
            if i.right:
                q.put(i.right)
        buffer.clear()
        print()
            
    
if __name__ == '__main__':
    bst = BST()
    # test of insert and find
    bst.root = bst.insert(None, 8)
    r = bst.root
    print(bst.find(r, 8) != None, " value=", bst.find(r, 8).value)
    
    bst.insert(r, 5)
    print(bst.find(r, 5) !=None, " value=", bst.find(r, 5).value)
    
    bst.insert(r, 13)
    print(bst.find(r, 13) !=None, " value=", bst.find(r, 13).value)
    
    print(is_binary_tree(r) == True)
    
    bst.insert(r, 2)
    bst.insert(r, 6)
    bst.insert(r, 7)
    bst.insert(r, 13)
    bst.insert(r, 10)
    
    ## max and min test
    print("maximum ret:", bst.maximum(r).value == 13) 
    print("minimum ret:", bst.minimum(r).value == 2) 
    
    ## predecessor test
    print("predecessor ret:", bst.predecessor(r, 5).value == 2)
    print("predecessor ret:", bst.predecessor(r, 13).value == 10)
    print("predecessor ret:", bst.predecessor(r, 2) == None)

    BFS(r)
    print("successor ret:", bst.successor(r, 5).value == 6)
    print("successor ret:", bst.successor(r, 13) == None)
    print("successor ret:", bst.successor(r, 2).value == 5)
     
    ## delete testt
    # detele node with two child
    print(bst.delete(r, 5) == True)
    print(bst.find(r,5) == None)
    BFS(r) 
    
    #delete node with one child
    print(bst.delete(r, 6) == True)
    print(bst.find(r,6) == None)
    BFS(r) 

    #delete node with zero child
    print(bst.delete(r, 2) == True)
    print(bst.find(r,2) == None)
    BFS(r) 
    
    
    
    
    