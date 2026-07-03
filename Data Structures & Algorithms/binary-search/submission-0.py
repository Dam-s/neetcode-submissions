class Solution:
    def search(self, nums: List[int], target: int) -> int:
        gauche = 0
        droite = len(nums) - 1
        pos = -1 

        while gauche <= droite:
            milieu = (gauche + droite) // 2
            
            if nums[milieu] == target:
                pos = milieu
                break
            elif nums[milieu] < target:
                gauche = milieu + 1
            else:
                droite = milieu - 1
        
        return pos
            