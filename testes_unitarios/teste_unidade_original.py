import unittest

l = [["foo", "a", "a"], ["bar", "a", "b"], ["lee", "b", "b"]]

class TestSequence(unittest.TestCase):
    def testsample(self):
        for name, a, b in l:
            print("test", name)
            self.assertEqual(a, b)

if __name__ == '__main__':
    unittest.main()