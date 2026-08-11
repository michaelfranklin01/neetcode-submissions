class Node:
    def __init__(self, val: int, next_node = None):
        
        self.val = val
        self.next = next_node


class LinkedList:
    
    def __init__(self):

        self.head = None
        self.tail = None
        self.size = 0


    def get(self, index: int) -> int:

        if index > self.size -1:
            return -1
        
        elif index == 0:
            return self.head.val
        
        else:

            count = 0
     
            prev = None
            curr = self.head
     
            while count != index:
                curr = curr.next
                count += 1

            return curr.val    
                
            
        

    def insertHead(self, val: int) -> None:
        if self.size == 0:
            self.head = Node(val)
            self.tail= self.head
            self.size +=1
        else:

            new_node = Node(val, self.head)
            self.head = new_node
            self.size +=1
        

    def insertTail(self, val: int) -> None:
        if self.size == 0:
            self.tail = Node(val)
            self.head = self.tail
            self.size +=1
        else:
            new_node = Node(val)
            self.tail.next = new_node
            self.tail = new_node
            self.size +=1

        

    def remove(self, index: int) -> bool:

        if index > self.size -1:
            return False
        elif self.size ==1:
            self.head = None
            self.tail = None
            self.size = 0
            return True
        elif index ==0:
            self.head = self.head.next
            self.size -=1
            return True
        
        else:
            prev = None
            curr = self.head
            count = 0

            while count != index:
                prev = curr
                curr = curr.next
                count +=1
            
            if index == self.size -1:
                self.tail = prev
                self.size -=1
                return True
            else:
                prev.next = curr.next
                self.size -=1
                return True
            
        

    def getValues(self) -> List[int]:

        arr = []
        curr = self.head
        for i in range(self.size):
            arr.append(curr.val)
            curr = curr.next
        return arr
            



        
