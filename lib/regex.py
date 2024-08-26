import re

# Define the regular expression pattern
pattern = r"""
    It's\ such\ a\ lovely\ day\ today\.|
    Some\ weather\ we're\ having\ today,\ huh\?|
    Maybe\ today's\ just\ not\ my\ day\.
"""

# Compile the pattern with appropriate flags
my_regex = re.compile(pattern, re.VERBOSE | re.MULTILINE)

# Test the regex with the given test cases
if __name__ == "__main__":
    import unittest

    class TestRegEx(unittest.TestCase):
        def test_matches_its_such_a_lovely_day(self):
            '''matches the string "It's such a lovely day today."'''
            self.assertIsNotNone(my_regex.fullmatch("It's such a lovely day today."))

        def test_matches_some_weather_were_having(self):
            '''matches the string "Some weather we're having today, huh?"'''
            self.assertIsNotNone(my_regex.fullmatch("Some weather we're having today, huh?"))

        def test_matches_maybe_todays_not_my_day(self):
            '''matches the string "Maybe today's just not my day."'''
            self.assertIsNotNone(my_regex.fullmatch("Maybe today's just not my day."))

        def test_finds_all_matches(self):
            '''can be used to find these three strings and ONLY these three strings.'''
            matches = my_regex.findall(FINDALL_STRING) # type: ignore
            self.assertEqual(matches, [
                "It's such a lovely day today.",
                "Some weather we're having today, huh?",
                "Maybe today's just not my day.",
            ])

    unittest.main()
