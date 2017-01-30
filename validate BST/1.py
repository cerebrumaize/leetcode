
#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    '''Solution description'''
    def leftMost(self, root):
        '''find the left most child in root'''
        if root.left == None:
            return root
        while not (root.left == None):
            return self.leftMost(root.left)

    def rightMost(self, root):
        '''find the right most child in root'''
        if root.right == None:
            return root
        while not (root.right == None):
            return self.rightMost(root.right)
    def isValidBST(self, root):
        '''Solution function description'''
        if (root == None) | ((root.left == None) & (root.right == None)):
            return True
        if (root.left.left == None) & (root.left.right == None) & (root.right == None) & root.left.val < root.val:
            return True
        else:
            return False
        if (root.right.left == None) & (root.right.right == None) & (root.left == None) & (root.val < root.right.val):
            return True
        else:
            return False
        if (root.left.left == None) & (root.left.right == None) & (root.right.left == None) & (root.right.right == None):
            if not (root.left.val < root.val & root.val < root.right.val):
                return False
        else:
            self.isValidBST(root.left)
            self.isValidBST(root.right)
        return True

def main():
    '''main function'''
    _solution = Solution()
    res = _solution.isValidBST(a, b)
    print res

if __name__ == "__main__":
    main()
