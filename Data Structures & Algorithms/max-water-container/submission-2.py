class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Méthode des deux pointers
        gauche = 0
        droite = len(heights) - 1
        max_eau = 0
        while gauche < droite:
            hauteur_actuelle = (droite - gauche) * min(heights[gauche], heights[droite])
            max_eau = max(max_eau, hauteur_actuelle)
            if heights[gauche] < heights[droite]:
                gauche += 1
            else:
                droite -= 1 
        return max_eau
        