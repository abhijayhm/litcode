class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        shorter_len = len(word1)
        longer_word = word2
        if len(word2) < shorter_len:
            shorter_len = len(word2)
            longer_word = word1
        result = ""
        for i in range(shorter_len):
            result = result + word1[i]
            result = result + word2[i]
        if len(word1) != len(word2):
            result = result + longer_word[shorter_len:]
        return result