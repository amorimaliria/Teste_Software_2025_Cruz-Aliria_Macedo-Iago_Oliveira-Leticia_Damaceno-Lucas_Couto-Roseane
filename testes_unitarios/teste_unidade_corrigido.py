import unittest

l = [["foo", "a", "a"], ["bar", "a", "b"], ["lee", "b", "b"]]

def create_test(name, a, b):
    def test(self):
        self.assertEqual(a, b)
    test.__name__ = f'test_{name}'
    return test

class TestSequence(unittest.TestCase):
    pass

for name, a, b in l:
    test_method = create_test(name, a, b)
    setattr(TestSequence, test_method.__name__, test_method)

if __name__ == '__main__':
    unittest.main()
