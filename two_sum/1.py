
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

    def list_to_dict(self, nums, target):
        '''
        convert list to dictionary, and then use key exist to calculate
        dictionary is saved as hash table, which accelerates value retrieving
        '''
        dict_nums = {}
        for i in xrange(0, len(nums)):
            if nums[i] in dict_nums:
                dict_nums[nums[i]] = [dict_nums[nums[i]], i]
            else:
                dict_nums[nums[i]] = i

        for i in xrange(0, len(nums)):
            target_1 = nums[i]
            target_2 = target - target_1
            if target_2 in dict_nums:
                if isinstance(dict_nums[target_1], list):
                    return dict_nums[target_1]
                if dict_nums[target_1] != dict_nums[target_2]:
                    return [dict_nums[target_1], dict_nums[target_2]]

def main():
    '''main function'''
    _solution = Solution()
    res = _solution.list_to_dict([0, 4, 3, 0], 0)
    print res

if __name__ == "__main__":
    main()
