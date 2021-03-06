import unittest

from case_converter import snake_case_to_camel_case, camel_case_to_snake_case


class CaseConverterTest(unittest.TestCase):
    def test_snake_case_to_camel_case(self):
        snake_str = 'case_converter_test'
        self.assertEqual(snake_case_to_camel_case(snake_str), 'caseConverterTest')

    def test_camel_case_to_snake_case(self):
        camel_str = 'caseConverterTest'
        self.assertEqual(camel_case_to_snake_case(camel_str), 'case_converter_test')

if __name__ == '__main__':
    unittest.main()
