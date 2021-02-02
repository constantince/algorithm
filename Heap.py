class Heap:
    def __init__(self, root) -> None:
        self.root = root
        self.heap = [None, root]
    pass

    #判断插入的是左节点还是右节点
    def l_o_r(self, target):
        return int(target / 2 ) if target % 2 == 0 else int((target + 1) / 2)  

    def heapily_from_bottom(self, node):
        self.heap.append(node)
        length = len(self.heap)
        me = length - 1
        father = self.l_o_r(me)

        while father >= 0 and self.heap[me] > self.heap[father]:
            self.swap(me, father)
            me = father
            father = self.l_o_r(me)

    def heapily_from_top(self, node):
        lens = len(self.heap)
        if node > self.heap[1]:
            cur = self.heap[1]
            self.heap[1] = node
        else:
            cur = node
        i = 1
        while i < lens:
            x = cur
            if 2 * i <= lens and self.heap[2 * i] <= cur:
                i = i * 2
                cur = self.heap[i]
                self.heap[i] = x
            elif 2 * i + 1 <= lens and self.heap[2 * i + 1] <= cur:
                i = 2 * i + 1
                cur = self.heap[i]
                self.heap[i] = x
            else:
                self.heap.append(cur)
                break
        


    def swap(self, old_index, new_index):
        old = self.heap[old_index]
        new = self.heap[new_index]
        self.heap[old_index] = new
        self.heap[new_index] = old

    def delete(self, node):
        self.heap.remove(node)
        tar = self.heap[len(self.heap) - 1]
        self.heapily_from_top(tar)

if __name__ == "__main__":
    heap = Heap(0)
    for i in [9, 4, 6, 7, 3, 1]:
        heap.heapily_from_bottom(i)
    heap.heapily_from_bottom(20)
    
    print(heap.heap)
    #[None, 20, 9, 6, 7, 0, 3, 1, 4]


    heap.heapily_from_top(8)
    print(heap.heap)

    heap.delete(9)
    print(heap.heap)
