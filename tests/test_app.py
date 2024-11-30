import unittest
from app.app import app

class TestApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Se ejecuta antes de todas las pruebas"""
        cls.client = app.test_client()
        cls.base_url = "/"

    def test_home_endpoint(self):
        """Prueba que el endpoint '/' devuelva el mensaje correcto"""
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "¡Hola desde Flask!"})

    def test_nonexistent_endpoint(self):
        """Prueba que un endpoint inexistente devuelva un error 404"""
        response = self.client.get("/nonexistent")
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()
