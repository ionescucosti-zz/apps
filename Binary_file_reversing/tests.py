import unittest
from binary_reverse import read_input, write_output


class Testing(unittest.TestCase):

    def test_read_input(self):
        self.assertIsNotNone(read_input('sample.bin'))
        self.assertRaises(Exception, lambda: read_input('sample.txt'))

    def test_length_data_equality(self):
        input_data = read_input('sample.bin')
        output_data = write_output(input_data)
        self.assertEqual(len(input_data[0]), len(output_data))

    def test_reversed_elements(self):
        input_data = read_input('sample.bin')
        output_data = write_output(input_data)
        passed = True
        for i, o in zip(input_data[0][::-1], output_data):
            if hex(i)!=hex(o):
                passed = False
                break
        self.assertEqual(passed, True)


if __name__ == '__main__':
    unittest.main()