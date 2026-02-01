import unittest
from crud_api import app

class CrudApiTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_get_products(self):
        response = self.client.get('/products')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data, list)
        self.assertGreaterEqual(len(data), 8)

    def test_add_product(self):
        new_product = {"name": "Speaker", "price": 99}
        response = self.client.post('/product', json=new_product)
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data["name"], "Speaker")
        self.assertEqual(data["price"], 99)

    def test_get_product(self):
        response = self.client.get('/product/1')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["id"], 1)

    def test_delete_product(self):
        response = self.client.delete('/product/8')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("result", data)

    def test_get_nonexistent_product(self):
        response = self.client.get('/product/999')
        self.assertEqual(response.status_code, 404)
        data = response.get_json()
        self.assertIn("error", data)

if __name__ == '__main__':
    unittest.main()
