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
        
        json_data = obj.get_json_data(obj.get_json_path(obj.test_case_json))
            
        for dt in json_data[obj.json_tc]:
            result = obj.get_reading_count(dt[obj.input])
            self.assertEqual(result, dt[obj.range])

if __name__ == "__main__":
    unittest.main()