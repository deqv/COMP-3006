# Varun Suresh
# 873569280
# This program counts the frequency of the characters that appear in the files that it is fed.

import count
import unittest

class TestSum(unittest.TestCase):

    def test_count_main_without_flags(self):
# The following line tests if count.py runs successfully without any flags.
        count.main()
        assert True

# The following lines of code test all the different combinations of flags.
    def test_count_main_with_all_flags(self):
        sys.argv = ["-c", "-l", "-z", "test.txt"]
        count.main()
        assert True

    def test_count_main_with_a_few_flags(self):
        sys.argv = ["-c", "-z", "test.txt"]
        count.main()
        assert True

    def test_count_main_with_a_few_flags(self):
        sys.argv = ["-c", "-l", "test.txt"]
        count.main()
        assert True

    def test_count_main_with_a_few_flags(self):
        sys.argv = ["-l", "-z", "test.txt"]
        count.main()
        assert True

    def test_count_main_with_a_few_flags(self):
        sys.argv = ["-c", "-z", "test.txt"]
        count.main()
        assert True

    def test_count_main_with_a_few_flags(self):
        sys.argv = ["-c", "-z", "test.txt"]
        count.main()
        assert True

    def test_count_main_with_a_few_flags(self):
        sys.argv = ["-z", "test.txt"]
        count.main()
        assert True

    def test_count_main_with_a_few_flags(self):
        sys.argv = ["-c", "test.txt"]
        count.main()
        assert True

    def test_count_main_with_a_few_flags(self):
        sys.argv = ["-l", "test.txt"]
        count.main()
        assert True
