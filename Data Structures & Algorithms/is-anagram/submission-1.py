class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            l,ll = [],[]
            for n in range(len(s)):
                l.append(int(ord(s[n])))
                ll.append(int(ord(t[n])))
            l = sorted(l)
            ll = sorted(ll)
            if (l == ll):
                return True
            else:
                return False
        else:
            return False