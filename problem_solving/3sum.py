class Solution:
    # not my soln but its very cool
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        neg, pos, zeros = [], [], 0
        for num in nums:
            if num > 0:
                pos.append(num)
            elif num < 0:
                neg.append(num)
            else:
                zeros += 1
        neg_set, pos_set = set(neg), set(pos)  # for O(1) lookup
        
        # if there's zero in list, add cases where -x is in neg and x is in pos
        if zeros > 0:
            for num in pos_set:
                if -num in neg_set:
                    triplets.add((-num, 0, num))
                    
        # if at least 3 zeros in list, add 0, 0, 0
        if zeros >= 3:
            triplets.add((0, 0, 0))
            
        # for all pairs of negative numbers, check if their complement is in positive set
        for i in range(len(neg)):
            for j in range(i + 1, len(neg)):
                target = -1 * (neg[i] + neg[j])
                if target in pos_set:
                    triplets.add(tuple(sorted([neg[i], neg[j], target])))
        
        # do the same for positive numbers
        for i in range(len(pos)):
            for j in range(i + 1, len(pos)):
                target = -1 * (pos[i] + pos[j])
                if target in neg_set:
                    triplets.add(tuple(sorted([pos[i], pos[j], target])))
        return triplets
