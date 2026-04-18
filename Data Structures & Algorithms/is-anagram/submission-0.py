class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arrA = []
        arrB = []
        for i in range(len(s)):
            arrA.append(s[i])
        for j in range(len(t)):
            arrB.append(t[j])
        # print(arrA)
        # print(arrB)
        arrA.sort()
        arrB.sort()
        return arrA == arrB

        