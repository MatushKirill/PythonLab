import unittest
import ser_json
import ser_pickle
import ser_yaml
import test_util

from model import LastResults
from unittest.mock import patch
from unittest.mock import MagicMock


class TestStringMethods(unittest.TestCase):
    def test_json(self):
        """
        test json serializer

        """
        stream = test_util.get_stringio()
        res = LastResults()
        res.add_result(2)
        res.add_result(2)
        res.add_result(3)
        res.add_result(4)
        ser_json.write(res, stream)
        stream.seek(0)
        res2 = ser_json.read(stream)
        self.assertEqual(res.lastResult, res2.lastResult)

    def test_pickle(self):
        """
        test pickle serializer

        """
        stream = test_util.get_bytesio()
        res = LastResults()
        res.add_result(1)
        res.add_result(2)
        res.add_result(3)
        res.add_result(4)
        ser_pickle.write(res, stream)
        stream.seek(0)
        res2 = ser_pickle.read(stream)
        self.assertEqual(res.lastResult, res2.lastResult)

    def test_yaml(self):
        """
        test yaml serializer

        """
        stream = test_util.get_stringio()
        res = LastResults()
        res.add_result(1)
        res.add_result(2)
        res.add_result(3)
        res.add_result(4)
        ser_yaml.write(res, stream)
        stream.seek(0)
        res2 = ser_yaml.read(stream)
        self.assertEqual(res.lastResult, res2.lastResult)

if __name__ == '__main__':
    unittest.main()