import hashlib
import math
end = 10
class HashTable: 
    def __init__(self):
        self.table = [None] * end

    def get(self, key) -> list:
        i = self.hashFunction(str(key))
        return self.table[i]

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
            
    def set(self, key, value):
        i = self.hashFunction(str(key))
        print('{} is index'.format(i))
        if self.table[i] is None:
            self.table[i] = value
        else:
            next = self.findNextNotNone(i)
            self.table[next] = value

    def __str__(self):
        return str(self.table)


if __name__ == "__main__":
    h = HashTable()
    h.set('hello world', 'anny')
    h.set('hello world333', 'aacvranny2222')
    h.set('hello worl33', 'anny1')
    print(h.get('hello world'))
    print(h)