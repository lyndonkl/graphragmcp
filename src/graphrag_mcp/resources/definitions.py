"""
Resource definitions for the GraphRAG MCP Server.
"""

import mcp.types as types
from typing import List


def get_graphrag_resources() -> List[types.Resource]:
    """Get all GraphRAG knowledge resources in hierarchical structure."""
    return [
        # Level 1: Overview and Abstract
        types.Resource(
            uri="graphrag://overview",
            name="GraphRAG Overview",
            description="Comprehensive overview of Knowledge Graph Construction & Retrieval Strategies for LLM Reasoning",
            mimeType="text/markdown",
        ),

        # Level 2: Main Knowledge Areas (7 key tracks)
        types.Resource(
            uri="graphrag://construction-patterns",
            name="Knowledge Graph Construction Patterns",
            description="Seven key patterns for building knowledge graphs that enable effective reasoning and retrieval with LLMs",
            mimeType="text/markdown",
        ),
        types.Resource(
            uri="graphrag://embedding-strategies",
            name="Embedding Fusion Strategies",
            description="Methods for combining LLM-derived semantic embeddings with graph structural embeddings",
            mimeType="text/markdown",
        ),
        types.Resource(
            uri="graphrag://retrieval-strategies",
            name="Retrieval & Search Strategies",
            description="Six comprehensive strategies for retrieval orchestration leveraging both graph traversal and vector search",
            mimeType="text/markdown",
        ),
        types.Resource(
            uri="graphrag://architectural-tradeoffs",
            name="Architectural Trade-offs in Graph Models",
            description="Analysis of pros and cons of different graph data models (LPG, RDF/OWL, hypergraphs, factor graphs)",
            mimeType="text/markdown",
        ),
        types.Resource(
            uri="graphrag://literature-landscape",
            name="External Literature & Industry Landscape",
            description="Recent research and current industry practice on graph-enhanced retrieval-augmented LLMs (2022-present)",
            mimeType="text/markdown",
        ),
        types.Resource(
            uri="graphrag://technology-stacks",
            name="Frameworks & Technology Stacks",
            description="Survey of notable frameworks, platforms, and stacks enabling hybrid graph + vector retrieval for LLMs",
            mimeType="text/markdown",
        ),
        types.Resource(
            uri="graphrag://pattern-catalog",
            name="Pattern Catalog",
            description="Consolidated design pattern handbook for LLM-centric graph-augmented retrieval",
            mimeType="text/markdown",
        ),

        # Level 3: Detailed Sub-patterns and Specific Techniques
        # Construction Patterns Sub-resources
        types.Resource(
            uri="graphrag://patterns/llm-assisted-extraction",
            name="LLM-Assisted Entity & Relation Graphs",
            description="Pattern for LLM-driven extraction of entities/relations aligned to ontologies",
            mimeType="text/markdown",
        ),
        types.Resource(
            uri="graphrag://patterns/event-reification",
            name="Event Reification (N-ary Relations as Nodes)",
            description="Pattern for modeling complex n-ary events or relations as first-class nodes",
            mimeType="text/markdown",
        ),
        types.Resource(
            uri="graphrag://patterns/layered-graphs",
            name="Layered Graphs (Multi-Tier Knowledge Integration)",
            description="Pattern for constructing graphs in layers that separate different data sources or abstraction levels",
            mimeType="text/markdown",
        ),
        types.Resource(
            uri="graphrag://patterns/provenance-evidence",
            name="Provenance & Evidence Layering",
            description="Pattern for augmenting graph nodes/edges with provenance metadata and evidence nodes",
            mimeType="text/markdown",
        ),
        types.Resource(
            uri="graphrag://patterns/temporal-episodic",
            name="Temporal & Episodic Graphs",
            description="Pattern for capturing temporal sequences and state changes as graph structures",
            mimeType="text/markdown",
        ),
        types.Resource(
            uri="graphrag://patterns/hybrid-symbolic-vector",
            name="Hybrid Symbolic-Vector Graphs",
            description="Pattern for integrating neural embedding representations directly into graph structure",
            mimeType="text/markdown",
        ),

        # Embedding Strategies Sub-resources
        types.Resource(
            uri="graphrag://embeddings/node-embeddings",
            name="Node Embeddings: Semantic + Structural",
            description="Strategy for augmenting each graph node with embeddings capturing both semantic content and structural context",
            mimeType="text/markdown",
        ),
        types.Resource(
            uri="graphrag://embeddings/edge-relation-embeddings",
            name="Edge and Relation Embeddings",
            description="Strategy for representing edges with embeddings incorporating relationship semantics and context",
            mimeType="text/markdown",
        ),
        types.Resource(
            uri="graphrag://embeddings/path-metapath-embeddings",
            name="Path and Metapath Embeddings",
            description="Strategy for representing sequences of connected nodes and edges as embeddings",
            mimeType="text/markdown",
        ),
        types.Resource(
            uri="graphrag://embeddings/subgraph-community-embeddings",
            name="Subgraph or Community Embeddings",
            description="Strategy for computing embeddings for entire subgraphs or clusters of nodes",
            mimeType="text/markdown",
        ),
        types.Resource(
            uri="graphrag://embeddings/joint-representation-fusion",
            name="Joint Representation & Fusion Techniques",
            description="Strategy for combining or aligning multiple embedding types into joint space",
            mimeType="text/markdown",
        ),

        # Retrieval Strategies Sub-resources
        types.Resource(
            uri="graphrag://retrieval/global-first",
            name="Global-First Retrieval (Top-Down Overview)",
            description="Strategy starting by retrieving global summary or high-level nodes, then drilling down",
            mimeType="text/markdown",
        ),
        types.Resource(
            uri="graphrag://retrieval/local-first",
            name="Local-First Retrieval (Bottom-Up Expansion)",
            description="Strategy beginning at specific seed entities and exploring outward to gather information",
            mimeType="text/markdown",
        ),
        types.Resource(
            uri="graphrag://retrieval/u-shaped-hybrid",
            name="Hybrid or U-shaped Retrieval",
            description="Strategy combining global and local approaches in two-stage coarse-to-fine bidirectional process",
            mimeType="text/markdown",
        ),
        types.Resource(
            uri="graphrag://retrieval/query-rewriting-decomposition",
            name="Query Rewriting & Decomposition for Multi-hop",
            description="Strategy using LLM to rewrite or break queries into sub-queries for multi-hop retrieval",
            mimeType="text/markdown",
        ),
        types.Resource(
            uri="graphrag://retrieval/temporal-predictive",
            name="Temporal and Predictive Retrieval",
            description="Strategy incorporating time-based searching for sequence, future events, or historical state queries",
            mimeType="text/markdown",
        ),
        types.Resource(
            uri="graphrag://retrieval/constraint-guided-filtering",
            name="Constraint-Guided and Hybrid Symbolic-Neural Filtering",
            description="Strategy applying symbolic constraints to narrow search, then using neural ranking on filtered set",
            mimeType="text/markdown",
        ),
    ]


# Export the resources
GRAPHRAG_RESOURCES = get_graphrag_resources()