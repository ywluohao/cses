# 1-9       1 * 9
# 10-99     2 * 90
# 100-999   3 * 900
# 1000-9999 4 * 9000

l = [9]
for i in range(17):
    l.append(l[i] + (i + 2) * 9 * 10 ** (i + 1))


def c(n):
    if n <= 9:
        return n
    for i in range(17):
        if n <= l[i]:
            break

    q, r = divmod(n - l[i - 1] + i, i + 1)
    return int(str(10 ** (i) + q - 1)[r])


import unittest


class TestC(unittest.TestCase):
    def test_c(self):
        self.assertEqual(c(7), 7)
        self.assertEqual(c(19), 4)
        self.assertEqual(c(12), 1)
        self.assertEqual(c(187), 8)

        #
        self.assertEqual(c(672274832941907421), 7)


if __name__ == "__main__":
    unittest.main()
