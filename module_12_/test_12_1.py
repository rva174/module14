import unittest
# from Runner import Runner


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class TestRunner(unittest.TestCase):
    def setUp(self):
        self.runner = Runner('name')

    def test_run(self):
        r = Runner("Run")
        for i in range(10):
            r.run()
        self.assertEqual(r.distance, 100)

    def test_walk(self):
        r = Runner("Walk")
        for i in range(10):
            r.walk()
        self.assertEqual(r.distance, 50)

    def test_challenge(self):
        r1 = Runner("Run")
        r2 = Runner('Walk')
        for i in range(10):
            r1.run()
            r2.walk()
        self.assertNotEqual(r1.distance, r2.distance)


if __name__ == '__main__':
    unittest.main()