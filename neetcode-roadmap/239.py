from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        queue_idx = deque()
        ret_list = []

        for i in range(len(nums)):
            # Remove first element of queue if the index is out of window
            if queue_idx and queue_idx[0] <= i - k:
                queue_idx.popleft()

            # Remove last elements that are smaller than current
            while queue_idx and nums[queue_idx[-1]] < nums[i]:
                queue_idx.pop()

            queue_idx.append(i)

            # Add first element if current index is after initial k - 1
            if i >= k - 1:
                ret_list.append(nums[queue_idx[0]])

        return ret_list


if __name__ == "__main__":
    sol = Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    # nums = [3,1,1,3]
    # k = 3
    print(sol.maxSlidingWindow(nums=nums, k=k))
