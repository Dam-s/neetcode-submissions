class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        alls_counter = Counter(nums)
        alls_counter_dict = dict(sorted(alls_counter.items(), key=lambda item: item[1], reverse=True))

        reponse = []
        i = 0

        for nombre in alls_counter_dict.keys():
            if (i < k):
                reponse.append(nombre)
            i += 1
        return reponse