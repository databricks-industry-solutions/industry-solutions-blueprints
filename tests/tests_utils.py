import unittest



class UtilTest(unittest.TestCase):

  def test_hello(self):
    self.assertFalse('hello' == 'world')
    print('Hello World')


if __name__ == '__main__':
  unittest.main()
