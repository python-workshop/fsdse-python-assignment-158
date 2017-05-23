from unittest import TestCase


class TestSort(TestCase):
    def test_sort(self):
        try:
            from build import sort
        except ImportError:
            self.assertFalse("no function found")
        self.assertRaises(TypeError, sort, None)
        data = ['ram', 'act', 'arm', 'bat', 'cat', 'tab']
        expected = ['ram', 'arm', 'act', 'cat', 'bat', 'tab']
        self.assertEqual(sort(data), expected)

