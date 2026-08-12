class Solution:
    def maxSubarrayLength(self, nums, k):
        freq = {}
        left = 0
        max_len = 0

        for right, x in enumerate(nums):
            freq[x] = freq.get(x, 0) + 1

            while freq[x] > k:
                y = nums[left]
                freq[y] -= 1
                left += 1

            length = right - left + 1
            if length > max_len:
                max_len = length

        return max_len