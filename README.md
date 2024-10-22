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
### Total : ![1/150](https://progress-bar.xyz/1/?scale=150&suffix=/150)
- [ ] [Arrays and Hashing](#arrays-and-hashing) ![1/9](https://progress-bar.xyz/1/?scale=9&suffix=/9)
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

## Arrays and Hashing

1. [Duplicate Integer](#duplicate-integer)

---

### [Duplicate Integer](https://neetcode.io/problems/duplicate-integer)
#### Problem Description
This problem involves checking if there is a duplicate integer in the given list of integers. At face value, this means we need to iterate through the list until we find a duplicate. At first, I considered creating a bucket for each number, then adding the integers into each bucket until one of them had more than one item, indicating a duplicate. After considering this, I decided it was likely unnecessary and overcomplicated for this problem. The solution I ended up going with was to sort the array using `sort()`, then I could simply check for adjacent integers to see if there are duplicates. While this may not be the most time-efficient solution (since it requires sorting the whole list upfront), it meant that I wouldn't need to keep track of any intermediate data while parsing the list, such as what integers I've already seen.

[My Solution (C++)](Arrays_and_Hashing/Duplicate_Integer/solution.cpp)

#### Solution analysis
Time Complexity -> `O(n*log(n))`

This is not the fastest time complexity for this problem, but definitely not the worst case. The worst case is a brute force method, which iterates through the list once for each element of the list, checking if a duplicate element exist. This worst case solition has a time complexity of `O(n^2)`. The best time-efficient solution for this problem involves the use of an (`unordered_set`). If the array is iterated through once and each element is added to a set, the length of the set can be compared to the array. If the set is smaller (meaning duplicates were removed), then we know that a duplicate must exist in the array.

#### Key Takeaways
In the future, I should definitely take advantage of sets/hashes in order to create more time-efficient programs.