class Solution:
    def isAnagram(self, s: str, t: str):
        if len(s) != len(t):    # checks length of individual string to confirm have similar length to be an anagram
            return False
        else:
            for i in s:
                if s.count(i) != t.count(i): # takes each character from the string and validates each character repeated same number of times in the both strings
                    return False
                    break
        return True

# Takes input from the user
  
s = input("Enter String1 : ")
t = input("Enter string2 : ")

# intializig object for the class Solution

Sol = Solution()
# Calling function using object

print(Sol.isAnagram(s,t))
        