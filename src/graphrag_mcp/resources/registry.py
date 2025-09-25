"""
Resource registry for managing GraphRAG resources.
"""

import logging
from typing import Dict, List, Optional, Callable, Awaitable
import mcp.types as types

from ..utils.exceptions import ResourceNotFoundError, ContentGenerationError


class ResourceRegistry:
    """Registry for managing GraphRAG resources and their content generators."""

    def __init__(self, logger: Optional[logging.Logger] = None):
        self.logger = logger or logging.getLogger(__name__)
        self._resources: Dict[str, types.Resource] = {}
        self._content_generators: Dict[str, Callable[[], Awaitable[str]]] = {}

    def register_resource(
        self,
        resource: types.Resource,
        content_generator: Callable[[], Awaitable[str]]
    ) -> None:
        """Register a resource with its content generator."""
        self.logger.debug(f"Registering resource: {resource.uri}")
        self._resources[resource.uri] = resource
        self._content_generators[resource.uri] = content_generator

    def get_resources(self) -> List[types.Resource]:
        """Get all registered resources."""
        return list(self._resources.values())

    def get_resource(self, uri: str) -> types.Resource:
        """Get a specific resource by URI."""
        if uri not in self._resources:
            raise ResourceNotFoundError(uri)
        return self._resources[uri]

    async def get_content(self, uri: str) -> str:
        """Generate content for a specific resource."""
        if uri not in self._content_generators:
            raise ResourceNotFoundError(uri)

        try:
            self.logger.debug(f"Generating content for: {uri}")
            content = await self._content_generators[uri]()
            self.logger.debug(f"Generated {len(content)} characters for: {uri}")
            return content
        except Exception as e:
            self.logger.error(f"Failed to generate content for {uri}: {e}")
            raise ContentGenerationError(uri, str(e))

    def has_resource(self, uri: str) -> bool:
        """Check if a resource exists."""
        return uri in self._resources