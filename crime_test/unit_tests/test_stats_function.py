import unittest
import pandas as pd
from stats_function import calculate_mean_age, calculate_median_age

class TestStatsFunctions(unittest.TestCase):
    def setUp(self):
        # Sample data
        self.data = pd.DataFrame({'Vict Age': [25, 45, 35, 50, 60]})
        self.edge_case_data = pd.DataFrame({'Vict Age': [100]})

    def test_calculate_mean_age(self):
        self.assertEqual(calculate_mean_age(self.data), 43.0)

    def test_calculate_median_age(self):
        self.assertEqual(calculate_median_age(self.data), 45.0)

    def test_edge_case(self):
        self.assertEqual(calculate_mean_age(self.edge_case_data), 100.0)
        self.assertEqual(calculate_median_age(self.edge_case_data), 100.0)

if __name__ == "__main__":
    unittest.main()
