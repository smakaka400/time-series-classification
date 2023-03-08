import unittest
from model_deployment import app

class TestPredictions(unittest.TestCase):
    """
    Test class inheriting from unittest.TestCase.
    Each method (apart from setUp) is a test case for each of the testing files.
    Methods:
        setUp(self): method to instantiate the Flask API in testing mode.
        test_valid_data(self): a test that provides a CSV of correct format to the API.
        test_invalid_data_size(self): a test that provides a CSV with too few columns to the API.
        test_invalid_data_type(self): a test that provides a non-CSV file to the API.
    """
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True
        
    def test_valid_data(self):
        with open('test_predictions_correct.csv', 'rb') as f:
            response = self.client.post('/predict', content_type='multipart/form-data', data={'file': f})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {'predictions': [1, 1, 2, 1, 2]})
        
    def test_invalid_data_size(self):
        with open('test_predictions_incorrect.csv', 'rb') as f:
            response = self.client.post('/predict', content_type='multipart/form-data', data={'file': f})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, "Error in CSV input data. Check file is of correct size and format.")
        
    def test_valid_data_type(self):
        with open('test_predictions_incorrect.txt', 'rb') as f:
            response = self.client.post('/predict', content_type='multipart/form-data', data={'file': f})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, "Error in input data. Check file is an input CSV of correct size and format.")
        
if __name__ == '__main__':
    unittest.main()