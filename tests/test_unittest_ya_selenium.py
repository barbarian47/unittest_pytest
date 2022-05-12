import unittest
from ya_selenium import ya_authorization
from auth_data import ya_username, ya_password

class TestFunctions(unittest.TestCase):
    def setUp(self) -> None:
        print('setUp --> work')

    def tearDown(self) -> None:
        print('tearDown --> work')

    def test_ya_authorization(self):
        self.assertEqual(ya_authorization(ya_username, ya_password),
                         f'Авторизация для {ya_username} прошла успешно!')
