class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        // Create the hashmap of past_val->index
        unordered_map<int, int> past_indices; int i;
        
        // Iterate through the nums array
        for (i = 0; i < nums.size(); i++){
            // Find the diff between target and current value
            int diff = target - nums[i];
            
            // Search for the diff, if the end of the map was returned,
            // it means it's not in the list. Otherwise, it is
            if(past_indices.find(diff) != past_indices.end())
                // Diff found, return its index and the current index
                return {past_indices[diff], i};

            // Insert the current value and its index into the hashmap
            past_indices.insert({nums[i], i});
        }
        // This should never be reached since a twosum is guaranteed.
        return {-1, -1};
    }
};
