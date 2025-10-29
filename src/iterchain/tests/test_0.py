import types
import unittest

from iterchain.core import iterchain


class TestIterchain(unittest.TestCase):
    def test_depth_1_flattens_one_level(self):
        data = [[1, 2], [3], []]
        self.assertEqual(list(iterchain(data, depth=1)), [1, 2, 3])

    def test_depth_2_flattens_two_levels(self):
        data = [[[1], [2, 3]], [[4]], []]
        self.assertEqual(list(iterchain(data, depth=2)), [1, 2, 3, 4])

    def test_inv(self):
        data = [[[1], [2, 3]], [[4]], []]
        for n in range(5):
            self.assertEqual(list(iterchain(iterchain(data, depth=-n), depth=n)), data)

    def test_depth_0_iterates_input(self):
        data = (1, 2, 3)
        self.assertEqual(list(iterchain(data, depth=0)), [1, 2, 3])

    def test_depth_minus_1_yields_data_as_single_element(self):
        data = [1, 2, 3]
        out = list(iterchain(data, depth=-1))
        self.assertEqual(out, [data])  # data yielded as a single item

    def test_depth_less_than_minus_1_wraps_again(self):
        data = [1, 2]
        out = list(iterchain(data, depth=-2))
        # Should yield exactly one element, which itself is a generator
        self.assertEqual(len(out), 1)
        self.assertIsInstance(out[0], types.GeneratorType)
        # Iterating that inner generator should give [data]
        inner = list(out[0])
        self.assertEqual(inner, [data])

    def test_supports_index_custom_type(self):
        class DepthLike:
            def __index__(self):
                return 1  # act like depth=1

        data = [[10], [20, 30]]
        self.assertEqual(list(iterchain(data, depth=DepthLike())), [10, 20, 30])

    def test_generator_input_with_depth_0(self):
        def gen():
            for i in range(3):
                yield i

        self.assertEqual(list(iterchain(gen(), depth=0)), [0, 1, 2])

    def test_strings(self):
        # depth=0 iterates the string
        self.assertEqual(list(iterchain("ab", depth=0)), ["a", "b"])
        # depth=-1 treats the whole string as a single element
        self.assertEqual(list(iterchain("ab", depth=-1)), ["ab"])
        # depth=1 over a list of strings flattens one level into characters
        self.assertEqual(list(iterchain(["ab", "c"], depth=1)), ["a", "b", "c"])

    def test_type_error_when_nested_item_not_iterable_for_positive_depth(self):
        # For depth=1, inner items must be iterable; ints are not, so this should raise
        with self.assertRaises(TypeError):
            list(iterchain([1, 2], depth=1))

    def test_empty_input(self):
        self.assertEqual(list(iterchain([], depth=0)), [])
        self.assertEqual(list(iterchain([], depth=1)), [])
        self.assertEqual(list(iterchain([], depth=2)), [])

    def test_large_depth_exact(self):
        # Perfectly nested 3 levels
        data = [[[[1], [2]], [[3]]]]
        self.assertEqual(list(iterchain(data, depth=3)), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
