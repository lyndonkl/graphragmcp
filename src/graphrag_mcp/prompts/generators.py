"""
Prompt generators for GraphRAG MCP Server.
"""

from typing import Dict
import mcp.types as types


async def generate_analyze_pattern_prompt(arguments: Dict[str, str]) -> types.GetPromptResult:
    """Generate prompt for analyzing GraphRAG patterns."""
    use_case = arguments.get("use_case", "")
    constraints = arguments.get("constraints", "Not specified")

    prompt = f"""Based on the comprehensive GraphRAG research, analyze the best pattern(s) for this use case:

**Use Case**: {use_case}
**Constraints**: {constraints}

Please consider:

1. **Construction Patterns**: Which of the 6 construction patterns would be most suitable?
   - LLM-Assisted Entity & Relation Graphs (Ontology-Aligned)
   - Event Reification (N-ary Relations as Nodes)
   - Layered Graphs (Multi-Tier Knowledge Integration)
   - Provenance & Evidence Layering
   - Temporal & Episodic Graphs
   - Hybrid Symbolic-Vector Graphs

2. **Embedding Strategies**: Which embedding fusion approaches would work best?
   - Node embeddings (semantic + structural)
   - Edge/relation embeddings
   - Path/metapath embeddings
   - Subgraph/community embeddings
   - Joint representation fusion

3. **Retrieval Strategies**: Which retrieval orchestration strategy fits the query patterns?
   - Global-first retrieval (top-down)
   - Local-first retrieval (bottom-up)
   - U-shaped hybrid retrieval
   - Query rewriting & decomposition
   - Temporal/predictive retrieval
   - Constraint-guided filtering

4. **Architecture Choice**: Should this use RDF/OWL, LPG, hypergraphs, or factor graphs?

Provide specific recommendations with reasoning based on the research findings."""

    return types.GetPromptResult(
        description="Analysis of best GraphRAG patterns for the specified use case",
        messages=[
            types.PromptMessage(
                role="user",
                content=types.TextContent(type="text", text=prompt),
            ),
        ],
    )


async def generate_design_knowledge_graph_prompt(arguments: Dict[str, str]) -> types.GetPromptResult:
    """Generate prompt for knowledge graph design guidance."""
    domain = arguments.get("domain", "")
    data_sources = arguments.get("data_sources", "")
    query_types = arguments.get("query_types", "Not specified")

    prompt = f"""Design a knowledge graph structure for LLM integration:

**Domain**: {domain}
**Data Sources**: {data_sources}
**Expected Query Types**: {query_types}

Based on the GraphRAG research, please provide:

1. **Graph Construction Approach**:
   - Which construction pattern(s) to use and why
   - How to handle entity extraction and relation modeling
   - Ontology alignment strategy (if applicable)
   - Event modeling approach for complex relationships

2. **Layering Strategy**:
   - Whether to use layered graphs (user data → domain knowledge → canonical knowledge)
   - How to structure the layers for your domain
   - Integration points between layers

3. **Temporal Considerations**:
   - Whether temporal/episodic modeling is needed
   - How to handle state transitions and sequences
   - Provenance and evidence tracking requirements

4. **Embedding Integration**:
   - Which types of embeddings to compute (node, edge, path, subgraph)
   - How to fuse semantic and structural information
   - Vector indexing strategy

5. **Technology Recommendations**:
   - Graph database choice (Neo4j, Neptune, GraphDB, etc.)
   - Vector database for hybrid search
   - Integration framework recommendations

Please reference specific examples and patterns from the research where applicable."""

    return types.GetPromptResult(
        description="Knowledge graph design guidance for the specified domain",
        messages=[
            types.PromptMessage(
                role="user",
                content=types.TextContent(type="text", text=prompt),
            ),
        ],
    )


async def generate_implement_retrieval_strategy_prompt(arguments: Dict[str, str]) -> types.GetPromptResult:
    """Generate prompt for retrieval strategy implementation."""
    strategy = arguments.get("strategy", "")
    tech_stack = arguments.get("technology_stack", "Open to suggestions")

    prompt = f"""Provide implementation guidance for the {strategy} retrieval strategy:

**Technology Stack Preference**: {tech_stack}

Based on the GraphRAG research, please provide:

1. **Strategy Overview**:
   - Detailed mechanics of how {strategy} works
   - When this strategy is most effective
   - Typical query patterns it handles well

2. **Implementation Steps**:
   - Step-by-step implementation approach
   - Key algorithms or techniques required
   - Data structures and indexing needs

3. **Technology Integration**:
   - Recommended tools and frameworks
   - How to integrate with LLM applications
   - Performance considerations and optimizations

4. **Code Architecture**:
   - High-level system design
   - API or interface design
   - Error handling and edge cases

5. **Evaluation and Tuning**:
   - How to measure strategy effectiveness
   - Parameters to tune for different use cases
   - Common pitfalls and how to avoid them

Please include specific examples and reference implementations where available from the research."""

    return types.GetPromptResult(
        description=f"Implementation guidance for {strategy}",
        messages=[
            types.PromptMessage(
                role="user",
                content=types.TextContent(type="text", text=prompt),
            ),
        ],
    )


async def generate_compare_architectures_prompt(arguments: Dict[str, str]) -> types.GetPromptResult:
    """Generate prompt for architecture comparison."""
    requirements = arguments.get("requirements", "")

    prompt = f"""Compare graph model architectures for these requirements:

**Requirements**: {requirements}

Based on the architectural trade-offs analysis in the GraphRAG research, please compare:

1. **Labeled Property Graphs (LPG)**:
   - Pros and cons for your requirements
   - Best use cases and limitations
   - Technology options (Neo4j, TigerGraph, etc.)
   - LLM integration capabilities

2. **RDF/OWL Triple Stores**:
   - Advantages for standardization and reasoning
   - Interoperability benefits
   - Query capabilities (SPARQL)
   - Performance considerations

3. **Hypergraphs and N-ary Structures**:
   - When complex multi-entity relationships matter
   - Implementation complexity vs. benefits
   - Tool availability and maturity

4. **Hybrid Approaches**:
   - Combining multiple graph models
   - Vector database integration
   - Multi-modal data handling

5. **Recommendation**:
   - Which architecture best fits your requirements
   - Implementation strategy
   - Technology stack suggestions
   - Migration considerations if applicable

Please reference specific research findings and industry examples where relevant."""

    return types.GetPromptResult(
        description="Architectural comparison for the specified requirements",
        messages=[
            types.PromptMessage(
                role="user",
                content=types.TextContent(type="text", text=prompt),
            ),
        ],
    )