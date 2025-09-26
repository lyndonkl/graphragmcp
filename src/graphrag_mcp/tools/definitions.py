"""
Tool definitions for GraphRAG MCP Server.

Defines MCP tools that provide agent-accessible interfaces to GraphRAG knowledge resources.
All tools delegate to existing resource and prompt handlers to maintain consistency.
"""

from typing import Dict, Any, List
import mcp.types as types


def create_tool_definitions() -> List[types.Tool]:
    """Create tool definitions for GraphRAG MCP server."""

    tools = [
        # Generic resource query tool
        types.Tool(
            name="query_graphrag_resource",
            description="Query any GraphRAG knowledge resource by URI. Provides access to all 25 research resources.",
            inputSchema={
                "type": "object",
                "properties": {
                    "resource_uri": {
                        "type": "string",
                        "description": "The URI of the GraphRAG resource to query (e.g., 'graphrag://construction-patterns')",
                        "enum": [
                            "graphrag://overview",
                            "graphrag://construction-patterns",
                            "graphrag://embedding-strategies",
                            "graphrag://retrieval-strategies",
                            "graphrag://architectural-tradeoffs",
                            "graphrag://literature-landscape",
                            "graphrag://technology-stacks",
                            "graphrag://pattern-catalog",
                            "graphrag://patterns/llm-assisted-extraction",
                            "graphrag://patterns/event-reification",
                            "graphrag://patterns/layered-graphs",
                            "graphrag://patterns/provenance-evidence",
                            "graphrag://patterns/temporal-episodic",
                            "graphrag://patterns/hybrid-symbolic-vector",
                            "graphrag://embeddings/node-embeddings",
                            "graphrag://embeddings/edge-relation-embeddings",
                            "graphrag://embeddings/path-metapath-embeddings",
                            "graphrag://embeddings/subgraph-community-embeddings",
                            "graphrag://embeddings/joint-representation-fusion",
                            "graphrag://retrieval/global-first",
                            "graphrag://retrieval/local-first",
                            "graphrag://retrieval/u-shaped-hybrid",
                            "graphrag://retrieval/query-rewriting-decomposition",
                            "graphrag://retrieval/temporal-predictive",
                            "graphrag://retrieval/constraint-guided-filtering"
                        ]
                    }
                },
                "required": ["resource_uri"]
            }
        ),

        # Specific high-value tools
        types.Tool(
            name="get_construction_patterns",
            description="Get the 7 knowledge graph construction patterns for LLM reasoning with detailed descriptions and examples.",
            inputSchema={
                "type": "object",
                "properties": {},
                "additionalProperties": False
            }
        ),

        types.Tool(
            name="get_embedding_strategies",
            description="Get the 5 embedding fusion strategies for combining semantic and structural representations.",
            inputSchema={
                "type": "object",
                "properties": {},
                "additionalProperties": False
            }
        ),

        types.Tool(
            name="get_retrieval_strategies",
            description="Get the 6 retrieval and search strategies for graph+vector hybrid systems.",
            inputSchema={
                "type": "object",
                "properties": {},
                "additionalProperties": False
            }
        ),

        types.Tool(
            name="get_architectural_tradeoffs",
            description="Get analysis of pros and cons of different graph data models (LPG, RDF/OWL, hypergraphs, factor graphs).",
            inputSchema={
                "type": "object",
                "properties": {},
                "additionalProperties": False
            }
        ),

        types.Tool(
            name="get_technology_stacks",
            description="Get comprehensive survey of GraphRAG frameworks, platforms, and technology stacks.",
            inputSchema={
                "type": "object",
                "properties": {},
                "additionalProperties": False
            }
        ),

        # Prompt execution tools
        types.Tool(
            name="analyze_graphrag_pattern",
            description="Analyze which GraphRAG pattern would be best for a specific use case using the specialized analysis prompt.",
            inputSchema={
                "type": "object",
                "properties": {
                    "use_case": {
                        "type": "string",
                        "description": "Description of the use case or domain (e.g., 'healthcare patient records', 'financial compliance')"
                    },
                    "requirements": {
                        "type": "string",
                        "description": "Specific requirements or constraints (optional)",
                        "default": ""
                    },
                    "data_types": {
                        "type": "string",
                        "description": "Types of data involved (optional)",
                        "default": ""
                    }
                },
                "required": ["use_case"]
            }
        ),

        types.Tool(
            name="compare_architectures",
            description="Compare different graph model architectures for a specific use case using the specialized comparison prompt.",
            inputSchema={
                "type": "object",
                "properties": {
                    "use_case": {
                        "type": "string",
                        "description": "Description of the use case or domain"
                    },
                    "scale": {
                        "type": "string",
                        "description": "Expected scale (e.g., '1M entities', 'enterprise-scale')",
                        "default": ""
                    },
                    "performance_requirements": {
                        "type": "string",
                        "description": "Performance requirements (e.g., 'real-time', 'batch processing')",
                        "default": ""
                    }
                },
                "required": ["use_case"]
            }
        ),

        types.Tool(
            name="design_knowledge_graph",
            description="Get guidance on designing a knowledge graph structure for LLM integration using the specialized design prompt.",
            inputSchema={
                "type": "object",
                "properties": {
                    "domain": {
                        "type": "string",
                        "description": "Domain or industry (e.g., 'healthcare', 'finance', 'e-commerce')"
                    },
                    "data_sources": {
                        "type": "string",
                        "description": "Types of data sources (optional)",
                        "default": ""
                    },
                    "integration_requirements": {
                        "type": "string",
                        "description": "LLM integration requirements (optional)",
                        "default": ""
                    }
                },
                "required": ["domain"]
            }
        ),

        types.Tool(
            name="implement_retrieval_strategy",
            description="Get implementation guidance for a specific GraphRAG retrieval strategy using the specialized implementation prompt.",
            inputSchema={
                "type": "object",
                "properties": {
                    "strategy": {
                        "type": "string",
                        "description": "The retrieval strategy to implement",
                        "enum": [
                            "global-first",
                            "local-first",
                            "u-shaped-hybrid",
                            "query-rewriting-decomposition",
                            "temporal-predictive",
                            "constraint-guided-filtering"
                        ]
                    },
                    "technology_stack": {
                        "type": "string",
                        "description": "Preferred technology stack (optional)",
                        "default": ""
                    },
                    "use_case": {
                        "type": "string",
                        "description": "Specific use case context (optional)",
                        "default": ""
                    }
                },
                "required": ["strategy"]
            }
        )
    ]

    return tools


# Export the tools list
GRAPHRAG_TOOLS = create_tool_definitions()