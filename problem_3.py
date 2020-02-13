class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_set = set()
        longest = 0
        start, end = 0, 0
        l = len(s)
        while start < l and end < l:
            if s[end] not in seen_set:
                seen_set.add(s[end])
                end += 1
                longest = max(longest, end - start)
            else:
                seen_set.remove(s[start])
                start += 1
        return longest
