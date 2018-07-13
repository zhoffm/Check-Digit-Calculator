from unittest import TestCase
from check_digit_calc import UniversalProductCodeConverter

test_obj = UniversalProductCodeConverter()

test_obj.input_string = '12345678901'


class TestUniversalProductCodeConverter(TestCase):
    def test_len_check(self):
        self.assertEqual(len(test_obj.input_string), 11)

    def test_check_integer(self):
        test_obj.check_integer()
        self.assertEqual(test_obj.input_integer, 12345678901)

    def test_step_1(self):
        test_obj.step_1()
        self.assertEqual(test_obj.odd_sum, 26)

    def test_step_2(self):
        test_obj.step_2()
        self.assertEqual(test_obj.even_sum, 20)

    def test_step_3(self):
        test_obj.step_3()
        self.fail()

    def test_step_4(self):
        test_obj.step_4()
        self.fail()

    def test_step_5(self):
        test_obj.step_5()
        self.fail()

    def test_convert_upc(self):
        self.fail()
