"""
Content loader that extracts content from the original comprehensive implementation.
"""

import sys
import os
from typing import Callable, Awaitable

# Add the path to import from the original server
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    # Import all the content functions from the original server
    import sys
    import os
    # Add the parent directory to find server.py
    server_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "server.py")
    if os.path.exists(server_path):
        import importlib.util
        spec = importlib.util.spec_from_file_location("server", server_path)
        server_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(server_module)

        # Import all the content functions from the loaded module
        _get_overview_content = server_module._get_overview_content
        _get_construction_patterns_content = server_module._get_construction_patterns_content
        _get_embedding_strategies_content = server_module._get_embedding_strategies_content
        _get_retrieval_strategies_content = server_module._get_retrieval_strategies_content
        _get_architectural_tradeoffs_content = server_module._get_architectural_tradeoffs_content
        _get_literature_landscape_content = server_module._get_literature_landscape_content
        _get_technology_stacks_content = server_module._get_technology_stacks_content
        _get_pattern_catalog_content = server_module._get_pattern_catalog_content
        _get_construction_pattern_detail = server_module._get_construction_pattern_detail
        _get_embedding_strategy_detail = server_module._get_embedding_strategy_detail
        _get_retrieval_strategy_detail = server_module._get_retrieval_strategy_detail
    else:
        raise ImportError("Could not find server.py file")

    # Export all content functions
    get_overview_content = _get_overview_content
    get_construction_patterns_content = _get_construction_patterns_content
    get_embedding_strategies_content = _get_embedding_strategies_content
    get_retrieval_strategies_content = _get_retrieval_strategies_content
    get_architectural_tradeoffs_content = _get_architectural_tradeoffs_content
    get_literature_landscape_content = _get_literature_landscape_content
    get_technology_stacks_content = _get_technology_stacks_content
    get_pattern_catalog_content = _get_pattern_catalog_content
    get_construction_pattern_detail = _get_construction_pattern_detail
    get_embedding_strategy_detail = _get_embedding_strategy_detail
    get_retrieval_strategy_detail = _get_retrieval_strategy_detail

except ImportError as e:
    # Fallback if import fails
    print(f"Warning: Could not import from original server.py: {e}")

    # Provide minimal fallback implementations
    async def get_overview_content() -> str:
        return "# GraphRAG Overview\n\nContent loading failed. Please check the original server.py file."

    async def get_construction_patterns_content() -> str:
        return "# Construction Patterns\n\nContent loading failed. Please check the original server.py file."

    async def get_embedding_strategies_content() -> str:
        return "# Embedding Strategies\n\nContent loading failed. Please check the original server.py file."

    async def get_retrieval_strategies_content() -> str:
        return "# Retrieval Strategies\n\nContent loading failed. Please check the original server.py file."

    async def get_architectural_tradeoffs_content() -> str:
        return "# Architectural Trade-offs\n\nContent loading failed. Please check the original server.py file."

    async def get_literature_landscape_content() -> str:
        return "# Literature Landscape\n\nContent loading failed. Please check the original server.py file."

    async def get_technology_stacks_content() -> str:
        return "# Technology Stacks\n\nContent loading failed. Please check the original server.py file."

    async def get_pattern_catalog_content() -> str:
        return "# Pattern Catalog\n\nContent loading failed. Please check the original server.py file."

    async def get_construction_pattern_detail(uri: str) -> str:
        return f"# Pattern Detail\n\nContent loading failed for {uri}. Please check the original server.py file."

    async def get_embedding_strategy_detail(uri: str) -> str:
        return f"# Embedding Strategy Detail\n\nContent loading failed for {uri}. Please check the original server.py file."

    async def get_retrieval_strategy_detail(uri: str) -> str:
        return f"# Retrieval Strategy Detail\n\nContent loading failed for {uri}. Please check the original server.py file."