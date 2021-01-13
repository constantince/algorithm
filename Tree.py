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
        
        
    def __str__(self) -> str:
        return str(self.root)

if __name__ == "__main__":
    tree = Tree(0)
    for i in range(1, 20):
        tree.binary_tree_add(Node(i))

    print(tree.root)
