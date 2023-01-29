import unittest

from backend_layer.facade import Facade


class MyTestCase(unittest.TestCase):

    def test_signup_existing(self):
        f = Facade.get_instance()
        f.signup_request("nour walid1", "password", True)
        check, response = f.signup_request("nour walid1", "password", True)
        self.assertFalse(check)
        self.assertEqual(response,"Name already exists!")
        f.reset_instance()

    def test_signup_invalid_password(self):
        f = Facade.get_instance()
        check, response = f.signup_request("ali walid", "pass", True)
        self.assertFalse(check)
        self.assertEqual(response, "Invalid password!")
        f.reset_instance()

    def test_signup(self):
        f = Facade.get_instance()
        check, response = f.signup_request("malk walid", "password", True)
        self.assertTrue(check)
        self.assertIsNotNone(response)
        self.assertEqual(response.get_name(),'malk walid')
        self.assertTrue(response.get_gender())
        f.reset_instance()

    def test_signin_not_existing(self):
        f = Facade.get_instance()
        check, response = f.signin_request('not existing player','123456789')
        self.assertFalse(check)
        self.assertEqual(response,'Player doesn\'t exist!')
        f.reset_instance()

    def test_signin(self):
        f = Facade.get_instance()
        f.signup_request("nour walid2", "password", True)
        check, response = f.signin_request('nour walid2', 'password')
        self.assertTrue(check)
        self.assertEqual(response.get_name(),'nour walid2')
        f.reset_instance()

    def test_change_name_invalid(self):
        f = Facade.get_instance()
        f.signup_request("new player2", "password", True)
        check, response = f.signup_request("new player", "password", True)
        print(f.player.get_name())
        test = f.save_name('new player2')
        print(test)
        self.assertFalse(test)
        self.assertEqual(response.get_name(), 'new player')
        f.reset_instance()


if __name__ == '__main__':
    unittest.main()
