import unittest
import json
from crud_api import app

class CrudApiTestCase(unittest.TestCase):
    results = []
    def setUp(self):
        self.client = app.test_client()

    def save_result(self, name, response):
        CrudApiTestCase.results.append({
            "test": name,
            "status_code": response.status_code,
            "response": response.get_json()
        })

    def test_get_products(self):
        response = self.client.get('/products')
        self.save_result("get_products", response)
        self.assertEqual(response.status_code, 200)

    def test_add_product(self):
        new_product = {"name": "Speaker", "price": 99}
        response = self.client.post('/product', json=new_product)
        self.save_result("add_product", response)
        self.assertEqual(response.status_code, 201)

    def test_get_product(self):
        response = self.client.get('/product/1')
        self.save_result("get_product", response)
        self.assertEqual(response.status_code, 200)

    def test_delete_product(self):
        response = self.client.delete('/product/8')
        self.save_result("delete_product", response)
        self.assertEqual(response.status_code, 200)

    def test_get_nonexistent_product(self):
        response = self.client.get('/product/999')
        self.save_result("get_nonexistent_product", response)
        self.assertEqual(response.status_code, 404)

    @classmethod
    def tearDownClass(cls):
        # Save all results to test_results.json
        with open('test_results.json', 'w') as f:
            json.dump(cls.results, f, indent=2)

if __name__ == '__main__':
    unittest.main()
