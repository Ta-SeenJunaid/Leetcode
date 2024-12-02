class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        len_word = len(searchWord)
        sentence = sentence.split()
        for i in range(len(sentence)):
            if len(sentence[i]) >= len_word and searchWord in sentence[i][:len_word]:
                return i+1
        return -1
