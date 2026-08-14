class MinHeap:
    def __init__(self):
        self.heap = [0]

    def push(self, val: int) -> None:

        self.heap.append(val)

        # set index to the end and percolate up
        i = len(self.heap) - 1

        while i != 1 and self.heap[i] < self.heap[i // 2]:
            temp_val = self.heap[i // 2]

            self.heap[i // 2] = self.heap[i]
            self.heap[i] = temp_val
            # important need to keep dividing by two to check its parent is less
            i = i // 2

    def pop(self) -> int:
        # main goal is to percolate down take last effective child and put in the root repeat

        if len(self.heap) == 1:
            return -1
        elif len(self.heap) == 2:
            return self.heap.pop()
        else:
            # [0, 14, 19, 16, 21, 26, 19, 68, 29, 30]
            result = self.heap[1]
            self.heap[1] = self.heap.pop()
            # just swapped 14 and 30 and popped
            # [0, 30, 19, 16, 21, 26, 19, 68, 29, 14] -> [0, 30, 19, 16, 21, 26, 19, 68, 29]
            # Now need to keep comparing 30 to its right then left tree swap and repeat
            i = 1
            while 2 * i < len(self.heap):
                right_child = (2 * i) + 1
                left_child = 2 * i
                # check inboundedness of roots and then compare
                if (
                    right_child < len(self.heap)
                    and self.heap[right_child] < self.heap[left_child]
                    and self.heap[right_child] < self.heap[i]
                ):
                    temp = self.heap[i]
                    self.heap[i] = self.heap[right_child]
                    self.heap[right_child] = temp
                    i = right_child

                # if left is smaller then right can collapse the cases
                # only the left child matters
                elif self.heap[left_child] < self.heap[i]:
                    temp = self.heap[i]
                    self.heap[i] = self.heap[left_child]
                    self.heap[left_child] = temp
                    i = left_child
                else:
                    break

            return result

    def top(self) -> int:
        if len(self.heap) > 1:
            return self.heap[1]
        else:
            return -1

    def heapify(self, nums: List[int]) -> None:
        self.heap = [0] + nums
        curr = (len(self.heap) - 1) // 2

        while curr > 0:
            i = curr
            while 2 * i < len(self.heap):
                left_child = 2 * i
                right_child = 2 * i + 1
                if (
                    right_child < len(self.heap)
                    and self.heap[right_child] < self.heap[left_child]
                    and self.heap[right_child] < self.heap[i]
                ):
                    temp = self.heap[i]
                    self.heap[i] = self.heap[right_child]
                    self.heap[right_child] = temp
                    i = right_child
                elif self.heap[left_child] < self.heap[i]:
                    temp = self.heap[i]
                    self.heap[i] = self.heap[left_child]
                    self.heap[left_child] = temp
                    i = left_child
                else:
                    break
            curr -= 1
