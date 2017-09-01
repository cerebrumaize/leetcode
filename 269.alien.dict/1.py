#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, words):
        '''Solution function description'''
        pairs = []
        for word in zip(words, words[1:]):
            for a, b in zip(*word):
                if a != b:
                    pairs.append(a+b)
                    break
        chars = set(''.join(words))
        order = []
        while pairs:
            free = chars - set(list(zip(*pairs))[1])
            if not free:
                return ''
            order += free
            pairs = list(filter(free.isdisjoint, pairs))
            chars -= free
        return ''.join(order + list(chars))

def main():
    '''main function'''
    _solution = Solution()
    inp = [["w", 'p', 'tzo', 'qc']]
    for i in inp:
        print(_solution.func(i))

if __name__ == "__main__":
    main()

'''
这里值得注意的一点是, visited是用来保存已经访问过的节点, 一般情况下节点的标记不会是想list
的索引一样是自然数(得用dict), 这里是自然数所以用了简单的列表
'''