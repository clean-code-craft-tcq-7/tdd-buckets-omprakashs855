import os
import subprocess

class ChargingSession:
    
    def __init__(self):
        self.test_case_json = "test_case.json"
        self.json_tc = "Test Case"
        self.range = "Range Output"
        self.input = "Input Array"
    
    # Pure Function Inside Class
    def get_json_path(self):
        root_dir = subprocess.Popen(['git', 'rev-parse', '--show-toplevel'],
                                    stdout=subprocess.PIPE).communicate()[0].rstrip().decode('utf-8')
        for roots, _, files in os.walk(root_dir):
            for file in files:
                if self.test_case_json ==  file:
                    return os.path.join(roots, file)

    # Feature Specification functions
    def sort_array(self):
        # Function To Sort input array/list
        pass

    def get_range(self):
        # To get range
        pass

    def get_reading_count(self):
        # Main function called by Test
        pass
    
    def get_csv_format(self):
        # Print csv output data
        pass

# if __name__== "__main__":
#     obj = ChargingSession()
#     a = obj.get_json_path()
#     print(a)