from django.test import TestCase, Client

class APITests(TestCase):
    def test_listar_produtos_retorna_200(self):
        client = Client()
        response = client.get('/api/produtos/')
        self.assertEqual(response.status_code, 200)