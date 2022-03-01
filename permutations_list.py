import itertools
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        a= list(itertools.permutations(nums))
        b = []
        for ele in a:
            b.append(list(ele))
        return b
