import unittest 
import requests

class TestHello(unittest.TestCase):
    def test_hello_route(self):
        response = requests.get("http://localhost:8080/hello")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Hello, DevOps!")

if __name__ == "__main__":
    unittest.main()

