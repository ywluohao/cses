def c(y, x):
    if (y >= x and y % 2 == 1) or (y < x and x % 2 == 1):
        x, y = y, x
    if y >= x:
        return y ** 2 - x + 1
    else:
        return (x - 1) ** 2 + y


import unittest


class TestC(unittest.TestCase):
    def test_c(self):
        self.assertEqual(c(2, 3), 8)
        self.assertEqual(c(1, 1), 1)
        self.assertEqual(c(4, 2), 15)

        # y > x
        self.assertEqual(c(5, 3), 19)
        self.assertEqual(c(5, 4), 20)
        self.assertEqual(c(4, 6), 29)
        self.assertEqual(c(4, 3), 14)

        # x < y
        self.assertEqual(c(3, 5), 23)
        self.assertEqual(c(4, 5), 22)
        self.assertEqual(c(6, 4), 33)
        self.assertEqual(c(3, 4), 12)

        # real case
        self.assertEqual(c(1000000000, 1000000000), 999999999000000001)
        self.assertEqual(c(170550340, 943050741), 889344699930098742)


if __name__ == "__main__":
    unittest.main()
