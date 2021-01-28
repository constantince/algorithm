# import queue

from typing import Match


class Node:
    def __init__(self, item) -> None:
        self.value = item
        self.left = None
        self.right = None
        self.father = None

class Tree:
    def __init__(self, root) -> None:
        self.root = Node(root)
        self.heap = [None, root]
    #!!!普通二叉树添加子节点
    def binary_tree_add(self, node):
        queue = [self.root]
        while queue:
            cur = queue.pop(0)
            if cur.left is None:
                cur.left = node
                node.father = cur
                return
            queue.append(cur.left)
            if cur.right is None:
                cur.right = node
                node.father = cur
                return
            queue.append(cur.right)

    #搜索二叉树添加子节点    
    def search_tree_add(self, node):
        father = None
        cur = self.root
 
        while cur != None:
            if cur.value == node.value:
                return -1
            father = cur
            if node.value < cur.value:
                cur = cur.left
            else:
                cur = cur.right
        node.father = father
        if father == None:
            self.root = node
        elif node.value < father.value:
            father.left = node
        else:
            father.right = node
        
    def pre_order(self, node, q):
        if node.left is not None: 
            print(node.left.value)
            q.append(node.left)
        if node.right is not None:
            print(node.right.value)
            q.append(node.right)

    def in_order(self, node, q):
        if node.right is not None: 
            print(node.right.value)
            q.append(node.right)
        if node.left is not None:
            print(node.left.value)
            q.append(node.left)
        pass

    def post_order(self):
        pass

    #前序遍历
    def search_tree_pre_order(self, node):
        if node is None:
            return
        print(node.value)
        self.search_tree_pre_order(node.left)
        self.search_tree_pre_order(node.right)
       
    #中序遍历
    def search_tree_in_order(self, node):
        if node is None:
            return
        self.search_tree_in_order(node.left)
        print(node.value)
        self.search_tree_in_order(node.right)
        
    #后序遍历
    def search_tree_post_order(self, node):
        if node is None:
            return
        self.search_tree_post_order(node.left)
        self.search_tree_post_order(node.right)
        print(node.value)

    #判断插入的是左节点还是右节点
    def l_o_r(self, target):
        return int(target / 2 ) if target % 2 == 0 else int((target + 1) / 2)  

    def heapily(self, node):
        self.heap.append(node)
        length = len(self.heap)
        me = length - 1
        father = self.l_o_r(me)

        while father >= 0 and self.heap[me] > self.heap[father]:
            self.swap(me, father)
            me = father
            father = self.l_o_r(me)

    def swap(self, old_index, new_index):
        old = self.heap[old_index]
        new = self.heap[new_index]
        self.heap[old_index] = new
        self.heap[new_index] = old


    def __str__(self) -> str:
        return str(self.root)

#[None, 7,5,6,4,2,1]
if __name__ == "__main__":
    tree = Tree("A")
    alt = ["B", "C", "D", "E", "F", "G"]
    for i in alt:
        tree.binary_tree_add(Node(i))

    tree.search_tree_pre_order(tree.root)

    heap = Tree(0)
    for i in [9, 4, 6, 7, 3, 1]:
        heap.heapily(i)
    heap.heapily(20)
    print(heap.heap)
    
   
