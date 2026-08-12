# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def __init__(self):
        self.root = None


    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        self.root = root
        
        if not self.root:
            self.root = TreeNode(val)
            return self.root
        else:
            curr = self.root

            while curr:
                if curr.left and val < curr.val:
                    curr = curr.left
                elif curr.right and val > curr.val:
                    curr = curr.right
                elif curr.val == val:
                    break
                else:
                    break
            
            if val < curr.val:
                curr.left = TreeNode(val)
                return root
            elif val > curr.val:
                curr.right = TreeNode(val)
                return root
                



        