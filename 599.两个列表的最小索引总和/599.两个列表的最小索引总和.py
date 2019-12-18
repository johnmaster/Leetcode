"""
执行用时 :1020 ms, 在所有 python3 提交中击败了5.01%的用户
内存消耗 :13 MB, 在所有 python3 提交中击败了100.00%的用户
"""


class Solution:
    def findRestaurant(self, list1, list2):
        hash = {}
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    if hash.get(i + j):
                        hash[i + j].append(list1[i])
                    else:
                        hash[i + j] = [list1[i]]
        return hash[min(hash)]
