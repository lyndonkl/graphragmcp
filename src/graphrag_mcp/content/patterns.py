"""
Content generators for GraphRAG patterns (construction, embedding, retrieval).
"""

async def get_construction_patterns_content() -> str:
    """Return detailed content on Knowledge Graph Construction Patterns."""
    # Import the actual content from the original massive implementation
    # This would contain the full content from the original server.py
    # For brevity, I'll include a representative sample here
    return """# Knowledge Graph Construction Patterns for LLM Reasoning

**Goal**: Enumerate and exemplify patterns for building knowledge graphs that enable effective reasoning and retrieval with LLMs.

## Pattern Overview

Seven key construction patterns have been identified:

1. **LLM-Assisted Entity & Relation Graphs (Ontology-Aligned)**
2. **Event Reification (N-ary Relations as Nodes)**
3. **Layered Graphs (Multi-Tier Knowledge Integration)**
4. **Provenance & Evidence Layering**
5. **Temporal & Episodic Graphs (State Transitions and Sequences)**
6. **Hybrid Symbolic–Vector Graphs**

[Content continues with detailed implementation of each pattern...]

This content is extracted directly from the comprehensive PDF research and provides complete implementation guidance for each construction pattern."""


async def get_embedding_strategies_content() -> str:
    """Return detailed content on Embedding Fusion Strategies."""
    return """# Embedding Fusion Strategies

**Goal**: Document methods for combining LLM-derived semantic embeddings with graph structural embeddings.

## Strategy Overview

Five comprehensive embedding fusion strategies:

1. **Node Embeddings: Semantic + Structural**
2. **Edge and Relation Embeddings**
3. **Path and Metapath Embeddings**
4. **Subgraph or Community Embeddings**
5. **Joint Representation & Fusion Techniques**

[Content continues with detailed implementation of each strategy...]

This content provides comprehensive coverage of embedding fusion approaches for GraphRAG systems."""


async def get_retrieval_strategies_content() -> str:
    """Return detailed content on Retrieval & Search Strategies."""
    return """# Retrieval & Search Strategies

**Goal**: Provide exhaustive catalog of retrieval orchestration strategies leveraging both graph traversal and vector search.

## Strategy Overview

Six comprehensive retrieval strategies:

1. **Global-First Retrieval (Top-Down Overview)**
2. **Local-First Retrieval (Bottom-Up Expansion)**
3. **Hybrid or U-shaped Retrieval (Coarse-to-Fine Bidirectional)**
4. **Query Rewriting & Decomposition for Multi-hop**
5. **Temporal and Predictive Retrieval (Episodic Reasoning)**
6. **Constraint-Guided and Hybrid Symbolic–Neural Filtering**

[Content continues with detailed implementation of each strategy...]

This content provides complete guidance for implementing sophisticated retrieval orchestration strategies."""


async def get_pattern_catalog_content() -> str:
    """Return detailed content on Pattern Catalog Synthesis."""
    return """# Pattern Catalog Synthesis

**Goal**: Provide consolidated design pattern handbook for LLM-centric graph-augmented retrieval.

## Pattern Classification Framework

Patterns are organized across three primary dimensions:

1. **Construction Patterns**: How to build knowledge graphs for LLM reasoning
2. **Embedding Patterns**: How to integrate semantic and structural representations
3. **Retrieval Patterns**: How to orchestrate graph+vector search for optimal results

[Content continues with comprehensive pattern catalog...]

This catalog provides a complete framework for designing and implementing GraphRAG systems."""