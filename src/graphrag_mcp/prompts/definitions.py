"""
Prompt definitions for the GraphRAG MCP Server.
"""

import mcp.types as types
from typing import List


def get_graphrag_prompts() -> List[types.Prompt]:
    """Get all available GraphRAG prompts for different use cases."""
    return [
        types.Prompt(
            name="analyze-graphrag-pattern",
            description="Analyze which GraphRAG pattern would be best for a specific use case",
            arguments=[
                types.PromptArgument(
                    name="use_case",
                    description="Description of the use case, domain, and requirements",
                    required=True,
                ),
                types.PromptArgument(
                    name="constraints",
                    description="Any technical constraints, data types, or performance requirements",
                    required=False,
                ),
            ],
        ),
        types.Prompt(
            name="design-knowledge-graph",
            description="Get guidance on designing a knowledge graph structure for LLM integration",
            arguments=[
                types.PromptArgument(
                    name="domain",
                    description="Domain or industry (e.g., healthcare, finance, enterprise)",
                    required=True,
                ),
                types.PromptArgument(
                    name="data_sources",
                    description="Types of data sources to integrate",
                    required=True,
                ),
                types.PromptArgument(
                    name="query_types",
                    description="Expected types of queries or questions",
                    required=False,
                ),
            ],
        ),
        types.Prompt(
            name="implement-retrieval-strategy",
            description="Get implementation guidance for a specific GraphRAG retrieval strategy",
            arguments=[
                types.PromptArgument(
                    name="strategy",
                    description="Name of the retrieval strategy to implement",
                    required=True,
                ),
                types.PromptArgument(
                    name="technology_stack",
                    description="Preferred technologies, frameworks, or platforms",
                    required=False,
                ),
            ],
        ),
        types.Prompt(
            name="compare-architectures",
            description="Compare different graph model architectures for a specific use case",
            arguments=[
                types.PromptArgument(
                    name="requirements",
                    description="Specific requirements like scale, performance, standardization needs",
                    required=True,
                ),
            ],
        ),
    ]


# Export the prompts
GRAPHRAG_PROMPTS = get_graphrag_prompts()