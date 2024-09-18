import unittest
from app import app
import warnings

class TestAuroraBriefo(unittest.TestCase):

    def setUp(self):
        # Set up a test client
        self.app = app.test_client()
        self.app.testing = True

        # Suppress FutureWarnings from Hugging Face Transformers
        warnings.filterwarnings("ignore", category=FutureWarning)

    def calculate_max_length(self, document_length):
        # Dynamic max_length based on the input document length (half of the input length)
        return max(10, int(0.5 * document_length))

    def test_home_page(self):
        # Test the home page route
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'AuroraBriefo', result.data)  # Check if AuroraBriefo is in the home page

    def test_summarize_short_length(self):
        # Test the summarization route with 'short' summary length
        document = 'Artificial intelligence is the simulation of human intelligence in machines.'
        max_len = self.calculate_max_length(len(document.split()))

        response = self.app.post('/summarize', data={
            'document': document,
            'summary_length': 'short'
        })
        self.assertEqual(response.status_code, 200)
        json_data = response.get_json()
        self.assertIn('summary', json_data)

    def test_summarize_medium_length(self):
        # Test the summarization route with 'medium' summary length
        document = 'Artificial intelligence is the simulation of human intelligence in machines.'
        max_len = self.calculate_max_length(len(document.split()))

        response = self.app.post('/summarize', data={
            'document': document,
            'summary_length': 'medium'
        })
        self.assertEqual(response.status_code, 200)
        json_data = response.get_json()
        self.assertIn('summary', json_data)

    def test_summarize_detailed_length(self):
        # Test the summarization route with 'detailed' summary length
        document = 'Artificial intelligence is the simulation of human intelligence in machines.'
        max_len = self.calculate_max_length(len(document.split()))

        response = self.app.post('/summarize', data={
            'document': document,
            'summary_length': 'detailed'
        })
        self.assertEqual(response.status_code, 200)
        json_data = response.get_json()
        self.assertIn('summary', json_data)

if __name__ == '__main__':
    unittest.main()
