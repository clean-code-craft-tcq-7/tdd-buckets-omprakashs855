import os
import math

class A2D_Convertor:

    def __init__(self):
        self.json_tc_a2d = "Test Case A2D"
        self.input = "Input Array"

    def check_nth_bit_array_size(self, nth_bit, Input_array):
        result = False
        if len(Input_array) == nth_bit:
            result = True
        return result

    def A2D(self, input_array):
        A2D_output = 0
        for idx, bit in enumerate(input_array[::-1]):
            A2D_output += math.pow(2,idx)*bit
        return A2D_output
    
    def max_A2D(self, nth_bit):
        max_dec = 0
        max_dec = self.A2D([1 for i in range(0,nth_bit)])
        return max_dec

    def round_off_val(self, dec_val, max_dec, max_Amps):
        return int((dec_val*max_Amps)/max_dec)+1

    def get_current_conv_amp(self, dt):
        nth_bit_check = self.check_nth_bit_array_size(dt["nth_bit_value"], dt["Input Array"])
        if nth_bit_check:
            max_dec = self.max_A2D(dt["nth_bit_value"])
            dec_val = self.A2D(dt["Input Array"])
            result_output = self.round_off_val(dec_val, max_dec, dt["Max Amps"])
        return result_output