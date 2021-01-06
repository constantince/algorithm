class Node:
    def __init__(self, item) -> None:
        self.ele = item
        self.left = None
        self.right = None

class Tree:
    def __init__(self, root) -> None:
        self.root = Node(root)

    def add(self, item):
        node = Node(item)
        cur = self.root
        while cur is not None:
            if cur.left is None:
                cur.left = node
                return
            elif cur.right is None:
                cur.right = node
                return
            else:
                cur = cur.left

    def __str__(self) -> str:
        return str(self.root)

if __name__ == "__main__":
    tree = Tree("tree-root")
    for i in range(1, 8):
        tree.add(i)

    print(tree)
