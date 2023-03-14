import unittest
import requests


class UnixTimestampConverterTests(unittest.TestCase):
    def setUp(self):
        self.url = 'https://helloacm.com/api/unix-timestamp-converter/'

    def test_valid_input(self):
        payload = {'s': '2016-01-01 2:3:22', 'cached': ''}
        response = requests.get(self.url, params=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/json')
        self.assertEqual(response.text.strip(), '1451613802')

    def test_invalid_input(self):
        payload = {'s': 'not_a_valid_timestamp', 'cached': ''}
        response = requests.get(self.url, params=payload)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers['Content-Type'], 'application/json')

    def test_correct_output(self):
        payload = {'s': '2016-01-01 2:3:22', 'cached': ''}
        response = requests.get(self.url, params=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/json')
        self.assertEqual(response.text.strip(), '1451613802')

    def test_error_message(self):
        payload = {'s': 'not_a_valid_timestamp', 'cached': ''}
        response = requests.get(self.url, params=payload)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers['Content-Type'], 'application/json')

    def test_response_time(self):
        payload = {'s': '2016-01-01 2:3:22', 'cached': ''}
        response = requests.get(self.url, params=payload)
        self.assertEqual(response.status_code, 200)
        self.assertLess(response.elapsed.total_seconds(), 1)


if __name__ == '__main__':
    unittest.main()
