class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        max_vowel_count = 0
        current_count = 0
        
        for i in range(k):
            if s[i] in vowels:
                current_count += 1
        
        max_vowel_count = current_count
        start, end = 0, k - 1
        
        for i in range(k, len(s)):
            if s[start] in vowels:
                current_count -= 1
            start += 1
            end += 1
            if s[end] in vowels:
                current_count += 1
            
            max_vowel_count = max(max_vowel_count, current_count)
        
        return max_vowel_count
