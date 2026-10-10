
import unittest
import pandas as pd

from src.preprocessing import clean_customer_data
from src.duplicate_detector import find_duplicates


class TestDuplicateFinder(unittest.TestCase):

    def test_exact_duplicate(self):
        data = pd.DataFrame([
            {
                "customer_id": 1,
                "name": "Rahul Sharma",
                "email": "rahul@gmail.com",
                "phone": "9876543210"
            },
            {
                "customer_id": 2,
                "name": "Rahul Sharma",
                "email": "rahul@gmail.com",
                "phone": "9876543210"
            }
        ])

        cleaned = clean_customer_data(data)
        results = find_duplicates(cleaned)

        self.assertEqual(len(results), 1)

    def test_different_customers(self):
        data = pd.DataFrame([
            {
                "customer_id": 1,
                "name": "Rahul Sharma",
                "email": "rahul@gmail.com",
                "phone": "9876543210"
            },
            {
                "customer_id": 2,
                "name": "Amit Kumar",
                "email": "amit@gmail.com",
                "phone": "9988776655"
            }
        ])

        cleaned = clean_customer_data(data)
        results = find_duplicates(cleaned)

        self.assertEqual(len(results), 0)


if __name__ == "__main__":
    unittest.main()
