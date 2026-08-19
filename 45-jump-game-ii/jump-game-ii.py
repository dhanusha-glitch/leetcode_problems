class Solution:
    def jump(self, nums: List[int]) -> int:
        count = reached_to = can_reach_to = 0
        for i in range(len(nums)):
            if i > reached_to: count += 1;reached_to = can_reach_to
            can_reach_to = max(can_reach_to, i + nums[i])
        return count