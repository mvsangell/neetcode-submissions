class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        lst = []
        for i in range(0,len(s)):
            if s[i].isalnum():
                lst.append(s[i])
        i = 0
        j = len(lst) - 1
        while (i <= j):
            if lst[i] != lst[j]:
                return False
            else:
                i+=1
                j-=1
        return True