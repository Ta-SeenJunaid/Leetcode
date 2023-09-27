# https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-automl-endpoint?view=azureml-api-2&tabs=python#deploy-manually-from-the-studio-or-command-line

class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        total_length = 0
        for char in s:
            if char.isnumeric():
                total_length *= int(char)
            else:
                total_length += 1
        
        for char in reversed(s):
            k %= total_length
            if k == 0 and char.isalpha():
                return char
            elif char.isnumeric():
                total_length //= int(char)
            else:
                total_length -= 1
