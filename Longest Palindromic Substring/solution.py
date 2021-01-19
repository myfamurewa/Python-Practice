class Solution:
    def longestPalindrome(self, s: str) -> str:
        ## expand from middle
        def expandfromMiddle(s, left, right):
            if s == None or left > right:
                return 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return right - left - 1
        if s == None or len(s) < 1:
            return ""
        start = 0
        end = 0
        for i in range(0, len(s)):
            len1 = expandfromMiddle(s, i, i)
            len2 = expandfromMiddle(s, i, i + 1)
            maxlen = max(len1, len2)
            if maxlen > end - start:
                start = i - ((maxlen - 1)// 2)
                end = i + (maxlen// 2)
        return s[start: end + 1]

        




class SolutionII:
    def longestPalindrome(self, s: str) -> str:
        p = ''
        for i in range(len(s)):
            p1 = self.get_palindrome(s, i, i+1)
            p2 = self.get_palindrome(s, i, i)
            p = max([p, p1, p2], key=lambda x: len(x))
        return p
    
    def get_palindrome(self, s: str, l: int, r: int) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]




## check if the substring is a palindrome
## if substr == substr[::-1]:

## if the substring is a palindrome we want to check if it's the longest palindrome
## len(palindrome)
## if it is we want to store it and return it at the end if it is still the longest palindrome

