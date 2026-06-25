class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        gauche, droite = 0, 1
        profit_max = 0
        while droite < len(prices):
            if prices[gauche] < prices[droite]:
               profit_actuelle = prices[droite] - prices[gauche]
               profit_max = max(profit_max, profit_actuelle)
            else:
                gauche = droite 
            droite += 1
    
        return profit_max
        