#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or head.next is None: return head

        pre, mid, post = None, head, head
        while post and post.next:
            pre, mid, post = mid, mid.next, post.next.next
        pre.next = None
        return self.merge(*map(self.sortList, (head, mid)))

    def merge(self, h1, h2):
        dummy = tail = ListNode(None)
        while h1 and h2:
            if h1.val < h2.val:
                tail.next, tail, h1 = h1, h1, h1.next
            else:
                tail.next, tail, h2 = h2, h2, h2.next

        tail.next = h1 or h2
        return dummy.next


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
