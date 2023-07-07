# medium

'''
A teacher is writing a test with n true/false questions, with 'T' denoting true and 'F' denoting false. He wants to confuse the students by maximizing the number of consecutive questions with the same answer (multiple trues or multiple falses in a row).

You are given a string answerKey, where answerKey[i] is the original answer to the ith question. In addition, you are given an integer k, the maximum number of times you may perform the following operation:

Change the answer key for any question to 'T' or 'F' (i.e., set answerKey[i] to 'T' or 'F').
Return the maximum number of consecutive 'T's or 'F's in the answer key after performing the operation at most k times.
'''

# https://leetcode.com/problems/maximize-the-confusion-of-an-exam/description/


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        maxi = k
        left = 0
        count = collections.Counter(answerKey[:k])

        for right in range(k, len(answerKey)):
            count[answerKey[right]] += 1

            while min(count["T"], count["F"]) > k:
                count[answerKey[left]] -= 1
                left += 1

            maxi = max(maxi, right - left + 1)

        return maxi

# Time complexity = O(n) where n is the length of answerKey
# Space complexity = O(1)
