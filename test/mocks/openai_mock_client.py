from src.llm_client import LLMClient

EXPECTED_RESPONSE = open('test/fixtures/openai-response.md').read()

class OpenAIMockClient(LLMClient):
    def __init__(self):
        super().__init__()
        self.model_loaded = False

    def load_model(self):
        self.model_loaded = True
        self.logger.info("Model loaded successfully.")

    def query(self, prompt: str) -> str:
        if not self.model_loaded:
            raise RuntimeError("OpenAIMockClient: Model not loaded. Call load_model() first.")
        self.logger.info(f"API call for '{prompt}'")
        return EXPECTED_RESPONSE
