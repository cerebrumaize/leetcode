#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, nums, k):
        '''Solution function description'''
        return sorted(nums, reverse=True)[k-1]
    def bubble_sort(self, nums, k):
        '''bubble sort'''
        for i in range(k):
            for j in range(len(nums)-i-1):
                if nums[j] > nums[j+1]: nums[j], nums[j+1] = nums[j], nums[j+1]
        return nums[k-1]
    def selection_sort(self, nums, k):
        for i in range(k):
            max_ind = i
            for j in range(1, len(nums)-i):
                if nums[j] > nums[max_ind]: max_ind = j
            nums[i], nums[max_ind] = nums[max_ind], nums[i]
        return nums[k-1]
    def quick_sort(self, nums, k):
        def helper(arr):
            print(arr)
            if len(arr) <= 1: return arr
            lwall, rwall = 0, 0
            pivot = arr[-1]
            for i, e in enumerate(arr):
                if e < pivot:
                    arr[i], arr[lwall] = arr[lwall], arr[i]
                    lwall += 1
                    arr[i], arr[rwall] = arr[rwall], arr[i]
                    rwall += 1
                elif e == pivot:
                    arr[i], arr[rwall] = arr[rwall], arr[i]
                    rwall += 1
                elif e > pivot: continue
            return helper(arr[:lwall]) + arr[lwall:rwall] + helper(arr[rwall:])
        return helper(nums)[len(nums)-k]


    #def tim_sort(self, nums, k):
    def min_heap_sort(self, nums, k):
        heap = []
        import heapq
        for i in nums: heapq.heappush(heap, -i)
        for _ in range(k-1): heapq.heappop(heap)
        return -    heapq.heappop(heap)


def main():
    '''main function'''
    _solution = Solution()
    inp = [([7,6,5,4,3,2,1], 2)]
    for i in inp:
        print(_solution.func(i[0], i[1]))
        print(_solution.bubble_sort(i[0], i[1]))
        print(_solution.selection_sort(i[0], i[1]))
        print(_solution.min_heap_sort(i[0], i[1]))
        print(_solution.quick_sort(i[0], i[1]))

if __name__ == "__main__":
    main()
