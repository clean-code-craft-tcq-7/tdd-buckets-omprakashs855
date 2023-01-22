import unittest
import json
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
from src.charging_session import ChargingSession as CS

class TestChargingSession(unittest.TestCase):

    def test_get_reading_count(self):

        # Creating ChargingSession Class Object
        obj = CS()

        with open(obj.get_json_path(), "r") as jsonread:
            json_data = json.load(jsonread)
            
            for dt in json_data[obj.json_tc]:
                result = "<Here a function will be called using the json input data, to get_reading_count>"
                self.assertEqual(result, dt[obj.range])

if __name__ == "__main__":
    unittest.main()