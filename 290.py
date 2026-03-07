class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        save = {}
        tab = s.split()
        i = 0

        # print(s, tab)

        if len(tab) != len(pattern):
            return False

        while i < len(pattern):
            if not pattern[i] in save.keys():
                if tab[i] in save.values():
                    return False
                save[pattern[i]] = tab[i]
            else:
                # print(save)
                if save[pattern[i]] != tab[i]:
                    # print(save[pattern[i]], tab[i])
                    return False
            i += 1

        # print(save)

        return True

print(Solution().wordPattern("abba", "dog cat cat dog"))
print(Solution().wordPattern("abba", "dog cat cat fish"))
print(Solution().wordPattern("aaaa", "dog cat cat dog"))
print(Solution().wordPattern("abba", "dog dog dog dog"))

