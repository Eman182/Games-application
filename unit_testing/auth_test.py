import unittest

from backend_layer.auth_proxy.sign_in import SignIn
from backend_layer.auth_proxy.sign_up import SignUp


class MyTestCase(unittest.TestCase):
    def test_sign_up(self):
        s = SignUp()
        s.sign_up("Admin2", "12345678", False)
        self.assertEqual(s.sign_up("new", "123", False), (False, "Invalid password!"))
        self.assertEqual(s.sign_up("Admin2", "12345678", False), (False, "Name already exists!"))
        check, player=s.sign_up("name1", "pass12345", False)
        self.assertEqual(player.get_name(), "name1")
        self.assertTrue(check)

    def test_sign_in(self):
        s = SignIn()
        self.assertEqual(s.sign_in("new", "123"), (False, "Player doesn't exist!"))
        s2 = SignUp()
        s2.sign_up("Admin3", "12345678", False)
        self.assertEqual(s.sign_in("Admin3", "123456"), (False, "Wrong password!"))
        check,player=s.sign_in("Admin3", "12345678")
        self.assertTrue(check)
        self.assertEqual(player.get_name(), "Admin3")

if __name__ == '__main__':
    unittest.main()
