class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        touches = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        result = []

        for i in range(len(digits)):
            if i == 0:
                result = list(touches[digits[i]])
            else:
                temp = []
                for j in result:
                    for k in touches[digits[i]]:
                        temp.append(j + k)
                result = temp
        return result


