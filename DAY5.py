class Solution:
    def isPalindrome(self, s: str) -> bool:
        r=''
        for i in s.lower():
            if i.isalnum():
                r+=i
        if(r[::-1] == r):
            print('true')
        else:
            print('false')

Sol = Solution()
Sol.isPalindrome(input())