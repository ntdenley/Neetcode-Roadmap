class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        // Edge case - list is size 0 or 1, no duplicates possible
        if (nums.size() <= 1) return false;

        // Sort the input list
        sort(nums.begin(), nums.end());

        // For each number in the list, check if its right neighbor is a duplicate
        for(int i = 0; i < nums.size()-1; i++)
            // Duplicate found, return true!
            if (nums[i] == nums[i+1]) return true;

        // No duplicates found, return false.
        return false;
    }
};