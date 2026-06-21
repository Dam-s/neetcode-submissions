class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        alls_counter = Counter(nums)
        alls_counter_dict = dict(sorted(alls_counter.items(), key=lambda item: item[1], reverse=True))

        reponse = []
        i = k

        for nombre in alls_counter_dict.keys():
            if (k <= i+1):
                reponse.append(nombre)
            k +=1
        return reponse