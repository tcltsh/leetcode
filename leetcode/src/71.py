class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        arr = path.split('/')
        stack = []
        for r in arr:
            if r == "..":
                if len(stack) > 0:
                    stack.pop(-1)
            elif r == '.' or r == '':
                continue
            else:
                stack.append(r)

        return '/' + '/'.join(stack)
