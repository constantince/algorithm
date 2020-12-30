class Node: 
    ''' 
        link list's node
    '''
    def __init__(self, node):
        self.item = node
        self.next = None

class LinkList:
    '''
        linked list for algorithm
    '''
    def __init__(self):
        self.head = None
        self.len = 0

    def reverse(self):
        pass

    def is_empty(self):
        return self.head is None

    def append(self, node):
        if self.head is None:
            self.head = Node(node)
        else:
            cur = self.head
            while cur is not None:
                if cur.next is not None:
                    cur = cur.next
                else:
                    cur.next = Node(node)
                    cur = None
        self.len = self.len + 1

    def remove(self, node):
        cur = self.head
        if cur.item == node:
            self.head = cur.next
            return
        
        while cur is not None:
            if cur.next is not None and cur.next.item  == node:
                cur.next = cur.next.next
                return
            elif cur.next is None:
                return False
            else:
                cur = cur.next

    def count(self):
        count = 0
        cur = self.head
        while cur is not None:
            count = count + 1
            if(cur.next is None):
                return count
            else:
                cur = cur.next
        return count

    def find(self, node):
        cur = self.head
        while cur is not None:
            if cur.item == node:
                return cur
            else:
                cur = cur.next

    def insert_before(self, node):
       pass

    def insert_after(self, node):
       pass

    def __str__(self):
        return str(self.head)

if __name__ == "__main__":
    print("start test")

    lk = LinkList()

    print(lk.count())

    print(lk.is_empty())

    lk.append(1)

    lk.append(2)

    print(lk.count())
    print(lk)

    lk.append(9)
    lk.append(10)

    print(lk.count())

    lk.remove(1)

    print('link list length is {} now'.format(lk.count()))


    
