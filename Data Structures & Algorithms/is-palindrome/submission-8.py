class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char.lower() for char in s if char.isalnum())
        isPalindrome = True
        for  i in range(math.ceil(len(s)/2)):
            if(s[i] != s[len(s) - 1 - i]):
                isPalindrome = False
                break
        
        return isPalindrome
        