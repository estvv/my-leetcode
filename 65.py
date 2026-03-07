class Number:
    s: str
    negative: bool = False
    value: int | None = None
    floating_value: int | None = None
    exponential_value: int

    def __init__(self, s: str):
        self.s = s

    def parse_sign(self):
        if len(self.s) < 1:
            raise Exception()
        if self.s[0] == '-':
            self.negative = True
            self.s = self.s[1:len(self.s)]
        elif self.s[0] == '+':
            self.s = self.s[1:len(self.s)]
        else:
            if not self.s[0].isdigit() and not (self.s[0] == '.' or self.s[0] == 'e' or self.s[0] == 'E'):
                # print("SIGN ERROR")
                raise Exception()

        # print("Sign:", self.negative)
        # print(self.s)

    def parse_value(self):
        i = 0

        while i < len(self.s) and self.s[i].isdigit():
            i += 1

        if i < len(self.s) and not self.s[i].isdigit() and not (self.s[i] == '.' or self.s[i] == 'e' or self.s[i] == 'E'):
            # print("ALPHABET ERROR IN VALUE")
            raise Exception()

        if i != 0:
            self.value = int(self.s[0:i])

            self.s = self.s[i:len(self.s)]

        # print("Value: ", self.value)
        # print(self.s)

    def parse_floating_value(self):
        if len(self.s) > 0 and self.s[0] == '.':
            self.s = self.s[1:len(self.s)]

            i = 0

            while i < len(self.s) and self.s[i].isdigit():
                i += 1

            if i < len(self.s) and not self.s[i].isdigit() and not (self.s[i] == 'e' or self.s[i] == 'E'):
                # print("ALPHABET ERROR IN FLOATING VALUE")
                raise Exception()

            if i != 0:
                self.floating_value = int(self.s[0:i])

                self.s = self.s[i:len(self.s)]
            else:
                if self.value == None:
                    raise Exception()
            # print("Float Value: ", self.floating_value)
            # print(self.s)

    def parse_exponent(self):
        if len(self.s) > 0 and (self.s[0] == 'e' or self.s[0] == 'E'):
            self.s = self.s[1:len(self.s)]

            if len(self.s) < 1:
                raise Exception()
            if self.s[0] == '-' or self.s[0] == '+':
                self.s = self.s[1:len(self.s)]
            else:
                if not self.s[0].isdigit() and not (self.s[0] == '.' or self.s[0] == 'e' or self.s[0] == 'E'):
                    # print("SIGN ERROR")
                    raise Exception()

            i = 0

            while i < len(self.s) and self.s[i].isdigit():
                i += 1

            if i < len(self.s) and not self.s[i].isdigit() and not (self.s[i] == '.' or self.s[i] == 'e' or self.s[i] == 'E'):
                # print("ALPHABET ERROR IN EXPONENT")
                raise Exception()

            self.exponential_value = int(self.s[0:i])

            self.s = self.s[i:len(self.s)]

            if self.value == None and self.floating_value == None:
                raise Exception()

            # print("Exponnet Value: ", self.exponential_value)
            # print(self.s)

            if len(self.s) != 0:
                raise Exception()

        if self.value == None and self.floating_value == None and self.exponential_value == None:
            raise Exception()

class Solution:
    def isNumber(self, s: str) -> bool:
        n = Number(s.strip())

        try:
            n.parse_sign()
            n.parse_value()
            n.parse_floating_value()
            n.parse_exponent()
        except:
            return False

        return True
