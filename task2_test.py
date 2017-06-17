import unittest
from task2 import Wizard


class TestTask2(unittest.TestCase):

    def test_case1(self):
        spell = "feeai"
        janusz = Wizard()
        result = janusz.damage(spell)
        expected_result = 2
        self.assertEquals(result, expected_result)

    def test_case2(self):
        spell = "feaineain"
        janusz = Wizard()
        result = janusz.damage(spell)
        expected_result = 7
        self.assertEquals(result, expected_result)

    def test_case3(self):
        spell = "jee"
        janusz = Wizard()
        result = janusz.damage(spell)
        expected_result = 0
        self.assertEquals(result, expected_result)

    def test_case4(self):
        spell = "fefefefefeaiaiaiaiai"
        janusz = Wizard()
        result = janusz.damage(spell)
        expected_result = 0
        self.assertEquals(result, expected_result)

    def test_case5(self):
        spell = "fdafafeajain"
        janusz = Wizard()
        result = janusz.damage(spell)
        expected_result = 1
        self.assertEquals(result, expected_result)

    def test_case6(self):
        spell = "fexxxxxxxxxxai"
        janusz = Wizard()
        result = janusz.damage(spell)
        expected_result = 0
        self.assertEquals(result, expected_result)

if __name__ == '__main__':
    unittest.main()
