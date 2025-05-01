# https://leetcode.com/problems/closest-dessert-cost
"""
You would like to make dessert and are preparing to buy the ingredients. You have n ice cream base flavors 
and m types of toppings to choose from. You must follow these rules when making your dessert:

There must be exactly one ice cream base.
You can add one or more types of topping or have no toppings at all.
There are at most two of each type of topping.
You are given three inputs:

baseCosts, an integer array of length n, where each baseCosts[i] represents the price of the ith ice cream base flavor.
toppingCosts, an integer array of length m, where each toppingCosts[i] is the price of one of the ith topping.
target, an integer representing your target price for dessert.
You want to make a dessert with a total cost as close to target as possible.

Return the closest possible cost of the dessert to target. If there are multiple, return the lower one.

Example 1:
Input: baseCosts = [1,7], toppingCosts = [3,4], target = 10
Output: 10
Explanation: Consider the following combination (all 0-indexed):
- Choose base 1: cost 7
- Take 1 of topping 0: cost 1 x 3 = 3
- Take 0 of topping 1: cost 0 x 4 = 0
Total: 7 + 3 + 0 = 10.

Example 2:
Input: baseCosts = [2,3], toppingCosts = [4,5,100], target = 18
Output: 17
Explanation: Consider the following combination (all 0-indexed):
- Choose base 1: cost 3
- Take 1 of topping 0: cost 1 x 4 = 4
- Take 2 of topping 1: cost 2 x 5 = 10
- Take 0 of topping 2: cost 0 x 100 = 0
Total: 3 + 4 + 10 + 0 = 17. You cannot make a dessert with a total cost of 18.

Example 3:
Input: baseCosts = [3,10], toppingCosts = [2,5], target = 9
Output: 8
Explanation: It is possible to make desserts with cost 8 and 10. Return 8 as it is the lower cost.
 

Constraints:
n == baseCosts.length
m == toppingCosts.length
1 <= n, m <= 10
1 <= baseCosts[i], toppingCosts[i] <= 104
1 <= target <= 104
"""

from sys import maxsize
from typing import List

class Solution:
    def closestCost1(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        base_len = len(baseCosts)
        topping_len = len(toppingCosts)
        k = 2
        greater_cost = maxsize # for all topping and base with cost > target
        lesser_cost = -maxsize # for all topping and base with cost <= target
        for base in baseCosts:
            dp = [False for i in range(target+1)]
            if base>target:
                greater_cost = min(greater_cost, base)
                continue
            else:
                lesser_cost = max(lesser_cost, base) # No topping
                dp[base] = base
            for topping in toppingCosts:
                for tk in range(k):
                    for i in range(target, -1, -1):
                        if dp[i]:
                            t_cost = i+topping
                            if t_cost>target:
                                greater_cost = min(greater_cost, t_cost)
                            else:
                                lesser_cost = max(lesser_cost, t_cost)
                                dp[t_cost] = t_cost
            #         print(f'{base=} {topping=} {dp=}')
            #     print('#'*10)
            # print('-'*10)
        return lesser_cost if (target-lesser_cost)<=(greater_cost-target) else greater_cost
    
    def get_nearest_pair_sum(self, arr, arr_len, k, target):
        spread = 0
        min_spread = maxsize
        s, e = 0, arr_len-1
        while s<=e:
            mid = s + (e-s)//2
            t_cost = arr[mid] + k
            t_spread = target-t_cost
            if abs(t_spread)<min_spread:
                min_spread = abs(t_spread)
                spread = t_spread
            if t_cost>target:
                e = mid-1
            elif t_cost<target:
                s = mid+1
            else:
                break
        return spread

    # This is faster
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        closest = maxsize
        min_spread = maxsize
        baseCosts_len = len(baseCosts)
        baseCosts.sort()
        toppingCosts.sort()
        topping_greater_than_target = maxsize
        dp = [False for i in range(target+1)]
        dp[0] = True
        for topping_cost in toppingCosts: # prepare all possible topping combinations
            double_cost = 2*topping_cost # to cater to two of each topping
            new_costs = list()
            for i in range(target+1):
                if not dp[i]: continue
                t_cost, t2_cost = i + topping_cost, i + double_cost
                if t_cost<=target:
                    new_costs.append(t_cost)
                else:
                    topping_greater_than_target = min(topping_greater_than_target, t_cost)
                if t2_cost<=target:
                    new_costs.append(t2_cost)
                else:
                    topping_greater_than_target = min(topping_greater_than_target, t2_cost)
            for cost in new_costs:
                dp[cost] = True
        # print(f'{dp=}')
        for topping_cost in range(target, -1, -1): # for topping_cost==0 we cal. case with only base and no topping
            if not dp[topping_cost]: continue
            t_spread = self.get_nearest_pair_sum(baseCosts, baseCosts_len, topping_cost, target)
            # print(f'{topping_cost=} {t_spread=} {target=}')
            if abs(t_spread)<min_spread:
                min_spread = abs(t_spread)
                closest = target - t_spread
            elif abs(t_spread)==min_spread and t_spread>0:
                closest = target - t_spread
        if topping_greater_than_target is not maxsize: # case when base is farther than min topping/s >target.
            t_spread = self.get_nearest_pair_sum(baseCosts, baseCosts_len, topping_greater_than_target, target)
            if abs(t_spread)<min_spread:
                min_spread = abs(t_spread)
                closest = target - t_spread
            elif abs(t_spread)==min_spread and t_spread>0:
                closest = target - t_spread
        return closest