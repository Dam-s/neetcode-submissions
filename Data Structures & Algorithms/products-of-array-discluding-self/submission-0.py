class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        resultats = []

        for index in range(len(nums)):
            # Créer une sous-liste sans l'élément à l'index courant
            liste_temp = nums[:index] + nums[index+1:]
            mon_produit = math.prod(liste_temp)
            resultats.append(mon_produit)
        return resultats