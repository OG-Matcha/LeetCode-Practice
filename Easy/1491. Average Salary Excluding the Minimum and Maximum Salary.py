# easy

'''
You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.
'''

# 　https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/description/


class Solution:
    def average(self, salary: List[int]) -> float:

        maxi = max(salary)
        mini = min(salary)

        return (sum(salary) - maxi - mini) / (len(salary) - 2)

# Time complexity = O(n) where n is the number of elements in salary
# Space complexity = O(1)
