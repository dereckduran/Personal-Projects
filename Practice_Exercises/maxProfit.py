import typing

def maxProfit(prices: list[int]) -> int:
        totalmax, currentmax = 0, 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                if prices[j] < prices[i]:
                    continue
                if prices[j] > prices[i]:
                    currentmax = max(currentmax, prices[j] - prices[i])
            totalmax = max(totalmax, currentmax)

        return totalmax

if __name__ == "__main__":
    prices = [2,4,1]
    print(maxProfit(prices))

    