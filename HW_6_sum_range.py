import unittest
import random


def generate_random_array(amount, left, right):
    return [random.randrange(left, right) for _ in range(amount)]

# print(generate_random_array(30, 5, 15))


class Solution:
    def sum_range(this, array):
        return sum([number for number in array if number in range(10, 101)])

    @staticmethod
    def sum_range_static(array, range):
        return sum([element for element in array if element in range])


class SolutionTest(unittest.TestCase):
    def test_sum_range_static(self):  # NOTE метод для тестирования работы функции sum_range_static
        result = Solution.sum_range_static(ints, range(-100, 0))
        self.assertEqual(-118, result)

    def test_sum_range(self):
        s = Solution()
        result = s.sum_range(ints)  # sum should be in range from 10 to 100 inclusive
        self.assertEqual(222, result)


if __name__ == '__main__':
    unittest.main()

# NOTE проверка работы привычными средствами
ints = [14, 57, 63, -38, 47, -80, -186, 41, 142, 193]
s = Solution()
answer = s.sum_range(ints)
print(answer)

print(Solution.sum_range_static(ints, range(-100, 0)))


random_array = generate_random_array(100, -100, 200)
print(s.sum_range(random_array))

print(Solution.sum_range_static(random_array, range(-100, 0)))

