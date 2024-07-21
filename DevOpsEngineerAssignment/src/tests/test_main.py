import unittest
from src.main import list_aws_resources

class TestMain(unittest.TestCase):
    def test_list_aws_resources(self):
        self.assertIsNone(list_aws_resources())

if __name__ == '__main__':
    unittest.main()
