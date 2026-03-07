class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        l = (nums1 + nums2)
        l.sort()
        # print(l)

        if len(l) % 2 != 0:
            # print(l[int(len(l) / 2)])
            # print("--")
            return l[int(len(l) / 2)]
        else:
            # print(l[int(len(l) / 2)])
            # print(l[int(len(l) / 2) - 1])
            # print("--")
            return (l[int(len(l) / 2) - 1] + l[int(len(l) / 2)]) / 2

print(Solution().findMedianSortedArrays([1, 3], [2]))
print("----")
print(Solution().findMedianSortedArrays([1, 2], [3, 4]))
# Solution().findMedianSortedArrays([0, 0], [0, 0])