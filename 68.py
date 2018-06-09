class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if maxWidth <= 0:
            return []
        ret = []
        nowLen = 0
        nowline = [];
        for word in words:
            if len(word) <= 0:
                continue
            if nowLen + len(word) + len(nowline) > maxWidth:
                appendline = ""
                sp= (maxWidth - nowLen)
                for w in nowline:
                    appendline += w

                nowline = [word]
                nowLen = 0
            else:
                nowLen += len(word)
                nowline += word
        return ret
