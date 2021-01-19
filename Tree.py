# import queue

class Node:
    def __init__(self, item) -> None:
        self.value = item
        self.left = None
        self.right = None
        self.father = None

class Tree:
    def __init__(self, root) -> None:
        self.root = Node(root)
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
        
    def pre_order(self, node):
        if node.left is not None: 
            print(node.left.value)
        if node.right is not None:
            print(node.right.value)

        self.pre_order(node.left)

    def search_tree_pre_order(self):
        cur = self.root
        if cur.left is not None: 
            self.pre_order(cur.left)

        if cur.left is not None: 
            self.pre_order(cur.right)



    def __str__(self) -> str:
        return str(self.root)

if __name__ == "__main__":
    tree = Tree(0)
    for i in range(1, 12):
        tree.binary_tree_add(Node(i))

    tree.search_tree_pre_order()
