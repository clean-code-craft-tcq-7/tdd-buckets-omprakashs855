import unittest
import json
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
from src.charging_session import ChargingSession as CS
from src.a2d_convertor import A2D_Convertor as A2D

class TestChargingSession(unittest.TestCase):

    def test_get_reading_count(self):

        # Creating ChargingSession Class Object
        obj = CS()

        # Creating a Separate A2D Class Object
        obj_a2d = A2D()
        
        json_data = obj.get_json_data(obj.get_json_path(obj.test_case_json, obj.root_dir))
            
        for dt in json_data[obj.json_tc]:
            result = obj.get_reading_count(dt[obj.input])
            self.assertEqual(result, dt[obj.range])
        
        for dt_a2d in json_data[obj_a2d.json_tc_a2d]:
            result_a2d = obj_a2d.get_current_conv_amp(dt_a2d)
            self.assertEqual(result_a2d, dt_a2d["Output"])

if __name__ == "__main__":
    unittest.main()