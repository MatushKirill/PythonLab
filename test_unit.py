import unittest
import ser_json
import ser_pickle
import ser_yaml

from model import LastResults


class TestStringMethods(unittest.TestCase):

    def test_json(self):
        """
        test json serializer

        """
        res = LastResults()
        res.add_result(1)
        res.add_result(2)
        res.add_result(3)
        res.add_result(4)
        ser_json.write(res)
        res2 = ser_json.read()
        self.assertEqual(res.lastResult, res2.lastResult)

    def test_pickle(self):
        """
        test pickle serializer

        """
        res = LastResults()
        res.add_result(1)
        res.add_result(2)
        res.add_result(3)
        res.add_result(4)
        ser_pickle.write(res)
        res2 = ser_pickle.read()
        self.assertEqual(res.lastResult, res2.lastResult)

    def test_yaml(self):
        """
        test yaml serializer

        """
        res = LastResults()
        res.add_result(1)
        res.add_result(2)
        res.add_result(3)
        res.add_result(4)
        ser_yaml.write(res)
        res2 = ser_yaml.read()
        self.assertEqual(res.lastResult, res2.lastResult)

if __name__ == '__main__':
    unittest.main()