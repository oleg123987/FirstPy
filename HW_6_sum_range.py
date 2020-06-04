import unittest
import random


# def generate_random_array(amount, left, right):
#     return [random.randrange(left, right) for i in range(amount)]


class Solution:
    def sum_range(this, array):  # TODO доработать этот метод
        return array

    @staticmethod
    def sum_range_static(array, range):  # TODO пример реализации
        return [element for element in array if element in range]


class SolutionTest(unittest.TestCase):
    def test_sum_range_static(self):  # NOTE метод для тестирования работы функции sum_range_static
        result = Solution.sum_range_static(ints, range(-100, 0))
        self.assertEqual(result, [-38, -80])

    def test_sum_range(self):  # TODO доработать метод для тестирования работы функции sum_range
        result = []  # Should be in range from 10 to 100 inclusive
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()

# NOTE проверка работы привычными средствами
ints = [14, 57, 63, -38, 47, -80, -186, 41, 142, 193]
s = Solution()
answer = s.sum_range(ints)
print(answer)

print(Solution.sum_range_static(ints, range(-100, 0)))
