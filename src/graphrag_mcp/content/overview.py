"""
Overview content for GraphRAG MCP Server.
"""


async def get_overview_content() -> str:
    """Return the comprehensive overview of GraphRAG research."""
    return """# Knowledge Graph Construction & Retrieval Strategies for LLM Reasoning

## Abstract

This handbook provides a comprehensive survey of graph-based design patterns and retrieval strategies that combine LLM-driven semantic embeddings with graph-structured knowledge to enhance reasoning in Retrieval-Augmented Generation (RAG) systems.

## Seven Key Tracks Covered

1. **Knowledge Graph Construction Patterns for LLM Reasoning** - Seven distinct patterns for building knowledge graphs that enable effective reasoning and retrieval with LLMs
2. **Embedding Fusion Strategies** - Five comprehensive strategies for combining semantic and structural embeddings at various graph granularities
3. **Retrieval & Search Strategies** - Six exhaustive strategies for retrieval orchestration leveraging both graph traversal and vector search
4. **Architectural Trade-offs in Graph Models** - Analysis of LPG, RDF/OWL, hypergraphs, and factor graphs for LLM integration
5. **Recent Research & Industry Practice (2022–present)** - Latest developments and current industry implementations
6. **Frameworks & Technology Stacks** - Survey of platforms enabling hybrid graph + vector retrieval
7. **Consolidated Pattern Catalog** - Design pattern handbook distilled from all findings

## Focus and Emphasis

- **LLMs as reasoning engines** augmented by hybrid symbolic–vector knowledge
- **Multi-hop reasoning, evidence retrieval, and robust LLM outputs**
- **Practical implementation guidance** with grounded examples from healthcare, finance, and research domains
- **Complete coverage** with 141 research citations for further detail

## Key Domains and Applications

Examples are drawn from:
- **Healthcare**: Patient EHR graphs, medical knowledge integration, clinical reasoning
- **Finance**: Market analysis, regulatory compliance, risk assessment
- **Research**: Academic collaboration networks, literature mining, knowledge discovery
- **Enterprise**: Organizational knowledge, project management, decision support

This research addresses LLM limitations in handling domain-specific terms and provides structured approaches for consistent naming, retrieval, and reasoning across complex knowledge domains.
"""