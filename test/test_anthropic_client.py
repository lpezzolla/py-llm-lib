import re
import pytest
from unittest.mock import patch

from pydantic_core._pydantic_core import ValidationError

from src.models.query_models import QueryPayload, QueryOutput
from test.mocks.anthropic_mock_client import AnthropicMockClient

EXPECTED_RESPONSE = open('test/fixtures/anthropic-response.md').read()

def test_load_model():
    """Test that the model loads successfully"""
    client = AnthropicMockClient()
    client.load_model()
    assert client.model_loaded is True, "Model should be loaded."

def test_query_with_loaded_model():
    """Test querying the model after it is loaded"""
    client = AnthropicMockClient()
    client.load_model()

    payload = QueryPayload(prompt="What is the meaning of life?", user_id="42")
    output = client.query(payload)

    assert isinstance(output, QueryOutput)
    assert output.response == EXPECTED_RESPONSE, "Response should match the expected mock output."

def test_query_with_loaded_model_but_invalid_payload():
    """Test querying the model after it is loaded, without including the user_id"""
    client = AnthropicMockClient()
    client.load_model()
    with pytest.raises(ValidationError):
        payload = QueryPayload(prompt="What is the meaning of life?")
        client.query(payload)

def test_query_without_loading_model():
    """Test querying the model before loading it, expecting an error"""
    client = AnthropicMockClient()
    payload = QueryPayload(prompt="What is the meaning of life?", user_id="42")
    with pytest.raises(RuntimeError, match=re.escape("Model not loaded. Call load_model() first.")):
        client.query(payload)

def test_handle_error():
    """Test the error handling mechanism"""
    client = AnthropicMockClient()
    with patch("logging.Logger.error") as mock_logger_error:
        error_message = "This is a test error."
        try:
            raise ValueError(error_message)
        except Exception as e:
            client.handle_error(e)

        mock_logger_error.assert_called_once_with(f"AnthropicMockClient error occurred: {error_message}")
