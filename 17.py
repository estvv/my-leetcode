class Solution(object):
    def letterCombinations(self, digits):
        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        if len(digits) == 0:
            return []

        final = [""]

        for number in digits:
            temp_list = []
            for comb in final:
                for letter in keyboard[number]:
                    temp_list.append(comb + letter)
            final = temp_list

        return final
