class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalnum())
        s = s.lower()
        isPalindrome = True
        for  i in range(math.ceil(len(s)/2)):
            if(s[i] != s[len(s) - 1 - i]):
                isPalindrome = False
                break
        
        return isPalindrome
        