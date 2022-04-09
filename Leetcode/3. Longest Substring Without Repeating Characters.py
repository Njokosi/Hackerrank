"""
3. Longest Substring Without Repeating Characters
Medium

22759

1018

Add to List

Share
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution(object):
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        max_length = 0
        start = 0
        
        for i in range(len(s)):
            # Check if we've seen the element
            if s[i] in seen:
                
                # If seen move the pointer to position after the last occurence
                start = max(start, seen[s[i]] + 1) 
                
            seen[s[i]] = i
            max_length = max(max_length, i - start + 1)
        return max_length
            
            

s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))

# ss = 'abaaa'
# print(ss[0])
s = {"a":1}
# print(s[ss[0]] + 1)