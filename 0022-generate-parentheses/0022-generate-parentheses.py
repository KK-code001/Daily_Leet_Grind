class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def is_valid(s):
            balance = 0

            for ch in s:
                if ch == '(':
                    balance += 1
                else:
                    balance -= 1

                if balance < 0:
                    return False

            return balance == 0

        def generate(s):
            if len(s) == 2 * n:
                if is_valid(s):
                    result.append(s)
                return

            generate(s + '(')
            generate(s + ')')

        generate("")
        return result