class Pair:
    def __init__(self, key, value):
        self.key = key
        self.val = value


class HashTable:
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.map = [None] * capacity
        # open addressing case with tombstone implementation
        self.DELETED = object()

    def insert(self, key: int, value: int) -> None:

        probes = 0

        index = self.hash(key)

        deleted_index = None

        while True:
            while self.map[index] != None and probes < self.capacity:
                if self.map[index] is self.DELETED:
                    if deleted_index is None:
                        deleted_index = index

                elif self.map[index].key == key:
                    modify_val = self.map[index]
                    modify_val.val = value
                    return

                index = (index + 1) % self.capacity
                probes += 1

            if self.size + 1 >= 0.5 * self.capacity:
                self.resize()
                index = self.hash(key)
                deleted_index = None
                probes = 0
            elif deleted_index is not None:
                self.map[deleted_index] = Pair(key, value)
                self.size += 1
                return
            else:
                self.map[index] = Pair(key, value)
                self.size += 1
                return

    def get(self, key: int) -> int:
        index = self.hash(key)
        deleted_index = None
        probe = 0

        while self.map[index] != None and probe < self.capacity:
            if self.map[index] is self.DELETED:
                if deleted_index is None:
                    deleted_index = index
            elif self.map[index].key == key:
                return self.map[index].val
            probe += 1
            index = (index + 1) % self.capacity

        return -1

    def remove(self, key: int) -> bool:
        index = self.hash(key)
        probe = 0

        if self.get(key) == -1:
            return False

        while probe < self.capacity:
            if self.map[index].key == key:
                self.map[index] = self.DELETED
                self.size -= 1
                return True
            else:
                index = (index + 1) % self.capacity
                probe+=1

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:

        self.capacity = self.capacity * 2

        newMap = [None] * self.capacity

        oldMap = self.map

        self.map = newMap

        self.size = 0

        for pair in oldMap:
            if pair == self.DELETED or pair == None:
                continue
            else:
                self.insert(pair.key, pair.val)

    def hash(self, key) -> int:
        return key % self.capacity
