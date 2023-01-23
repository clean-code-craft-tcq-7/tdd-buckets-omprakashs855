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

    def get_range(self, data):
        # To get range
        range_list = []
        while True:
            if len(data) == 0:
                break
            else:
                nested_list = []
                min_idx = 0
                max_idx = min_idx
                for idx, val in enumerate(data):
                    if (val - data[max_idx]) == 0:
                        nested_list.append(val)
                        pass
                    elif (val - data[max_idx]) == 1:
                        max_idx = idx
                        nested_list.append(val)
                    else:
                        break
                if len(data) == 1:
                    break
                data = data[idx:]
                range_list.append(nested_list)
        return range_list

    def get_reading_count(self, input_array):
        range_list = self.get_range(sorted(input_array))
        out_string_list = []
        for val in range_list:
            out_string = str(min(val)) + "-" + str(max(val)) + ", " + str(len(val))
            out_string_list.append(out_string)
        print(out_string_list)
        return out_string_list
    
    def get_csv_format(self):
        # Print csv output data
        pass
