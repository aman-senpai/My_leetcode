class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        total_count = 0
        freq = Counter(arr) # counts the frequency of all the elements in the array
        for index, count in enumerate(sorted(freq.values(), reverse=True)):
            total_count += count
            
            if total_count >= len(arr) // 2:
                return index + 1
        
        return 0