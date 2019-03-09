import unittest

class atest(unittest.TestCase):
    def setUp(self):
        print('one test begin')
    def tearDown(self):
        print('one tesr over')
    @classmethod
    def tearDownClass(cls):
        print('all test over ')

    @classmethod
    def setUpClass(cls):
        print('begin test')

    def test_a(self):
        self.assertEqual(2,2)
    def test_b(self):
        self.assertEqual('yes','yes')

if __name__=='__main__':
    unittest.main()#运行所有测试用例


