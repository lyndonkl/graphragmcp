"""
Content generators for GraphRAG MCP Server.
"""

from .loader import (
    get_overview_content,
    get_construction_patterns_content,
    get_construction_pattern_detail,
    get_embedding_strategies_content,
    get_embedding_strategy_detail,
    get_retrieval_strategies_content,
    get_retrieval_strategy_detail,
    get_architectural_tradeoffs_content,
    get_literature_landscape_content,
    get_technology_stacks_content,
    get_pattern_catalog_content,
)

__all__ = [
    "get_overview_content",
    "get_construction_patterns_content",
    "get_construction_pattern_detail",
    "get_embedding_strategies_content",
    "get_embedding_strategy_detail",
    "get_retrieval_strategies_content",
    "get_retrieval_strategy_detail",
    "get_architectural_tradeoffs_content",
    "get_literature_landscape_content",
    "get_technology_stacks_content",
    "get_pattern_catalog_content",
]