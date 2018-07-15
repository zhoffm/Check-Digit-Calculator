from random import randint
import pandas as pd


def random_11_digit_upc():
    upc_string = ''.join(["%s" % randint(0, 9) for num in range(0, 11)])
    print(upc_string)
    return upc_string

# Class to calculate the check digit for 11 digit UPC's


class CheckDigitCalculations:
    def __init__(self):
        self.input_string = None
        self.input_integer = None
        self.odd_sum = None
        self.odd_sum_times_3 = None
        self.even_sum = None
        self.new_sum = None
        self.m = None
        self.check_digit = None

    def len_check(self):
        if len(self.input_string) == 11:
            return True
        else:
            return False

    def check_integer(self):
        try:
            self.input_integer = int(self.input_string)
        except ValueError:
            print('The entered string is not exclusively numeric.')

    # 1. Sum the digits at odd-numbered positions (first, third, fifth,..., eleventh).
    def step_1(self):
        self.odd_sum = sum(int(self.input_string[i]) for i, j in enumerate(self.input_string) if i % 2 == 0)

    # 2. Multiply the result by 3.
    def step_2(self):
        self.odd_sum_times_3 = 3 * self.odd_sum

    # 3. Add the digit sum at even-numbered positions (second, fourth, sixth,..., tenth) to the result.
    def step_3(self):
        self.even_sum = sum(int(self.input_string[i]) for i, j in enumerate(self.input_string) if i % 2 != 0)
        self.new_sum = self.even_sum + self.odd_sum_times_3

    # 4. Find the result modulo 10 (i.e. the remainder, when divided by 10) and call it M.
    def step_4(self):
        self.m = self.new_sum % 10

    # 5. If M is zero, then the check digit is 0; otherwise the check digit is 10 − M.
    def step_5(self):
        if self.m == 0:
            self.check_digit = 0
        else:
            self.check_digit = 10 - self.m

    # Do all the steps. This runs all the previous steps.
    def compute_check_digit(self, input_upc):
        self.input_string = input_upc
        if self.len_check():
            self.step_1()
            self.step_2()
            self.step_2()
            self.step_3()
            self.step_4()
            self.step_5()
            return self.check_digit
        else:
            return ''


class RawUniversalProductCodeConditioning(CheckDigitCalculations):
    def __init__(self):
        super().__init__()
        self.input_file_path = None
        self.input_file = None
        self.upc_df = pd.DataFrame()

    def read_file_into_df(self, input_file_path, input_file):
        self.input_file_path = input_file_path
        self.input_file = input_file
        self.upc_df = pd.read_csv(self.input_file_path + self.input_file, dtype={'REFCODE': str}, na_filter=False)

    def add_updated_upc_to_df(self):
        pass




if __name__ == '__main__':
    test_upc = random_11_digit_upc()
    obj = CheckDigitCalculations()
    obj.compute_check_digit(test_upc)
    print(obj.check_digit)
