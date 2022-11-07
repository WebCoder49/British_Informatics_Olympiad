# RegEx matching
# Recursive, w/ backtracking
# with *, try any numbers then branch


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.match(s, p, 0, 0, len(s), len(p))  # Start from start of pattern, w/o '*'

    def match(self, string: str, pattern: str, string_i: int, pattern_i: int, len_str: int, len_pattern: int):
        """Match a partial RegEx from a position"""
        # print(string[string_i:], pattern[pattern_i:])

        repeating_char = False # True when '*' - don't iterate chars

        while (pattern_i < len_pattern):

            if (pattern_i != len_pattern - 1 and pattern[pattern_i + 1] == "*"):
                repeating_char = True
                # This char can be repeated - branch off for no repeat; match here for repeat
                if (self.match(string, pattern, string_i, pattern_i + 2, len_str, len_pattern)):
                    # Pattern i + 2 as ignoring this char and '*'
                    return True  # If 1 match, valid match

            if(string_i == len_str):
                # No more repeats
                return pattern_i == len_pattern

            if (pattern[pattern_i] == "."):
                # Any char
                string_i += 1
            else:
                if (pattern[pattern_i] == string[string_i]):
                    # Matched
                    string_i += 1
                else:
                    # Not matched
                    return False

            if(not repeating_char):
                pattern_i += 1

        # print(pattern_i, len_pattern)

        return string_i == len_str  # Found whole string if at end of pattern; else not

solution = Solution()
print(solution.isMatch("ab", ".*c"))