"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""


class Solution(object):

    def two_sum(self, nums, target):
        
        nums_index = [(nums[i], i) for i in range(len(nums))]
        nums_index.sort()
        
        i, j = 0, len(nums_index) - 1
        while i < len(nums_index):
            current_sum = nums_index[i][0] + nums_index[j][0]
            
            if current_sum == target:
                return nums_index[i][1], nums_index[j][1]
            
            elif current_sum < target:
                i += 1
                
            else:
                j -= 1
                
            

nums = list(map(int, input("Enter list separated by space: ").rstrip().split()))
target = int(input("Enter your target: "))

s = Solution()
print(s.two_sum(nums, target))