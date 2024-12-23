import unittest
import pandas as pd
from validate_functions import validate_vict_sex, validate_vict_age

class TestValidateFunctions(unittest.TestCase):
    def setUp(self):
        # Sample data
        self.valid_data = pd.DataFrame({
            'Vict Sex': ['M', 'F'],
            'Vict Age': [25, 45]
        })
        self.invalid_sex_data = pd.DataFrame({
            'Vict Sex': ['M', 'X', None],
            'Vict Age': [25, 45, 50]
        })
        self.invalid_age_data = pd.DataFrame({
            'Vict Sex': ['M', 'F'],
            'Vict Age': [0, 101]
        })

    def test_validate_vict_sex(self):
        self.assertTrue(validate_vict_sex(self.valid_data).empty)
        self.assertFalse(validate_vict_sex(self.invalid_sex_data).empty)

    def test_validate_vict_age(self):
        self.assertTrue(validate_vict_age(self.valid_data).empty)
        self.assertFalse(validate_vict_age(self.invalid_age_data).empty)

if __name__ == "__main__":
    unittest.main()
