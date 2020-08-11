class Solution:
    def findWords(self, words):
        rowdict = {}
        for c in "qwertyuiopQWERTYUIOP":
            rowdict[c] = 1
        for c in "asdfghjklASDFGHJKL":
            rowdict[c] = 2
        for c in "zxcvbnmZXCVBNM":
            rowdict[c] = 3
        res = []
        for word in words:
            if len(set(rowdict[c] for c in word)) == 1:
                res.append(word)
        return res
val=Solution()
words=list(map(str,input().split()))
print(val.findWords(words))
