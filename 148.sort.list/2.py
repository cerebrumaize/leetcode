#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    '''Solution description'''
    def sortList(self, head):
        '''Solution function description'''
        '''but this is not in place, mem is n, not constant'''
        p = head
        values = []
        while p != None:
            values.append(p.val)
            p = p.next
        values.sort()
        i = 0
        p = head
        while p != None:
            p.val = values[i]
            i += 1
            p = p.next
        return head


def stringToIntegerList(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return []
    return [int(number) for number in input.split(",")]

def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    result = ""
    if not node:
        return result

    while node:
        result += str(node.val) + ", "
        node = node.next
    return result[:-2]

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = (n for n in ['[2,1]', '[2,1,3]'])#readlines()
    while True:
        try:
            line = next(lines)
            head = stringToListNode(line)

            ret = Solution().sortList(head)

            out = listNodeToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
