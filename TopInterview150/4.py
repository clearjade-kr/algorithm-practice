from typing import List


# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         m, n = len(nums1), len(nums2)

#         # arr1, arr2 - pointer values to swap after changing length
#         # p1 - pointer for nums1 to evaluate
#         # p2 - pointer for nums2 to evaluate
#         def find_kth(arr1, p1, arr2, p2, k):
#             len1, len2 = len(arr1) - p1, len(arr2) - p2

#             if len1 == 0:
#                 return arr2[p2 + k]
#             if len2 == 0:
#                 return arr1[p1 + k]
#             if k == 0:
#                 return min(arr1[p1], arr2[p2])

#             # Check length of each and swap for O(log(min(M, N)))
#             if len1 > len2:
#                 return find_kth(arr2, p2, arr1, p1, k)

#             i = min(len1 - 1, k // 2)
#             j = k - i - 1

#             if arr1[p1 + i] > arr2[p2 + j]:
#                 return find_kth(arr1, p1, arr2, p2 + j + 1, k - (j + 1))
#             else:
#                 return find_kth(arr1, p1 + i + 1, arr2, p2, k - (i + 1))

#         total_len = len(nums1) + len(nums2)
#         if total_len % 2 == 1:
#             return float(find_kth(nums1, 0, nums2, 0, total_len // 2))
#         else:
#             mid1 = find_kth(nums1, 0, nums2, 0, total_len // 2 - 1)
#             mid2 = find_kth(nums1, 0, nums2, 0, total_len // 2)
#             return (mid1 + mid2) / 2.0
                


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Guarantee nums1 is the shorter array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        half_len = (m + n + 1) // 2

        lo, hi = 0, m

        while lo <= hi:
            i = (lo + hi) // 2
            j = half_len - i

            # Handle edge cases where partition cut is at index 0 or length boundary
            Aleft = nums1[i - 1] if i > 0 else float('-inf')
            Aright = nums1[i] if i < m else float('inf')
            Bleft = nums2[j - 1] if j > 0 else float('-inf')
            Bright = nums2[j] if j < n else float('inf')

            # Valid partition found
            if Aleft <= Bright and Bleft <= Aright:
                if (m + n) % 2 == 1:
                    return float(max(Aleft, Bleft))
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0

            # Partition cut in nums1 is too far right
            elif Aleft > Bright:
                hi = i - 1
            # Partition cut in nums1 is too far left
            else:
                lo = i + 1


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMedianSortedArrays([1, 3], [2]))
    print(sol.findMedianSortedArrays([1, 2], [3, 4]))