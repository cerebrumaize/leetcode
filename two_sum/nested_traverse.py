
#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401

class Solution(object):
    '''two sum'''
    def nested_traverse(self, nums, target):
        '''traverse list for i and j'''
        for i in xrange(0, len(nums)):
            another = target-nums[i]
            for j in xrange(0, len(nums)):
                if i != j and nums[j] == another:
                    return [i, j]

def main():
    '''main function'''
    _solution = Solution()
    res = _solution.nested_traverse([0, 4, 3, 0], 0)
    print res

if __name__ == "__main__":
    main()
