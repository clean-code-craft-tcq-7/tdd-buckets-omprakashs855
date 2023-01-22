import os
import subprocess
import json

class ChargingSession:
    
    def __init__(self):
        self.test_case_json = "test_case.json"
        self.json_tc = "Test Case"
        self.range = "Range Output"
        self.input = "Input Array"
    
    # Pure Function Inside Class
    def get_json_path(self, json_file_name):
        root_dir = subprocess.Popen(['git', 'rev-parse', '--show-toplevel'],
                                    stdout=subprocess.PIPE).communicate()[0].rstrip().decode('utf-8')
        for roots, _, files in os.walk(root_dir):
            for file in files:
                if json_file_name ==  file:
                    return os.path.join(roots, file)

    def get_json_data(self, json_path):
        with open(json_path, "r") as jsonread:
            json_data = json.load(jsonread)
        return json_data

    def get_range(self, sort_list):
        # To get range
        range_list = []
        min_val = sort_list[0]
        max_val = sort_list[1]
        if (max_val-min_val) < 2:
            range_list = sort_list
        return range_list, min_val, max_val

    def get_reading_count(self, input_array):
        # Sorting input array
        input_array.sort()
        range_list, min, max = self.get_range(input_array)
        length_count = len(range_list)
        # Main function called by Test
        str_data = str(min) + "-" + str(max) + ", " + str(length_count)
        return str_data
    
    def get_csv_format(self):
        # Print csv output data
        pass
