# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
            self.ans=[]
    def postorderTraversal(self, root):
        if root is None:
            return self.ans
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        self.ans.append(root.val)
        return self.ans
        
        

        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        