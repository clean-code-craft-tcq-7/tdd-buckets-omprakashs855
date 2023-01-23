import os
import subprocess
import json

class ChargingSession:
    
    def __init__(self):
        self.test_case_json = "test_case.json"
        self.json_tc = "Test Case"
        self.range = "Range Output"
        self.input = "Input Array"
        self.root_dir = subprocess.Popen(['git', 'rev-parse', '--show-toplevel'],
                                    stdout=subprocess.PIPE).communicate()[0].rstrip().decode('utf-8')
    

    # Pure Function Inside Class
    def get_json_path(self, json_file_name, root_dir):
        for roots, _, files in os.walk(root_dir):
            if json_file_name in files:
                return os.path.join(roots, json_file_name)

    def get_json_data(self, json_path):
        with open(json_path, "r") as jsonread:
            json_data = json.load(jsonread)
        return json_data

    def null_data_check(self, data):
        if len(data) == 0:
            return False
        else:
            return True
    
    def single_data_check(self, data):
        global range_list
        if len(data) == 1:
            range_list.append(data)
            return False
        else:
            return True
    
    def get_range(self, data):
        global range_list
        # To get range
        range_list = []
        data_check_flag = int(self.null_data_check(data)) * int(self.single_data_check(data))
        while bool(data_check_flag):
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
                if max(range_list[-1]) != nested_list[-1]:
                    range_list.append(nested_list)
                break
            data = data[idx:]
            range_list.append(nested_list)
        return range_list

    def get_reading_count(self, input_array):
        range_list = self.get_range(sorted(input_array))
        out_string_list = []
        for val in range_list:
            if min(val) == max(val):
                out_string = str(min(val)) + ", " + str(len(val))
            else:
                out_string = str(min(val)) + "-" + str(max(val)) + ", " + str(len(val))
            out_string_list.append(out_string)
        
        return self.get_csv_format(out_string_list)
    
    def get_csv_format(self, out_string_list):
        print("Range, Reading")
        for data in out_string_list:
            print(data)
        # Print csv output data
        return out_string_list
