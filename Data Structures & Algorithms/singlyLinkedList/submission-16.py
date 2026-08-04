class Node:
    def __init__(self, val: int, next_node = None):
        self.node_val = val
        self.next = next_node
        


class LinkedList:
    
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        
        if index >= self.size:
            return -1
        
        else:    
            counter = 0    
            curr = self.head
            while curr:

                if counter == index:
                    return curr.node_val
                else:
                    curr = curr.next
                    counter +=1
        return -1
        

    def insertHead(self, val: int) -> None:
        
        if self.size == 0:
            self.head = Node(val)
            self.tail = self.head
            self.size +=1
        
        else:
            new_node = Node(val, self.head)
            self.head = new_node
            self.size +=1


    def insertTail(self, val: int) -> None:
        if self.size == 0:
            self.head = Node(val)
            self.tail = self.head
            self.size +=1
        
        else:
            temp_node = Node(val)
            self.tail.next = temp_node
            self.tail = temp_node
            self.size +=1
            
        

    def remove(self, index: int) -> bool:
        if index > self.size -1:
            return False
        
        elif  self.size ==1:
            self.head = None
            self.tail= None
            self.size = 0
            return True
        
        elif index ==0:
            temp_node = self.head.next
            self.head = temp_node
            self.size -=1
            return True
        
        
        else:

            counter = 0
            curr = self.head
            prev = None
           
            while curr.next:
                
                if counter == index:
                    prev.next = curr.next
                    self.size -=1
                    return True
         
                else:
                    prev = curr
                    curr = curr.next
                    counter += 1

            self.tail = curr
            self.size -=1
            return True
    
        
        return False
                    

    def getValues(self) -> List[int]:
        
        
        arr = []

        curr = self.head
        

        while curr:
            arr.append(curr.node_val)
            curr = curr.next
        
        return arr



