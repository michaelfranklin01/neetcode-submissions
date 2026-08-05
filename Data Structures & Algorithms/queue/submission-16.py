# doubly linked list node
class Node:
    def __init__(self, value: int, prev_node= None, next_node= None):
        self.val = value
        self.next = next_node
        self.prev = prev_node
class Deque:
    def __init__(self):
        """
        sentinel solution head -> real nodes <- tail everything gets inserted
        between dummy nodes

        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

        """

        # non sentinal version
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self) -> bool:
        """
        sentinel:
        return self.head == self.tail

        """
        return self.size == 0

    def append(self, value: int) -> None:
         
        if self.size == 0:
            self.head = Node(value)
            self.tail = self.head
            self.size += 1
        else:
            self.tail.next = Node(value, self.tail)
            self.tail = self.tail.next
            self.size += 1

    def appendleft(self, value: int) -> None:
        if self.size == 0:
            self.head = Node(value)
            self.tail = self.head
            self.size += 1
        else:
            self.head.prev = Node(value, None, self.head)
            self.head = self.head.prev
            self.size += 1

    def pop(self) -> int:
        if self.size == 0:
            return -1
        
        elif self.size ==1:
            val = self.head.val
            self.head = None
            self.tail = None
            self.size -= 1
            return val

        elif self.size > 1:
            val = self.tail.val
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1
            return val

    def popleft(self) -> int:
        if self.size == 0:
            return -1
        elif self.size ==1:
            val= self.head.val
            self.head = None
            self.tail = None
            self.size -= 1
            return val

        elif self.size > 1:
            val = self.head.val
            self.head = self.head.next
            self.size -= 1
            return val
            
# def main():
#         deque = Deque()
#         deque.append(10)
#         deque.appendleft(20)
#         deque.appendleft(30)
#         deque.append(5)
        
# if __name__ == "__main__":
#         main()