class Solution(object):
    def mul(self, num, s, leed):
        ret = ""
        if leed > 0:
            ret += "0" * leed
        add = 0

        si = ord(s) - ord('0')

        for i in range(len(num)-1, -1, -1):
            mul = (ord(num[i]) - ord('0')) * si + add
            ret += chr(mul % 10 + ord('0'))
            add = mul // 10

        if add > 0:
            ret += chr(add + ord('0'))
        return ret

    def add(self, adds):
        ret = ""
        now = 0
        over = False
        mem = 0
        while not over:
            over = True
            nowadd = mem
            for add in adds:
                if len(add) > now:
                    over = False
                    nowadd += ord(add[now]) - ord('0')
            if over:
                break
            ret += chr(nowadd % 10 + ord('0'))
            mem = nowadd // 10
            now += 1
        if mem > 0:
            ret += chr(mem + ord('0'))
        ret = ret[::-1]
        while ret[0] == "0" and len(ret) > 1:
            ret = ret[1:]
        return ret

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        adds = []

        leed = 0
        for i in range(len(num2)-1, -1, -1):
            adds.append(self.mul(num1, num2[i], leed))
            leed += 1
        return self.add(adds)

if __name__ == "__main__":
    s = Solution()
    print s.multiply("1234", "5678")
    print s.multiply("1234", "0")

