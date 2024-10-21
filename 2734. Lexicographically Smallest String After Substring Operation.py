class Solution:
    def smallestString(self, s: str) -> str:
        n = len(s)
        count = 0
        
        # Count the leading 'a's
        while count < n and s[count] == 'a':
            count += 1
        
        # If all characters are 'a', change the last one to 'z'
        if count == n:
            return s[:-1] + 'z'
        
        # Find the first non-'a' and start decrementing
        result = s[:count]  # Keep leading 'a's as is
        i = count
        
        # Decrement characters from the first non-'a' until an 'a' is found or the string ends
        while i < n and s[i] != 'a':
            result += chr(ord(s[i]) - 1)
            i += 1
        
        # Append the remainder of the string from where we stopped
        result += s[i:]
        
        return result
