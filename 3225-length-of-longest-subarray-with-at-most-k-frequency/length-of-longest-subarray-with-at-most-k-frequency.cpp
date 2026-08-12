#include <vector>
#include <unordered_map>

class Solution {
public:
    int maxSubarrayLength(std::vector<int>& nums, int k) {
        std::unordered_map<int, int> freq;
        int left = 0, right = 0, max_length = 0;
        while (right < nums.size()) {
            freq[nums[right]]++;
            while (freq[nums[right]] > k) {
                freq[nums[left]]--;
                left++;
            }
            max_length = std::max(max_length, right - left + 1);
            right++;
        }
        return max_length;
    }
};