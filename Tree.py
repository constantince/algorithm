class Node:
    def __init__(self, item) -> None:
        self.ele = item
        self.left = None
        self.right = None

class Tree:
    def __init__(self, root) -> None:
        self.root = Node(root)
        return self.root

    def add(self, item):
        if self.root:
            if item < self.root.ele:
                if self.root.right is None:
                    self.root.right = Tree(item)
                else:
                    self.root.right.add(item)
            elif item > self.root.ele:
                if self.root.left is None:
                    self.root.left = Tree(item)
                else:
                    self.root.left.add(item)
            else:
                self.root = item

    def __str__(self) -> str:
        return str(self.root)

if __name__ == "__main__":
    tree = Tree("tree-root")
    for i in range(1, 8):
        tree.add(i)

    print(tree)
