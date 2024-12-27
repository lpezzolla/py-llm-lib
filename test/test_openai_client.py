import re
import pytest
from unittest.mock import patch
from test.mocks.openai_mock_client import OpenAIMockClient

EXPECTED_RESPONSE = open('test/fixtures/openai-response.md').read()

def test_load_model():
    """Test that the model loads successfully"""
    client = OpenAIMockClient()
    client.load_model()
    assert client.model_loaded is True, "Model should be loaded."

def test_query_with_loaded_model():
    """Test querying the model after it is loaded"""
    client = OpenAIMockClient()
    client.load_model()
    prompt = "What is the meaning of life?"
    response = client.query(prompt)
    assert response == EXPECTED_RESPONSE, "Response should match the expected mock output."

def test_query_without_loading_model():
    """Test querying the model before loading it, expecting an error"""
    client = OpenAIMockClient()
    with pytest.raises(RuntimeError, match=re.escape("Model not loaded. Call load_model() first.")):
        client.query("What is the meaning of life?")

def test_handle_error():
    """Test the error handling mechanism."""
    client = OpenAIMockClient()
    with patch("logging.Logger.error") as mock_logger_error:
        error_message = "This is a test error."
        try:
            raise ValueError(error_message)
        except Exception as e:
            client.handle_error(e)

        mock_logger_error.assert_called_once_with(f"OpenAIMockClient error occurred: {error_message}")