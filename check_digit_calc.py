# Class to calculate the check digit for 11 digit UPC's

class UniversalProductCodeConverter:
    def __init__(self):
        self.input_string = None
        self.input_integer = None
        self.odd_sum = None
        self.odd_sum_times_3 = None
        self.even_sum = None
        self.m = None
        self.check_digit = None

    def len_check(self):
        if len(self.input_string) == 11:
            return True
        else:
            return False

    def convert_to_integer(self):
        pass

    # 1. Sum the digits at odd-numbered positions (first, third, fifth,..., eleventh).
    def step_1(self):
        pass

    # 2. Multiply the result by 3.
    def step_2(self):
        pass

    # 3. Add the digit sum at even-numbered positions (second, fourth, sixth,..., tenth) to the result.
    def step_3(self):
        pass

    # 4. Find the result modulo 10 (i.e. the remainder, when divided by 10) and call it M.
    def step_4(self):
        pass

    # 5. If M is zero, then the check digit is 0; otherwise the check digit is 10 − M.
    def step_5(self):
        pass

    # Do all the steps. This runs all the previous steps.
    def convert_upc(self):
        pass
