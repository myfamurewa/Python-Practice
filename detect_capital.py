class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == word.upper() or word[0] == word[0].upper() and word == word[0].upper() + word[1:].lower() or word.lower() == word:
            return True
        else:
            return False
        