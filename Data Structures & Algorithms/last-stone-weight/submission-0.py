class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def get_two_max(arr):
            # Initialize variables with negative infinity
            max1 = max2 = float('-inf')
            
            for num in arr:
                if num > max1:
                    max2 = max1  # Demote old max to second max
                    max1 = num   # Update top max
                elif num > max2:
                    max2 = num   # Update second max if it falls between max1 and max2
            arr_max = [max1, max2]      
            return arr_max

        while len(stones) > 1:
                max1, max2 = get_two_max(stones)
                stones.remove(max1)
                stones.remove(max2)
                if max1 != max2:
                    stones.append(max1 - max2)
        return stones[0] if stones else 0