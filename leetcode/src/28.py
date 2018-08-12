def getnext(a, next):
    al = len(a)
    next[0] = -1
    k = -1
    j = 0
    while j < al - 1:
        if k == -1 or a[j] == a[k]:
            j += 1
            k += 1
            next[j] = k
        else:
            k = next[k]


def KmpSearch(a, b):
    next = [0]*len(b)
    getnext(b,next)
    i = j = 0
    al = len(a)
    bl = len(b)
    while i < al and j < bl:
        if j == -1 or a[i] == b[j]:
            i += 1
            j += 1
        else:
            j = next[j]
    if j == bl:
        return i - j
    else:
        return -1

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack is None or needle is None:
            return -1
        if needle == "":
            return 0
        if len(needle) > len(haystack):
            return -1
        return KmpSearch(haystack, needle)
