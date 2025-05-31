class Solution:
    def countSubarrays(self, arr, k):
        count = 0           # final answer store karne ke liye
        curr_sum = 0        # ab tak ka sum
        sum_freq = {0: 1}   # prefix sum frequency map, starting with 0 sum once

        for num in arr:
            curr_sum += num

            # check karo agar curr_sum - k pehle aaya hai ya nahi
            if curr_sum - k in sum_freq:
                count += sum_freq[curr_sum - k]

            # ab is curr_sum ki frequency update karo
            if curr_sum in sum_freq:
                sum_freq[curr_sum] += 1
            else:
                sum_freq[curr_sum] = 1

        return count
