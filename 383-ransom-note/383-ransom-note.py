class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        w_map = defaultdict(int)
        
        for c in magazine:
            w_map[c] += 1
        for c in ransomNote:
            if w_map[c] == 0:
                return False
            w_map[c] -= 1
        return True