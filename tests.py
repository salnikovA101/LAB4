import unittest
from tabulate import tabulate

def RectangleArea(a, b):
    if a >= 0 and b >= 0:
        return a * b
    else:
        return "Please enter non-negative numbers"

def RectanglePerimeter(a, b):
    if a >= 0 and b >= 0:
        return 2 * (a + b)
    else:
        return "Please enter non-negative numbers"

def SquareArea(a):
    if a >= 0:
        return a * a
    else:
        return "Please enter non-negative number"


def SquarePerimeter(a):
    if a >= 0:
        return 4 * a
    else:
        return "Please enter non-negative number"

def HandshakeTask(a):
    if (a == 0):
        return 0
    elif (a < 0):
        return "Please enter non-negative number"
    else:
        return int(a * (a - 1) / 2)

class TestCase(unittest.TestCase):
    results = []

    def add_result(self, name, inputs, expected, actual):
        self.results.append([name, inputs, expected, actual, "Пройден" if expected == actual else "Ошибка"])

    def test_RectangleArea_1(self):
        inputs = (5, 0)
        expected = 0
        actual = RectangleArea(*inputs)
        self.add_result("RectangleArea_1", inputs, expected, actual)

    def test_RectangleArea_2(self):
        inputs = (-10, 50)
        expected = "Please enter non-negative numbers"
        actual = RectangleArea(*inputs)
        self.add_result("RectangleArea_2", inputs, expected, actual)

    def test_RectangleArea_3(self):
        inputs = (5800000, 125)
        expected = 725000000
        actual = RectangleArea(*inputs)
        self.add_result("RectangleArea_3", inputs, expected, actual)

    def test_RectanglePerimeter_1(self):
        inputs = (0, 10)
        expected = 20
        actual = RectanglePerimeter(*inputs)
        self.add_result("RectanglePerimeter_1", inputs, expected, actual)

    def test_RectanglePerimeter_2(self):
        inputs = (-100, 2000)
        expected = "Please enter non-negative numbers"
        actual = RectanglePerimeter(*inputs)
        self.add_result("RectanglePerimeter_2", inputs, expected, actual)

    def test_RectanglePerimeter_3(self):
        inputs = (1235, 456)
        expected = 3382
        actual = RectanglePerimeter(*inputs)
        self.add_result("RectanglePerimeter_3", inputs, expected, actual)

    def test_SquareArea_1(self):
        inputs = 0
        expected = 0
        actual = SquareArea(inputs)
        self.add_result("SquareArea_1", inputs, expected, actual)

    def test_SquareArea_2(self):
        inputs = -10
        expected = "Please enter non-negative number"
        actual = SquareArea(inputs)
        self.add_result("SquareArea_2", inputs, expected, actual)

    def test_SquareArea_3(self):
        inputs = 123123
        expected = 15159273129
        actual = SquareArea(inputs)
        self.add_result("SquareArea_1", inputs, expected, actual)

    def test_SquarePerimeter_1(self):
        inputs = 0
        expected = 0
        actual = SquarePerimeter(inputs)
        self.add_result("SquarePerimeter_1", inputs, expected, actual)

    def test_SquarePerimeter_2(self):
        inputs = -10
        expected = "Please enter non-negative number"
        actual = SquarePerimeter(inputs)
        self.add_result("SquarePerimeter_2", inputs, expected, actual)

    def test_SquarePerimeter_3(self):
        inputs = 13123
        expected = 52492
        actual = SquarePerimeter(inputs)
        self.add_result("SquarePerimeter_3", inputs, expected, actual)
    
    def test_HandshakeTask_1(self):
        inputs = 1
        expected = 0
        actual = HandshakeTask(inputs)
        self.add_result("HandshakeTask_1", inputs, expected, actual)

    def test_HandshakeTask_2(self):
        inputs = 0
        expected = 0
        actual = HandshakeTask(inputs)
        self.add_result("HandshakeTask_2", inputs, expected, actual)

    def test_HandshakeTask_3(self):
        inputs = -10
        expected = "Please enter non-negative number"
        actual = HandshakeTask(inputs)
        self.add_result("HandshakeTask_3", inputs, expected, actual)

    def test_HandshakeTask_4(self):
        inputs = 150
        expected = 11175
        actual = HandshakeTask(inputs)
        self.add_result("HandshakeTask_4", inputs, expected, actual)

    @classmethod
    def tearDownClass(res):
        print(tabulate(res.results, headers=["Название теста", "Входные данные", "Ожидаемый результат", "Фактический результат", "Статус теста"], tablefmt="grid"))
        if any(result[4] == "Ошибка" for result in res.results):
            print("\nНекоторые тесты не прошли!") 
            exit(1)