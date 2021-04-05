from unittest import TestCase
from unittest.mock import patch

from homework3.task01 import f


class Test(TestCase):
    @patch("builtins.input", side_effect=["1", "2", "5"])
    def test_limited_cache_times_2(self, mock_input):
        calls_results = [f() for _ in range(8)]
        self.assertEqual(calls_results, ["1", "1", "1", "2", "2", "2", "5", "5"])
