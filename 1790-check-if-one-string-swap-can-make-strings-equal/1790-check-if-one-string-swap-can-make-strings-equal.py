class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        c = 0
        for c1, c2 in zip(s1,s2):
            if c1 != c2:
                c += 1
        return s1 == s2 or sorted(s1) == sorted(s2) and c == 2