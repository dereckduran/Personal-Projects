import typing 
def minCostClimbingStairs(cost: list[int]) -> int:
    def sumPrev(cost: list[int], index: int):
        if index < 0:
            return 0

        return min(cost[index] + sumPrev(cost, index - 1), cost[index] + sumPrev(cost, index - 2))
    
    return sumPrev(cost, len(cost) - 1)


costs = [10,15, 20]

print(minCostClimbingStairs(costs))