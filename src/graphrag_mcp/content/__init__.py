"""
Content generators for GraphRAG MCP Server.
"""

from .overview import get_overview_content
from .construction_patterns import (
    get_construction_patterns_content,
    get_construction_pattern_detail
)
from .embedding_strategies import (
    get_embedding_strategies_content,
    get_embedding_strategy_detail
)
from .retrieval_strategies import (
    get_retrieval_strategies_content,
    get_retrieval_strategy_detail
)
from .architectural_tradeoffs import get_architectural_tradeoffs_content
from .literature_landscape import get_literature_landscape_content
from .technology_stacks import get_technology_stacks_content
from .pattern_catalog import get_pattern_catalog_content

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