import unittest
from app.main import create_app
from app.database import initialize
class SmokeTest(unittest.TestCase):
    def setUp(self):
        initialize()
        self.client=create_app().test_client()
    def test_home(self):
        r=self.client.get('/')
        self.assertEqual(r.status_code,200)
    def test_login(self):
        r=self.client.post('/auth/login',json={'username':'alice','password':'welcome1'})
        self.assertEqual(r.status_code,200)
if __name__=='__main__': unittest.main()
