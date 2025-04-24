import unittest
from unittest.mock import patch, Mock
from assistant import CustomerSupportAssistant  # assuming your main file is named assistant.py

class TestCustomerSupportAssistant(unittest.TestCase):

    def setUp(self):
        self.assistant = CustomerSupportAssistant(api_key="fake-api-key")

    @patch("assistant.requests.post")
    def test_successful_response(self, mock_post):
        # Mocked API response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "choices": [
                {
                    "message": {
                        "content": "I'm sorry to hear your order is delayed. There could be several reasons..."
                    }
                }
            ]
        }
        mock_post.return_value = mock_response

        result = self.assistant.ask_question("Why is my order delayed?")
        self.assertIn("I'm sorry to hear your order is delayed", result)

    @patch("assistant.requests.post")
    def test_failed_api_request(self, mock_post):
        # Simulate a RequestException
        import requests
        mock_post.side_effect = requests.exceptions.RequestException("Network error")


        result = self.assistant.ask_question("Why is my order delayed?")
        self.assertEqual(result, "Sorry, I couldn't reach the support system right now. Please try again later.")

    def test_empty_api_key(self):
        assistant_with_no_key = CustomerSupportAssistant(api_key=None)
        self.assertIsNone(assistant_with_no_key.api_key)

if __name__ == '__main__':
    unittest.main()
