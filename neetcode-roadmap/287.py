class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while slow2 != slow:
            slow2 = nums[slow2]
            slow = nums[slow]

        return slow


if __name__ == "__main__":
    sol = Solution()
    nums = [1,3,4,2,2]
    print(sol.findDuplicate(nums=nums))
