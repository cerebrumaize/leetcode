
#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def func(self, strs):
        '''
        Solution function description
        '''
        d = {}
        for i in xrange(0, len(strs)):
            key = ''.join(sorted(strs[i]))
            if key in d:
                d[key].append(strs[i])
            else:
                d[key] = []
                d[key].append(strs[i])
        res = []
        for word_list in d:
            res.append(d[word_list])
        return res

def main():
    '''main function'''
    _solution = Solution()
    a = ["c", "c"]
    res = _solution.func(a)
    print res

if __name__ == "__main__":
    main()
