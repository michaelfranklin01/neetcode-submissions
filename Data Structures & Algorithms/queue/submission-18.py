class Node:    
    def __init__(self, val: int, prev_node = None, next_node = None):
        self.val = val
        self.prev = prev_node
        self.next = next_node


class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    def isEmpty(self) -> bool:
        return self.size == 0
        

    def append(self, value: int) -> None:
        if self.size ==0:
            self.tail = Node(value)
            self.head = self.tail
            self.size += 1
        else:
            new_node = Node(value, self.tail)
            self.tail.next = new_node
            self.tail = new_node
            self.size +=1
        

    def appendleft(self, value: int) -> None:
        if self.size ==0:
            self.head = Node(value)
            self.tail = self.head
            self.size +=1
        else:
            new_node = Node(value, None, self.head)
            # new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.size +=1
    

    def pop(self) -> int:
        if self.size ==0:
            return -1
        elif self.size ==1:
            val = self.tail.val
            self.head = None
            self.tail = None
            self.size -=1
            return val
        else:
            val = self.tail.val
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -=1
            return val


        

    def popleft(self) -> int:
        if self.size ==0:
            return -1
        elif self.size ==1:
            val = self.head.val
            self.head = None
            self.tail = None
            self.size -=1
            return val
        else:
            val = self.head.val
            self.head = self.head.next
            self.head.prev = None
            self.size -=1
            return val
        
