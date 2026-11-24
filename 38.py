class Solution:
    def countAndSay(self, n: int) -> str:
        base = "1"
        res = base

        while n != 1:
            res = ""

            j = 0
            while j < len(base):
                counter = 0
                k = j

                while k < len(base) and base[j] == base[k]:
                    counter += 1
                    k += 1

                res += str(counter) + base[j]
                j += counter

            base = res
            n -= 1

        return res


Solution().countAndSay(1) # "1"
Solution().countAndSay(2) # "11"
Solution().countAndSay(3) # "21"
Solution().countAndSay(4) # "1211"
