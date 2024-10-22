class Solution {
public:
    bool isAnagram(string s, string t) {
        // Edge case - string lengths are different, anagram not possible
        if(s.length() != t.length()) return false;

        // Create an unordered hashtable with char keys and int values. Default value for
        // int is zero, which is already what we want the values to start at.
        unordered_map<char, int> map;

        // Both strings should be the same length
        for(int i = 0; i < s.length(); i++){
            map[s[i]]++; //Increase char "balance"
            map[t[i]]--; //Decrese char "balance"
        }

        /*
            The idea here is that since chars in t had negative weight, and chars in s
            has positive weight, then they should cancel eachother out if they have equal
            occurences. If all chars cancel eachother out then we can say the strings are
            anagrams of eachother.
        */
        for(char c : s)
            if (map[c] > 0) return false; // Imbalance detected, anagram not possible.

        // All chars are balanced, return true!
        return true;
    }
};