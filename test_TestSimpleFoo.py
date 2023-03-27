from unittest import TestCase, main as unittest_main


class TestSimpleFoo(TestCase):
    foo = 'bar'

    def setUp(self):
        pass

    def test_a(self):
        self.assertEqual(self.__class__.foo, 'bar')
        self.__class__.foo = 'can'

    def test_f(self):
        self.assertEqual(self.__class__.foo, 'can')


if __name__ == '__main__':
    unittest_main()

    # https://stackoverflow.com/questions/21447740/persist-variable-changes-between-tests-in-unittest