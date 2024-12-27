from abc import ABC, abstractmethod
from src.utils.logger import get_logger
from typing import Any, Dict

class LLMClient(ABC):
    def __init__(self, config: Dict[str, Any] = None):
        self.config = None
        self.configure(config)
        self.logger = get_logger(self.__class__.__name__)

    @abstractmethod
    def load_model(self):
        """Load the LLM model into memory"""
        pass

    def configure(self, next_config: Dict[str, Any] = None):
        """Replaces the current configuration with the given one"""
        self.config = next_config or {}
        pass

    @abstractmethod
    def query(self, prompt: str) -> str:
        """Interact with the LLM using the given prompt"""
        pass

    def handle_error(self, error: Exception):
        self.logger.error(f"{self.__class__.__name__} error occurred: {str(error)}")