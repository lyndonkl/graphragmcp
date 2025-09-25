"""
Prompt registry for managing GraphRAG prompts.
"""

import logging
from typing import Dict, List, Optional, Callable, Awaitable
import mcp.types as types

from ..utils.exceptions import PromptNotFoundError


class PromptRegistry:
    """Registry for managing GraphRAG prompts and their generators."""

    def __init__(self, logger: Optional[logging.Logger] = None):
        self.logger = logger or logging.getLogger(__name__)
        self._prompts: Dict[str, types.Prompt] = {}
        self._generators: Dict[str, Callable[[Dict[str, str]], Awaitable[types.GetPromptResult]]] = {}

    def register_prompt(
        self,
        prompt: types.Prompt,
        generator: Callable[[Dict[str, str]], Awaitable[types.GetPromptResult]]
    ) -> None:
        """Register a prompt with its generator."""
        self.logger.debug(f"Registering prompt: {prompt.name}")
        self._prompts[prompt.name] = prompt
        self._generators[prompt.name] = generator

    def get_prompts(self) -> List[types.Prompt]:
        """Get all registered prompts."""
        return list(self._prompts.values())

    def get_prompt(self, name: str) -> types.Prompt:
        """Get a specific prompt by name."""
        if name not in self._prompts:
            raise PromptNotFoundError(name)
        return self._prompts[name]

    async def generate_prompt(self, name: str, arguments: Dict[str, str]) -> types.GetPromptResult:
        """Generate a prompt result for a specific prompt."""
        if name not in self._generators:
            raise PromptNotFoundError(name)

        try:
            self.logger.debug(f"Generating prompt: {name}")
            result = await self._generators[name](arguments)
            self.logger.debug(f"Generated prompt result for: {name}")
            return result
        except Exception as e:
            self.logger.error(f"Failed to generate prompt {name}: {e}")
            raise

    def has_prompt(self, name: str) -> bool:
        """Check if a prompt exists."""
        return name in self._prompts