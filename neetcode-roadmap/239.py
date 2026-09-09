from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue_idx = []
        for i in range(k):
            while queue_idx and nums[queue_idx[-1]] < nums[i]:
                queue_idx.pop(-1)

            queue_idx.append(i)

        ret_list = [nums[queue_idx[0]]]
        for i in range(k, len(nums)):
            start = i - k
            if queue_idx[0] == start:
                queue_idx.pop(0)

            while queue_idx and nums[queue_idx[-1]] < nums[i]:
                queue_idx.pop(-1)

            queue_idx.append(i)
            ret_list.append(nums[queue_idx[0]])

        return ret_list


if __name__ == "__main__":
    sol = Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    # nums = [3,1,1,3]
    # k = 3
    print(sol.maxSlidingWindow(nums=nums, k=k))
