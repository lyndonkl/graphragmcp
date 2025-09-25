"""
Content factory for generating GraphRAG knowledge content.

This module provides a centralized way to generate all content for the GraphRAG MCP server
without duplicating the massive content strings.
"""

from typing import Dict, Callable, Awaitable
import logging

from ..utils.exceptions import ResourceNotFoundError


class ContentFactory:
    """Factory for generating content for GraphRAG resources."""

    def __init__(self, logger: logging.Logger):
        self.logger = logger
        self._generators: Dict[str, Callable[[], Awaitable[str]]] = {}
        self._setup_generators()

    def _setup_generators(self) -> None:
        """Set up all content generators."""
        from .overview import get_overview_content
        from .patterns import (
            get_construction_patterns_content,
            get_embedding_strategies_content,
            get_retrieval_strategies_content,
            get_pattern_catalog_content
        )
        from .analysis import (
            get_architectural_tradeoffs_content,
            get_literature_landscape_content,
            get_technology_stacks_content
        )
        from .details import (
            get_construction_pattern_detail,
            get_embedding_strategy_detail,
            get_retrieval_strategy_detail
        )

        # Main content generators
        self._generators.update({
            "graphrag://overview": get_overview_content,
            "graphrag://construction-patterns": get_construction_patterns_content,
            "graphrag://embedding-strategies": get_embedding_strategies_content,
            "graphrag://retrieval-strategies": get_retrieval_strategies_content,
            "graphrag://architectural-tradeoffs": get_architectural_tradeoffs_content,
            "graphrag://literature-landscape": get_literature_landscape_content,
            "graphrag://technology-stacks": get_technology_stacks_content,
            "graphrag://pattern-catalog": get_pattern_catalog_content,
        })

        # Detail generators
        pattern_details = [
            "llm-assisted-extraction", "event-reification", "layered-graphs",
            "provenance-evidence", "temporal-episodic", "hybrid-symbolic-vector"
        ]
        for pattern in pattern_details:
            uri = f"graphrag://patterns/{pattern}"
            self._generators[uri] = self._create_pattern_detail_generator(uri)

        embedding_details = [
            "node-embeddings", "edge-relation-embeddings", "path-metapath-embeddings",
            "subgraph-community-embeddings", "joint-representation-fusion"
        ]
        for embedding in embedding_details:
            uri = f"graphrag://embeddings/{embedding}"
            self._generators[uri] = self._create_embedding_detail_generator(uri)

        retrieval_details = [
            "global-first", "local-first", "u-shaped-hybrid",
            "query-rewriting-decomposition", "temporal-predictive", "constraint-guided-filtering"
        ]
        for retrieval in retrieval_details:
            uri = f"graphrag://retrieval/{retrieval}"
            self._generators[uri] = self._create_retrieval_detail_generator(uri)

    def _create_pattern_detail_generator(self, uri: str) -> Callable[[], Awaitable[str]]:
        """Create a pattern detail generator for a specific URI."""
        async def generator() -> str:
            return await get_construction_pattern_detail(uri)
        return generator

    def _create_embedding_detail_generator(self, uri: str) -> Callable[[], Awaitable[str]]:
        """Create an embedding detail generator for a specific URI."""
        async def generator() -> str:
            return await get_embedding_strategy_detail(uri)
        return generator

    def _create_retrieval_detail_generator(self, uri: str) -> Callable[[], Awaitable[str]]:
        """Create a retrieval detail generator for a specific URI."""
        async def generator() -> str:
            return await get_retrieval_strategy_detail(uri)
        return generator

    async def generate_content(self, uri: str) -> str:
        """Generate content for a specific resource URI."""
        if uri not in self._generators:
            self.logger.error(f"No content generator found for: {uri}")
            raise ResourceNotFoundError(uri)

        try:
            self.logger.debug(f"Generating content for: {uri}")
            content = await self._generators[uri]()
            self.logger.info(f"Generated {len(content)} characters for: {uri}")
            return content
        except Exception as e:
            self.logger.error(f"Failed to generate content for {uri}: {e}")
            raise

    def has_generator(self, uri: str) -> bool:
        """Check if a content generator exists for the given URI."""
        return uri in self._generators

    def get_available_uris(self) -> list[str]:
        """Get all available content URIs."""
        return list(self._generators.keys())