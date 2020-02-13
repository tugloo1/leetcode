from unittest import TestCase


class Solution(object):

    def convert_to_base_string(self, inp_string: str):
        seen_map = {}
        output = ''
        current_num = 1
        for word in inp_string:
            if word not in seen_map:
                seen_map[word] = current_num
                current_num += 1
            output += str(seen_map[word])
        return output

    def convert_word_seq_to_base_string(self, input_word: str):
        seen_map = {}
        output = ''
        current_num = 1
        for word in input_word.split(' '):
            if word not in seen_map:
                seen_map[word] = current_num
                current_num += 1
            output += str(seen_map[word])
        return output

    def wordPattern(self, pattern: str, str: str) -> bool:
        return self.convert_to_base_string(pattern) == self.convert_word_seq_to_base_string(str)


class SolutionTest(TestCase):
    def test_base(self):
        sol = Solution()
        word = 'dog cat cat dog'
        pattern = 'abba'
        self.assertTrue(sol.wordPattern(pattern, word))
        word2 = 'dog cat cat fish'
        self.assertFalse(sol.wordPattern(pattern, word2))