import hashlib
import math
from Link import LinkList

end = 10
class HashTable: 
    def __init__(self):
        self.table = [None] * end

    def get(self, key) -> list:
        i = self.hashFunction(str(key))
        old_link = self.table[i]
        cur = old_link.head
        while cur.item is not None:
            if cur.item["k"] is key:
                return cur.item["value"]
            else:
                cur = cur.next

    def hashFunction(self, content) -> int:
        md5 = hashlib.md5(content.encode(encoding='UTF-8')).hexdigest()
        index = math.floor(float.fromhex(md5[:1]))
        length = len(self.table) - 1
        index = index if index < length else length
        return index
    # 寻址法
    def findNextNotNone(self, start: int) -> int:
        n = start
        count = 1
        end = len(self.table)
        while count < end:
            n = n if n < end else n - end
            if self.table[n] is not None:
                count += 1
                n += 1
                continue
            else:
                return n

    # 链表插入法
    def insertLinkList(self, new_item, key, i):
        old_lk = self.table[i]
        if old_lk is not None:
            old_lk.append({"k":key, "value":new_item})
        else:
            lk = LinkList()
            lk.append({"k":key, "value":new_item})
            self.table[i] = lk

    def set(self, key, value):
        i = self.hashFunction(str(key))
        print('{} is index'.format(i))
        self.insertLinkList(value, key, i)
        '''
        
        if self.table[i] is None:
            self.table[i] = value
        else:
            next = self.findNextNotNone(i)
            self.table[next] = value
        '''

    def __str__(self):
        return str(self.table)


if __name__ == "__main__":
    h = HashTable()
    h.set('hello world', 'anny')
    h.set('hello world333', 'aacvranny2222')
    h.set('hello worl33', 'anny1')
    h.set('hello worl444', 'anny1')
    print(h.get('hello world333'))
    print(h)