class Solution(object):
    def count_append(self, maxWidth, nowLen, nowline):
        sp= (maxWidth - nowLen)
        wsp = [0] * len(nowline)
        flag = 0
        for i in range(0, sp):
            wsp[flag] += 1
            if len(nowline) - 1 > 0:
                flag = (flag + 1) % (len(nowline) - 1)
            else:
                flag = (flag + 1) % len(nowline)
        append_str = ""
        for i in range(0, len(nowline)):
            append_str += nowline[i]
            if i != 0 and i == len(nowline) - 1:
                continue
            append_str += (' ' * wsp[i])
        return append_str

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
                append_str = self.count_append(maxWidth, nowLen, nowline)
                ret.append(append_str)

                nowline = [word]
                nowLen = len(word)
            else:
                nowLen += len(word)
                nowline.append(word)
        if len(nowline) > 0:
            append_str = ""
            for st in nowline:
                append_str += st
                if len(append_str) < maxWidth:
                    append_str += ' '
            append_str += (' ' * (maxWidth - len(append_str)))
            ret.append(append_str)
        return ret

if __name__ == "__main__":
    s = Solution()
    r = s.fullJustify(["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"], 20)
    print(r)
    for i in r:
        print(len(i))
