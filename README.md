# Neetcode.io Solutions: LeetCode Roadmap Problems

Welcome to my personal repository for [Neetcode.io's **LeetCode Roadmap**](https://neetcode.io/roadmap) solutions! This repository contains my implementations of various LeetCode problems in **C++** and **Python**, following the structure provided by Neetcode.io.

## Table of Contents

1. [Introduction](#introduction)
2. [Structure](#structure)
4. [Solutions Overview](#solutions-overview)

## Introduction

This repository contains solutions to LeetCode problems organized by [Neetcode.io's curated roadmap](https://neetcode.io/roadmap). Each problem is solved in either **C++** or **Python**, providing clean, efficient code implementations.

The goal of this repository is to not only serve as a personal resource for interview preparation but also to help others learn by sharing well-commented and optimized solutions. In this README file, I will be adding my own interpretations of each problem and the thought process behind each solution. While I know this project will certainly help me prepare for more technical programming challenges, I hope that it also serves as a helpful resource for those who want to learn more about the problem-solving process for these challenges.

## Structure

Each section of the roadmap will have it's own directory, which will be in the root of this project. For each section, there will be a folder for each problem I've started/completed, containing my solution.

## Solutions Overview
These are the sections of the roadmap, in the order I will most likely be completing them. If a section has been started by me, it will have a progress bar next to it, and it will link to a section outlining my solutions to the problems in that section that I've completed so far. If it has been completed, it will have a checkmark next to it.
### Total : ![3/150](https://progress-bar.xyz/3/?scale=150&suffix=/150)
- [ ] [Arrays and Hashing](#arrays-and-hashing) ![3/9](https://progress-bar.xyz/3/?scale=9&suffix=/9)
- [ ] Two Pointers
- [ ] Stack
- [ ] Binary Search
- [ ] Sliding Window
- [ ] Linked List
- [ ] Trees
- [ ] Tries
- [ ] Backtracking
- [ ] Heap / Priority Queue
- [ ] Graphs
- [ ] 1-D DP
- [ ] Intervals
- [ ] Greedy
- [ ] Advanced Graphs
- [ ] 2-D DP
- [ ] Bit Manipulation
- [ ] Math & Geometry
---
## Arrays and Hashing

1. [Duplicate Integer](#duplicate-integer)
2. [Is Anagram](#is-anagram)
3. [Two Integer Sum](#two-integer-sum)

---

### [Duplicate Integer](https://neetcode.io/problems/duplicate-integer)
#### My Approach:
This problem involves checking if there is a duplicate integer in the given list of integers. At face value, this means we need to iterate through the list until we find a duplicate. At first, I considered creating a bucket for each number, then adding the integers into each bucket until one of them had more than one item, indicating a duplicate. After considering this, I decided it was likely unnecessary and overcomplicated for this problem. The solution I ended up going with was to sort the array using `sort()`, then I could simply check for adjacent integers to see if there are duplicates. While this may not be the most time-efficient solution (since it requires sorting the whole list upfront), it meant that I wouldn't need to keep track of any intermediate data while parsing the list, such as what integers I've already seen.

[My Solution (C++)](Arrays_and_Hashing/Duplicate_Integer/solution.cpp)

#### Solution Analysis:
Time Complexity -> `O(n*log(n))`

This is not the fastest time complexity for this problem, but definitely not the worst case. The worst case is a brute force method, which iterates through the list once for each element of the list, checking if a duplicate element exist. This worst case solition has a time complexity of `O(n^2)`. The best time-efficient solution for this problem involves the use of an (`unordered_set`). If the array is iterated through once and each element is added to a set, the length of the set can be compared to the array. If the set is smaller (meaning duplicates were removed), then we know that a duplicate must exist in the array.

#### Key Takeaways:
In the future, I should definitely take advantage of sets/hashes in order to create more time-efficient programs.

---

### [Is Anagram](https://neetcode.io/problems/is-anagram)
#### My Approach:
This problem requires the user to take two strings, s and t, and return true if s is an anagram of t. That is to say, if the letters of s can be rearranged to create t, then s is an anagram of t, and vice versa. Initially, I wanted to think of a way I can use a hash set or hash map of some kind to make this optimally time-efficient. In the end, I came up with the idea to make an `unordered_map` of character "balances", where a positive balance indicates it occurs more in string s, and a negative balance means it occurs more in string t. Using this concept, I was able to make a solution which iterates through the length of the string once, calculating the balances of each char, then a second time, ensuring that all chars are balanced. If an imbalance is detected, it means that s and t are not anagrams of eachother.

[My Solution (C++)](Arrays_and_Hashing/Is_Anagram/solution.cpp)

#### Solution Analysis:
Time Complexity -> `O(n)`

This is the best time complexity possible for this problem, but there are still some ways it can be improved. Something to note from neetcode's optimal solution is that the range of char values in each string is limited to the 26 letters of the alphabet, so a fixed size map can be created and iterated over in the end rather than re-iterating over the string at the end. This is ideal especially if the string is very large. Additionally, since chars are just byte values, we can use their offset from 'a' to index a list or vector of count values, meaning a linear time solution is possible without a hashtable. 

#### Key Takeaways:
The most notable takeaway here is while hashtables can be reliable for making time efficient solutions to problems, they may not always be necessary. Additionally, taking advantage of the provided constraints (in this case, the knowledge that each string will only consist of lowercase alphabetic character) can allow for further optimizations.

---

### [Two Integer Sum](https://neetcode.io/problems/two-integer-sum)
#### My Approach:
Two Int Sum is an infamous problem that requires you to find the indices of two integers in a list that sum up to a given target value. Initially, I attempted to solve this problem using the well-known two-pointer approach. The basic idea is that you start with a pointer to each end of the list, and shift them from the ends until the target sum value is reached. While this approach worked for the basic tests, it only ended up passing 7 out of 23 of the overall tests. The main reason for this is that my approach was assuming that the list is sorted, and while it was sorted in the basic tests, it was not sorted in all the overall tests.

Of course, one way this problem could be solved without fail is the brute force method, where for each int element, you check all other ints in the list to see if any of them add up to the target. This is `O(n^2)`, so not very ideal for a time-efficient solution. My next idea was to explore a hashmap-based approach.

To utilize a hashmap for this problem, I'll keep a dictionary of past values and their corresponding index, so the key is the num, and the value is its index. By traversing the array once, I can keep track of which nums I've seen, and every time I look at a new number, I can find the difference between the target and itself, and then perform a constant-time lookup into the dictionary. If a match is found, return the value of the entry (the index), and the index of the number currently being looked at. Since the dictionary is built on previously seen values, it will always mean the earliest index is returned as the first part of the return value.

[My Solution (Python)](Arrays_and_Hashing/Two_Integer_Sum/solution.py)
[My Solution (C++)](Arrays_and_Hashing/Two_Integer_Sum/solution.cpp)

#### Solution Analysis:
Time Complexity -> `O(n)`

This is the optimal performance of this problem, especially since two-pointers is not a viable solution due to the array not always being sorted. Neetcode's solution is essentially the same as what I have, and there doesn't seem to be any other offered solution methods, although brute forcing the problem is still possible, despite being much slower than the hash solution. The reason the hash solution is linear time is because the list is only iterated through once, and the lookups onto the past indices are constant (since it's a hashmap). 

#### Key Takeaways:
Although two pointers didn't work for the entire testbed, there was still a lot of value in conceptualizing and implementing it. Hashmaps are very flexible and effective for a large range of problems, but these other methods still have their place for more intuitive solutions.

---