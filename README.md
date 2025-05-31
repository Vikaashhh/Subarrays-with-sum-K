# 🔰 Day 49 – GFG 160 Days DSA Challenge
### Problem: Count Subarrays with Sum K
### Language: Python
### Date: 31 May 2025

## ✅ Problem Statement:
Given an array of integers arr and an integer k, find the total number of subarrays whose sum equals k.

## 💡 Optimized Approach – Prefix Sum + Hash Map:
- Maintain a running prefix sum curr_sum.

- Store frequencies of all previous prefix sums in a dictionary (sum_freq).

- For each element:

- Check if (curr_sum - k) has occurred before. If yes, we can form a subarray with sum k.

- Update sum_freq with the current prefix sum.

### ⏱️ Time & Space Complexity:
Time: O(n)

Space: O(n)

