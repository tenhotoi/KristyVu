def isSubsequence1(x, y):
    it = iter(y)
    return all(any(c == ch for c in it) for ch in x)

print(isSubsequence1("abc", "def"))
print(isSubsequence1("abc", "adebcf"))

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ls, lt = len(s), len(t)
        if ls > lt:
            return False
        i = j = 0
        while i < ls and j < lt:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == ls

testsubseq = Solution()
print(testsubseq.isSubsequence("abc", "def"))
print(testsubseq.isSubsequence("abc", "adebcf"))
