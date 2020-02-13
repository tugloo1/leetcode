class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        to_return = 0
        for i, numeral in enumerate(s):
            value = roman_map[numeral]
            to_return += value
            if i == len(s) - 1:
                continue
            next_num = s[i+1]
            if numeral == 'I' and (next_num == 'V' or next_num == 'X'):
                to_return -= 2
            elif numeral == 'X' and (next_num == 'L' or next_num == 'C'):
                to_return -= 20
            elif numeral == 'C' and (next_num == 'D' or next_num == 'M'):
                to_return -= 200

        return to_return
