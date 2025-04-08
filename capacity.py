# shipWithinDays:
# - Binary search on capacity to ship all weights within given days.
# - Try mid capacity, count days needed, adjust bounds.

# TC: O(N * log(S)), N = weights, S = sum(weights) - max(weights)
# SC: O(1)


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        maxWeight, totalWeight = -1, 0
        for weight in weights:
            maxWeight = max(maxWeight, weight)
            totalWeight += weight
        left, right = maxWeight, totalWeight
        while left < right:
            mid = (left + right) // 2
            daysNeeded, currWeight = 1, 0
            for weight in weights:
                if currWeight + weight > mid:
                    daysNeeded += 1
                    currWeight = 0
                currWeight += weight
            if daysNeeded > days:
                left = mid + 1
            else:
                right = mid
        return left