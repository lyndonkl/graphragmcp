#!/usr/bin/env python3
"""
GraphRAG MCP Server

A Model Context Protocol server for Knowledge Graph Construction & Retrieval
Strategies for LLM Reasoning. This server provides hierarchical access to
comprehensive research on graph-based design patterns and retrieval strategies
that combine LLM-driven semantic embeddings with graph-structured knowledge.

Based on the research document: "Knowledge Graph Construction & Retrieval
Strategies for LLM Reasoning"
"""

import json
import logging
from typing import Any, Dict, List, Optional, Union
import mcp.types as types
from mcp.server import NotificationOptions, Server
from mcp.server.models import InitializationOptions
import mcp.server.stdio

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("graphrag-mcp")

# Create server instance
server = Server("graphrag-mcp")


@server.list_resources()
async def handle_list_resources() -> list[types.Resource]:
    """List available GraphRAG knowledge resources in hierarchical structure."""
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


@server.read_resource()
async def handle_read_resource(uri: str) -> str:
    """Read and return content for the specified GraphRAG knowledge resource."""

    if uri == "graphrag://overview":
        return await _get_overview_content()
    elif uri == "graphrag://construction-patterns":
        return await _get_construction_patterns_content()
    elif uri == "graphrag://embedding-strategies":
        return await _get_embedding_strategies_content()
    elif uri == "graphrag://retrieval-strategies":
        return await _get_retrieval_strategies_content()
    elif uri == "graphrag://architectural-tradeoffs":
        return await _get_architectural_tradeoffs_content()
    elif uri == "graphrag://literature-landscape":
        return await _get_literature_landscape_content()
    elif uri == "graphrag://technology-stacks":
        return await _get_technology_stacks_content()
    elif uri == "graphrag://pattern-catalog":
        return await _get_pattern_catalog_content()
    # Detailed sub-pattern resources
    elif uri.startswith("graphrag://patterns/"):
        return await _get_construction_pattern_detail(uri)
    elif uri.startswith("graphrag://embeddings/"):
        return await _get_embedding_strategy_detail(uri)
    elif uri.startswith("graphrag://retrieval/"):
        return await _get_retrieval_strategy_detail(uri)
    else:
        raise ValueError(f"Unknown resource URI: {uri}")


async def _get_overview_content() -> str:
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


async def _get_construction_patterns_content() -> str:
    """Return detailed content on Knowledge Graph Construction Patterns."""
    return """# Knowledge Graph Construction Patterns for LLM Reasoning

**Goal**: Enumerate and exemplify patterns for building knowledge graphs that enable effective reasoning and retrieval with LLMs. Each pattern details its purpose, the mechanics of graph construction (ingestion to indexing), and a grounded example.

## Pattern Overview

Seven key construction patterns have been identified:

1. **LLM-Assisted Entity & Relation Graphs (Ontology-Aligned)**
2. **Event Reification (N-ary Relations as Nodes)**
3. **Layered Graphs (Multi-Tier Knowledge Integration)**
4. **Provenance & Evidence Layering**
5. **Temporal & Episodic Graphs (State Transitions and Sequences)**
6. **Hybrid Symbolic–Vector Graphs**

## 1. LLM-Assisted Entity & Relation Graphs (Ontology-Aligned)

**Pattern**: LLM-driven extraction of entities/relations aligned to ontologies or taxonomies.

**Purpose**: Capture knowledge from unstructured data into a structured graph that an LLM can navigate. By aligning extracted entities to known ontologies (e.g. UMLS in healthcare or corporate taxonomies), the graph provides a backbone of canonical concepts for consistent reasoning.

### Mechanics

The pipeline typically involves:

**Ingestion & Chunking**: Break documents into manageable sections with hybrid semantic chunking to preserve context.

**Entity Extraction**: Identify key entities (people, concepts, drugs, etc.) using NER, possibly in a multi-round process where the LLM double-checks if all entities are found. Each entity is linked to a canonical ID in an ontology or dictionary if available.

**Relation Extraction**: Detect relations between entities via dependency parsing, prompt-based LLM extraction, or a combination of rule-based and ML methods. For robust results, LLMs can be prompted in stages: first list entities, then describe relations among them. Incorporate domain knowledge by few-shot examples.

**Alignment & Deduplication**: Merge synonymous entities (e.g. "heart attack" with "myocardial infarction" via ontology) to avoid duplicates. Link to taxonomy nodes.

**Graph Assembly**: Create nodes for entities (with type labels from ontology) and edges for relations. Attach context metadata to each (source document, sentence, etc., for provenance).

**Indexing**: Index the graph for fast retrieval (store adjacency lists, and optionally vectorize node text for hybrid search).

### Example: Healthcare Knowledge Graph

Processing patient clinical notes and medical literature to build a patient-centric knowledge graph. The LLM extracts medical entities (symptoms, diagnoses, medications) and links them to a medical ontology (e.g. SNOMED or UMLS).

From a note "Patient has elevated LDL and was prescribed atorvastatin":
- Creates nodes: `PatientX`, `Hyperlipidemia` (mapped to ontology term), `Atorvastatin`
- Creates relations: `treatment(PatientX, Atorvastatin)` and `finding(PatientX, Hyperlipidemia)`
- Aligns drug and condition to databases like DrugBank or MeSH

This structured graph becomes the foundation for queries like "What treatments target the genes involved in Hyperlipidemia?" – the graph can be traversed to find relevant connections, which the LLM can then reason over with reduced hallucination.

## 2. Event Reification (N-ary Relations as Nodes)

**Pattern**: Model complex n-ary events or relations as first-class nodes (hypernodes) with links to participating entities (reification).

**Purpose**: Enable representation of multi-entity interactions (beyond binary relations) that are common in real-world scenarios, thereby preserving full context for LLM reasoning. Many important facts involve more than two entities (e.g. a clinical trial linking a drug, a disease, a patient group, and an outcome).

### Mechanics

Instead of only nodes for entities and binary edges, introduce event nodes:

**Event Identification**: Use LLMs or rule-based extraction to identify text descriptions of events or n-ary relations. For example, in healthcare: "Patient X was given Drug Y for Condition Z on Date T leading to Outcome O."

**Event Node Creation**: Create a node representing the event (e.g. a node labeled `TreatmentEvent`) and attach attributes like date or type of event.

**Role Edges**: Link the event node to each participating entity with role-specific edge labels (e.g. `has_patient→PatientX`, `has_drug→DrugY`, `for_condition→ConditionZ`, `date→T`, `resulted_in→OutcomeO`).

**Normalization**: Use ontologies for event types if available. An LLM can assist by classifying event type from description.

**Provenance & Confidence**: Optionally attach source and confidence to the event node.

### Example: Hospital Visit Event

In a patient's health record graph, represent a hospital visit as an event node with edges to:
- Patient: `PatientX`
- Physician: `Dr. Jones`
- Diagnosis: `Appendicitis`
- Procedure: `Appendectomy`
- Date: `2025-09-01`
- Outcome: `Recovered`

By modeling this as one unit, an LLM can retrieve the entire context when asked "What happened during Patient X's ER visit in September?".

## Integration with Healthcare Applications

Recent research like HyperGraphRAG explicitly advocates hypergraph structures for medical cases where facts like "male hypertensive patients with creatinine 115–133 µmol/L are diagnosed with mild elevation" would lose information if broken into pairwise relations.

For detailed implementations of each pattern, see the specific pattern resources in this knowledge base.
"""


# Continue implementing other content methods...
async def _get_embedding_strategies_content() -> str:
    """Return detailed content on Embedding Fusion Strategies."""
    return """# Embedding Fusion Strategies

**Goal**: Document methods for combining LLM-derived semantic embeddings with graph structural embeddings or features. We discuss strategies at various graph granularities (node, edge, path, subgraph) and how these embeddings are fused or used in retrieval.

## Strategy Overview

Five comprehensive embedding fusion strategies:

1. **Node Embeddings: Semantic + Structural**
2. **Edge and Relation Embeddings**
3. **Path and Metapath Embeddings**
4. **Subgraph or Community Embeddings**
5. **Joint Representation & Fusion Techniques**

## 1. Node Embeddings: Semantic + Structural

**Strategy**: Augment each graph node with an embedding that captures both its semantic content and structural context.

### Mechanics

**Semantic Text Embedding**: Use an LLM or encoder to embed a textual representation of the node. The text could be the node's label plus a summary of its directly connected neighbors.

**Graph Structural Embedding**: Use graph embedding techniques (Node2Vec, DeepWalk, GraphSAGE, etc.) to get a vector based on the node's position in the graph topology.

**Feature Combination**: Concatenate or average the semantic and structural vectors to create a hybrid embedding. Alternatively, feed the structural info as additional tokens into an LLM for embedding.

**Storage and Indexing**: Store node embeddings in a vector index keyed by node ID for similarity search.

### Application Example: Analogous Patients

In a healthcare knowledge graph, each patient node has an embedding encoding their profile (e.g., "Patient, 45-year-old male with Type-2 Diabetes and Hypertension, on Metformin and Lisinopril").

Combine:
- Semantic embedding of the textual summary
- Structural embedding from the patient's connections to disease/medication nodes

When a clinician asks "Find patients similar to John Doe", the system can vector-search the patient node embeddings to find analogous cases for outcome prediction.

## 2. Edge and Relation Embeddings

**Strategy**: Represent edges (relations) with embeddings that incorporate the relationship's semantics and context.

### Mechanics

**Relation Type Embeddings**: Embed each relation label (e.g., "treats", "causes") by using its name or definition for analogical matching.

**Specific Edge Embeddings**: Form triplet representations like "Drug X treats Disease Y" and embed the sentence with an LLM encoder.

**Neighborhood Context**: Enhance edge embedding by incorporating neighbor info (e.g., "Drug X treats Disease Y, as evidenced by Study Z").

**Use in Retrieval**: Treat each edge as a document in a vector index of facts for semantic similarity queries.

### Application Example: FAQ Retrieval

Knowledge base with triples: `<Issue> —[solution]→ <Procedure>`. User asks "How can I reset my password if I forgot it?".

By embedding the edge text "If a user forgets their password, they should follow the account recovery procedure", the system retrieves it as relevant knowledge, allowing the LLM to generate answer steps.

## 3. Path and Metapath Embeddings

**Strategy**: Represent sequences of connected nodes and edges (paths) as embeddings, especially typed metapaths in heterogeneous graphs.

### Mechanics

**Path Encoding**: Take a path like `Company A -> (acquires) -> Company B -> (hires) -> Person X`. Construct textual description: "Company A acquired Company B, which hired Person X." Embed this sentence.

**Metapath Patterns**: In heterogeneous graphs, metapaths are sequences of types like `Author - Paper - Author` (co-authorship). Generate verbalizations: "Author A co-authored a paper with Author B" and embed these.

**Use in Retrieval**: Meta-path guided retrieval where the system picks relevant metapath and finds actual path instances matching it.

### Application Example: Collaboration Discovery

Query: "How are Dr. Smith and Dr. Garcia connected?" System embeds metapath `Author–Paper–Author–Paper–Author` describing indirect collaboration. Retrieval finds: "Dr. Smith co-authored with Dr. Lee, who co-authored with Dr. Garcia."

## 4. Subgraph or Community Embeddings

**Strategy**: Compute embeddings for entire subgraphs or clusters of nodes (beyond linear paths) to use as retrievable units.

### Mechanics

**Ego-network Embedding**: For each node, consider its k-hop neighborhood. Flatten into structured text and encode with an LLM, producing an embedding representing that entity in context.

**Community Embedding**: Treat entire communities as subgraphs and embed summaries. For instance, cluster diseases related to metabolic syndrome and embed that cluster.

**Dynamic Subgraph Construction**: Given a query, extract a subgraph and embed it on-the-fly using LLM.

### Application Example: Evidence Bundle Ranking

Legal scenario: "What evidence supports that Company X was knowingly involved in fraud Y?" System gathers subgraph of facts around Company X and fraud Y. Instead of feeding nodes separately, embed the entire connected subgraph representing the fraud involvement pattern.

## 5. Joint Representation & Fusion Techniques

**Strategy**: Combine or align multiple embedding types into joint space or use multi-step ranking (bi-encoder + cross-encoder) to fuse semantic and structural signals.

### Mechanics

**Contrastive Alignment**: Train system so textual and graph-based embeddings coincide for the same entity or fact.

**Late Fusion via Re-ranking**: Do broad retrieval with one embedding, then re-rank with more powerful model incorporating structural context.

**Enrich Query with Graph Info**: Use graph to expand query before embedding it (append related terms as context).

**Multi-vector Representations**: Allow each entity to have multiple embeddings capturing different aspects.

### Application Example: Semantic Query + Type Constraint

Enterprise query: "Find all projects involving machine learning led by Alice."

1. Use graph to parse structurally: identify "Alice" as Person, "machine learning" as topic, expecting Project node answer
2. Use semantic embedding for "project involving machine learning" concept
3. Filter candidates: Project nodes with Alice as leader (symbolic filter)
4. Among those, rank by embedding similarity to "machine learning project"
5. Verify with cross-encoder for final precision

This hybrid approach ensures both semantic relevance and structural correctness.

## Integration Benefits

These embedding fusion strategies leverage complementary strengths:
- **Graphs**: Provide structured, relational knowledge and constraints
- **LLMs**: Provide understanding and generative flexibility
- **Combined**: Enable hybrid retrieval supporting both exact logical relationships and fuzzy semantic similarity

The result is systems that can reason analogically while respecting structural constraints, leading to more accurate and contextually appropriate responses.
"""


# Additional content generation methods would continue here...
async def _get_retrieval_strategies_content() -> str:
    """Return detailed content on Retrieval & Search Strategies."""
    return """# Retrieval & Search Strategies

**Goal**: Provide an exhaustive catalog of retrieval orchestration strategies that leverage both graph traversal and vector search, tailored for LLM integration. Each strategy describes mechanics, best-suited query types, and grounded examples.

## Strategy Overview

Six comprehensive retrieval strategies:

1. **Global-First Retrieval (Top-Down Overview)**
2. **Local-First Retrieval (Bottom-Up Expansion)**
3. **Hybrid or U-shaped Retrieval (Coarse-to-Fine Bidirectional)**
4. **Query Rewriting & Decomposition for Multi-hop**
5. **Temporal and Predictive Retrieval (Episodic Reasoning)**
6. **Constraint-Guided and Hybrid Symbolic–Neural Filtering**

## 1. Global-First Retrieval (Top-Down Overview)

**Strategy**: Start by retrieving a global summary or relevant high-level nodes to get an overview, then optionally drill down for details.

### Mechanics
- **Global graph summary search**: Search for high-level concept nodes or subgraph most relevant to query
- **Use of Summarized Index**: Match against community embeddings or topic clusters first
- **Traverse downward**: Once relevant region identified, perform targeted retrieval within that region
- **Pre-indexing communities**: If hierarchical ontology exists, first find broad categories then specifics

### Best-Suited Queries
- Broad or exploratory questions: "What are the main health effects of climate change?"
- Summary requests: "Give me an overview of patient X's medical history"
- Context-before-specifics: "Explain the relationship between diet and heart disease"

### Example: MedGraphRAG Overview Query

Query: "What is MedGraphRAG and how does it work in healthcare?"

1. Recognize "MedGraphRAG" as high-level entity, retrieve summary node with attached info: "medical graph-based retrieval system using hierarchical graphs and U-retrieval"
2. Fetch connected concepts: "Triple Graph Construction" and "U-Retrieval strategy"
3. LLM answers with overview: "MedGraphRAG is a graph-based RAG for medicine using three-layer graph linking patient data to medical literature to dictionary, with U-shaped retrieval combining top-down search and bottom-up refinement"

## 2. Local-First Retrieval (Bottom-Up Expansion)

**Strategy**: Begin at specific seed entities (identified from query) and explore outward (neighbors, connections) to gather relevant information.

### Mechanics
- **Entity linking**: Use LLM to find key entities in query
- **Retrieve seed nodes**: Fetch entity nodes from graph, anchoring the search
- **Neighborhood Expansion**: From seed nodes, traverse to connected nodes following relevant edges
- **Gather & Rank**: Use ranking by relevance to pick top facts from local subgraph
- **Iterative deepening**: If initial expansion insufficient, go one hop further

### Best-Suited Queries
- Entity-focused questions: "What are the side effects of Metformin in patients with kidney disease?"
- Relationship queries: "Who are Alice's direct collaborators on project Phoenix?"
- Queries using specific terms that map to graph entities

### Example: Medical Query

Query: "This patient has Type 2 Diabetes and Hypertension. What drugs should be avoided or used with caution?"

1. **Identify seeds**: Type 2 Diabetes and Hypertension nodes in Layer 3
2. **Expand neighbors**: Find medication nodes connected with `treatment` or `contraindication` edges
3. **Combine relevant neighbors**: Gather drugs problematic for diabetics, drugs to avoid if diabetic
4. **LLM synthesis**: "For patients with both diabetes and hypertension, certain medications require caution. High-dose thiazide diuretics can worsen glucose control, and beta-blockers may mask hypoglycemia symptoms."

## 3. Hybrid or U-shaped Retrieval (Coarse-to-Fine Bidirectional)

**Strategy**: Combine global and local strategies in two-stage process - top-down coarse retrieval to find context, followed by bottom-up detailed retrieval to refine answer.

### Mechanics
- **Top-Down Phase**: Interpret query and retrieve high-level nodes or summaries (global context identification)
- **Drill-Down Phase**: Use context from phase 1 to perform targeted local expansion
- **Response Generation**: LLM generates answer using detailed info while staying framed by global context
- **Iterative Loops**: Can iterate if initial answer raises need for more information

### Best-Suited Queries
- Complex queries requiring broad knowledge plus specific evidence
- Specialized domains where context is layered (medical diagnosis requiring overview then specifics)
- Long-form questions needing overview then elaboration
- Potentially ambiguous queries touching multiple aspects

### Example: Medical Literature Query

Query: "What are the risks of prescribing beta-blockers to diabetic patients and what does medical literature say?"

**Top-Down**: Classify as medical query, identify main tags (beta-blockers, diabetic patients), retrieve meta-graph connecting these concepts

**Bottom-Up**: Fetch direct relations - beta-blockers' known effects ("mask hypoglycemia"), diabetes vulnerabilities, literature evidence from specific studies

**Generate Answer**: "Beta-blockers can mask hypoglycemia in diabetic patients by blunting adrenergic warning signs of low blood sugar. Medical literature confirms this risk - a 2023 study notes diabetics on non-selective beta-blockers had more unrecognized hypoglycemic episodes. Should be prescribed with caution and close monitoring."

## 4. Query Rewriting & Decomposition for Multi-hop

**Strategy**: Use LLM to rewrite user query or break it into sub-queries that incorporate graph context, enabling multi-hop retrieval via iterative steps.

### Mechanics
- **Complex query analysis**: Analyze query for multiple parts or hops
- **Rewrite or Split**: LLM generates simpler sub-queries to execute sequentially
- **Sequential Retrieval**: Execute sub-queries against graph, with first result informing second
- **Aggregation**: Combine results to answer original query
- **Multi-hop traversal guided by prompts**: Self-ask pattern where LLM iteratively decides what to find next

### Best-Suited Queries
- Multi-condition questions: "Which authors who wrote about machine learning have also won a Turing Award?"
- Implicit multi-hop: "Is there relationship between Entity A and Entity C through something in common?"
- Complex filter questions combining graph relations and attributes

### Example: Cross-Condition Drug Query

Query: "Find a medication that treats hypertension but should be avoided in diabetic patients."

**LLM Decomposition**:
1. "What medications treat hypertension?" (hop 1)
2. "Which of these medications are contraindicated in diabetes?" (hop 2)

**Execution**:
- Hop 1 yields: [Hydrochlorothiazide, Beta-blocker, ACE inhibitor, etc.]
- Hop 2: Check each for diabetes warnings, finds Beta-blockers have contraindication edge

**Answer**: "Beta-blockers treat hypertension but must be used cautiously in diabetic patients as they can mask hypoglycemia symptoms."

## 5. Temporal and Predictive Retrieval (Episodic Reasoning)

**Strategy**: Incorporate time-based searching to handle queries about sequence, future events, or historical state, using temporal graph constructs.

### Mechanics
- **Time-slice filtering**: Apply filter on graph by timestamp for historical questions
- **Episodic windowing**: Use temporal links to retrieve sequences (what happened after X?)
- **Nearest neighbor sequence**: For predictions, find similar past sequences and see what followed
- **Pattern-based reasoning**: Search for known temporal patterns or progression pathways
- **Time-decay ranking**: Rank recent nodes higher when recency matters

### Best-Suited Queries
- "What happens next" queries in stories, processes, or data sequences
- Historical comparisons and trend analysis
- Temporal fact-checking: "Who was CEO of Company Z in 2010?"
- Planning/simulation questions: "If event A occurs, what follows?"

### Example: Patient Timeline Prediction

Patient graph shows: 2018 Prediabetes → 2020 Type 2 Diabetes → 2022 Early Kidney Disease

Query: "What complications should we watch for next?"

**Temporal retrieval**: Find similar progression patterns in other patients, retrieve statistical edges showing diabetes + kidney disease often leads to retinopathy or cardiac complications

**Answer**: "Having diabetes with early kidney disease suggests other complications may arise. Diabetic patients often develop retinopathy after long-term disease, and the combination increases cardiovascular risks. Monitor patient's eyes and heart."

## 6. Constraint-Guided and Hybrid Symbolic–Neural Filtering

**Strategy**: Apply explicit symbolic constraints (type, attribute, rules) to narrow search space, then use neural ranking or expansion on filtered set.

### Mechanics
- **Pre-filter by type/attribute**: Restrict retrieval to certain node types before vector search
- **Apply known rules**: Incorporate domain rules or ontology constraints
- **Symbolic Graph Query then Neural Re-rank**: Run precise graph query, then embed candidates and use LLM to rank
- **Post-filter after neural retrieval**: Broad vector search followed by symbolic criterion filtering
- **Use of reasoning rules**: Incorporate rule engine for constraint solving

### Best-Suited Queries
- Queries with explicit filters: "Which European cities have hosted Olympics more than once?"
- Cases where certain answers would be invalid given context
- Multi-domain RAG requiring joins between structured and unstructured data
- Yes/No questions with constraints needing verification

### Example: Travel Assistant Query

Query: "Find kid-friendly museums in Paris open on Sundays."

**Constraint extraction**: kid-friendly (category=children), location=Paris, open_on_Sunday=true

**Graph filter**: Query for Museum nodes with location Paris AND open_on_Sunday=true AND audience includes "Children"

**Vector re-rank**: Among filtered candidates, rank by "kid-friendliness" description

**Answer**: "The Cité des Enfants at La Villette is a very kid-friendly museum in Paris open on Sundays" - satisfies all criteria.

## Integration and Orchestration

These strategies can be combined as needed:
- **U-shaped retrieval** might use **constraint filtering** at each stage
- **Query decomposition** might trigger multiple **local-first** retrievals
- **Global-first** can be followed by **temporal retrieval** for time-sensitive aspects

The choice depends on query complexity, domain requirements, and performance constraints. Most production systems use hybrid approaches, combining multiple strategies for robust coverage.
"""


# Placeholder implementations for other content methods
async def _get_architectural_tradeoffs_content() -> str:
    """Return detailed content on Architectural Trade-offs in Graph Models."""
    return """# Architectural Trade-offs in Graph Models for LLM Retrieval

**Goal**: Compare and analyze pros and cons of different graph data model architectures (LPG, RDF/OWL, hypergraphs, factor graphs) for integrating with LLMs in retrieval-augmented generation systems.

## Model Architecture Overview

Four primary graph model architectures are analyzed:

1. **Labeled Property Graphs (LPG)**
2. **RDF/OWL Triple Stores**
3. **Hypergraphs and N-ary Structures**
4. **Factor Graphs and Probabilistic Models**

## 1. Labeled Property Graphs (LPG)

**Architecture**: Nodes and edges can have multiple labels/types and arbitrary key-value properties.

### Advantages for LLM Integration

**Intuitive Modeling**: LPGs naturally model real-world entities and relationships with rich metadata. Properties on nodes/edges align well with how LLMs understand contextual information.

**Flexible Schema**: No rigid schema requirements - can evolve as understanding of domain grows. LLMs can help extract properties dynamically without predefined ontologies.

**Performance**: Optimized for traversal queries common in RAG scenarios. Index structures in Neo4j, TigerGraph enable fast neighbor lookups needed for local-first retrieval.

**Embedding Integration**: Properties can include embedding vectors directly. Nodes can have both semantic text and structural embeddings as properties.

**Query Language Expressiveness**: Cypher (Neo4j) and GSQL (TigerGraph) provide intuitive pattern matching that maps well to natural language queries.

### Disadvantages

**Limited Standardization**: Each LPG database has proprietary formats and query languages, making portability difficult.

**Complex N-ary Relationships**: Requires reification patterns to represent relationships involving more than two entities, adding modeling complexity.

**Reasoning Limitations**: Limited built-in support for logical inference compared to RDF/OWL systems.

**Interoperability**: Difficult to integrate with external knowledge bases using standards like Linked Data.

### Best Use Cases

- Enterprise knowledge graphs with evolving schemas
- Social networks and recommendation systems
- Fraud detection requiring complex pattern matching
- Healthcare systems needing flexible patient-centric modeling

### Technology Options

**Neo4j**: Most mature, excellent Cypher query language, strong community
**TigerGraph**: High performance for large-scale analytics, parallel processing
**Amazon Neptune**: Managed service, supports both LPG and RDF
**ArangoDB**: Multi-model database supporting graphs, documents, key-value

## 2. RDF/OWL Triple Stores

**Architecture**: Everything represented as subject-predicate-object triples, with optional ontology-based reasoning.

### Advantages for LLM Integration

**Standardization**: W3C standards ensure interoperability. Can integrate easily with external knowledge bases like DBpedia, Wikidata.

**Semantic Reasoning**: OWL ontologies enable automatic inference of new facts. LLMs can leverage inferred knowledge for more complete answers.

**Global Knowledge Integration**: Can federate queries across multiple SPARQL endpoints, accessing vast amounts of linked data.

**Vocabulary Reuse**: Standard vocabularies (FOAF, Schema.org, etc.) provide consistent naming for LLM understanding.

**Provenance Support**: Named graphs and reification support detailed provenance tracking for evidence-based reasoning.

### Disadvantages

**Triple Complexity**: Everything must be decomposed into subject-predicate-object format, which can be unnatural for complex relationships.

**Performance Limitations**: SPARQL queries can be slow compared to native graph databases, especially for traversal-heavy operations.

**Schema Rigidity**: Ontology design requires upfront planning. Changes can be complex to implement across large knowledge bases.

**Learning Curve**: SPARQL and OWL have steep learning curves compared to property graph query languages.

**Limited Property Support**: Properties on relationships require reification, making models more complex.

### Best Use Cases

- Scientific research requiring rigorous ontologies
- Government/healthcare systems needing standards compliance
- Cross-organizational data sharing initiatives
- Applications requiring automated reasoning and inference

### Technology Options

**Apache Jena/Fuseki**: Open source, strong SPARQL support
**Stardog**: Commercial, excellent reasoning and query optimization
**GraphDB**: RDF database with good performance and reasoning
**Amazon Neptune**: Managed service supporting both RDF and LPG

## 3. Hypergraphs and N-ary Structures

**Architecture**: Hyperedges can connect any number of nodes, naturally representing complex multi-entity relationships.

### Advantages for LLM Integration

**Natural N-ary Modeling**: Complex real-world relationships (medical diagnoses involving patient, symptoms, tests, treatments) fit naturally without reification.

**Rich Context Preservation**: Entire contexts can be preserved as single hyperedges, providing complete information for LLM reasoning.

**Reduced Model Complexity**: No need for intermediate nodes or complex reification patterns when dealing with multi-entity relationships.

**Enhanced Retrieval**: Can retrieve entire contextual units (hyperedges) rather than reconstructing from multiple binary relations.

### Disadvantages

**Tool Immaturity**: Limited commercial database support compared to LPG and RDF options. Most implementations are research-oriented.

**Query Complexity**: Query languages for hypergraphs are less developed and standardized than Cypher or SPARQL.

**Visualization Challenges**: Difficult to visualize and debug hypergraph structures compared to traditional graphs.

**Performance Unknowns**: Less research on optimization techniques and scalability compared to established graph models.

**Integration Challenges**: Fewer tools and libraries available for embedding generation and vector integration.

### Best Use Cases

- Medical/healthcare domains with complex multi-factor relationships
- Scientific modeling with inherently multi-dimensional relationships
- Event modeling where events naturally involve multiple entities
- Legal/regulatory domains with complex multi-party relationships

### Technology Options

**HyperGraphRAG**: Research implementation specifically for medical knowledge graphs
**HyperX**: Experimental hypergraph database
**Custom implementations**: Often built on top of existing graph databases

## 4. Factor Graphs and Probabilistic Models

**Architecture**: Bipartite graphs with variable nodes and factor nodes representing probabilistic relationships.

### Advantages for LLM Integration

**Uncertainty Handling**: Natural representation of uncertain or probabilistic knowledge, which complements LLM uncertainty estimation.

**Inference Integration**: Built-in probabilistic inference can provide confidence scores for retrieved information.

**Multi-modal Integration**: Can represent both symbolic knowledge and neural network outputs in unified framework.

**Causal Modeling**: Can represent causal relationships explicitly, supporting more sophisticated reasoning.

### Disadvantages

**Complexity**: Requires probabilistic modeling expertise, more complex than deterministic graph approaches.

**Computational Overhead**: Probabilistic inference can be computationally expensive for large graphs.

**Limited Tooling**: Fewer mature database solutions compared to LPG and RDF options.

**Interpretation Challenges**: Probabilistic outputs may be harder for end users to interpret and trust.

### Best Use Cases

- Applications requiring uncertainty quantification
- Causal reasoning and what-if analysis
- Integration with probabilistic ML models
- Risk assessment and decision support systems

### Technology Options

- Custom implementations using probabilistic programming frameworks
- Integration with tools like PyMC, Stan, or TensorFlow Probability

## Decision Framework

### Choose LPG When:
- Need flexible, evolving schemas
- Performance and traversal speed are critical
- Team familiar with property graph concepts
- Rich metadata on nodes/edges is important

### Choose RDF/OWL When:
- Standards compliance and interoperability essential
- Need to integrate with external linked data sources
- Automated reasoning and inference are required
- Long-term data preservation and sharing are priorities

### Choose Hypergraphs When:
- Domain has many natural n-ary relationships
- Preserving complete context is critical
- Willing to invest in custom tooling
- Research/experimental context acceptable

### Choose Factor Graphs When:
- Uncertainty quantification is essential
- Need to integrate probabilistic and symbolic reasoning
- Causal modeling is important
- Have expertise in probabilistic methods

## Hybrid Approaches

Many production systems combine multiple approaches:

**LPG + Vector Database**: Property graphs for structured relationships, vector databases for semantic search
**RDF + Property Graphs**: RDF for canonical knowledge, LPG for application-specific data
**Multi-modal Integration**: Different graph models for different data types within same application

## Performance Considerations

**Query Patterns**:
- LPG databases excel at traversal queries (finding paths, neighbors)
- RDF systems better for complex analytical queries requiring inference
- Hypergraphs best when queries naturally involve multi-entity contexts

**Scale Characteristics**:
- LPG systems generally handle larger node/edge counts efficiently
- RDF systems can struggle with very large triple counts but excel at complex reasoning
- Hypergraph performance depends heavily on implementation

**Embedding Integration**:
- LPG systems easiest for storing embeddings as node properties
- RDF systems require more complex approaches for vector integration
- Hypergraph and factor graph integration largely experimental

## Recommendations

For most LLM-integrated RAG systems, **start with LPG** unless specific requirements dictate otherwise:

1. **Rapid prototyping and development**
2. **Good balance of flexibility and performance**
3. **Mature tooling ecosystem**
4. **Natural fit with LLM reasoning patterns**

Consider **RDF/OWL** for:
- Standards-critical environments
- Heavy integration with external knowledge sources
- Domains requiring automated reasoning

Explore **hypergraphs** for specialized domains with complex n-ary relationships, but expect additional implementation effort.

**Factor graphs** should be considered when uncertainty quantification is a primary requirement, typically in risk assessment or decision support applications.

## Integration Patterns

Successful GraphRAG systems often use **layered architectures**:

1. **Canonical Layer**: RDF/OWL for standardized, shared knowledge
2. **Application Layer**: LPG for flexible, application-specific relationships
3. **Vector Layer**: Dedicated vector databases for semantic search
4. **Probabilistic Layer**: Factor graphs for uncertainty-critical decisions

This layered approach leverages the strengths of each model while mitigating individual weaknesses."""

async def _get_literature_landscape_content() -> str:
    """Return detailed content on External Literature & Industry Landscape."""
    return """# External Literature & Industry Landscape (2022–Present)

**Goal**: Survey recent research and current industry practice on graph-enhanced retrieval-augmented LLMs, providing comprehensive coverage of key developments from 2022-present.

## Research Evolution Timeline

### 2022: Foundation Period
- **GraphRAG emergence**: Microsoft Research introduces GraphRAG concepts combining knowledge graphs with RAG
- **Entity-centric approaches**: Focus on entity linking and relation extraction for knowledge graphs
- **Early graph + LLM integration experiments**: Initial work on using graphs to enhance LLM reasoning

### 2023: Methodological Advances
- **Multi-hop reasoning systems**: Development of sophisticated multi-hop retrieval strategies
- **Hybrid architectures**: Integration of vector databases with graph databases
- **Domain-specific applications**: Healthcare, finance, and legal applications emerge
- **Embedding fusion techniques**: Advanced methods for combining semantic and structural embeddings

### 2024-Present: Production Maturity
- **Enterprise adoption**: Major companies deploying graph-enhanced RAG in production
- **Framework consolidation**: Mature tooling ecosystems around LangChain, LlamaIndex integration
- **Performance optimization**: Focus on scaling and efficiency improvements
- **Specialized architectures**: Domain-specific graph models (medical, legal, scientific)

## Key Research Contributions

### Microsoft GraphRAG Research
**Core Innovation**: Global-first and local-first retrieval strategies with graph-based knowledge organization.

**Key Papers**:
- "From Local to Global: A Graph RAG Approach to Query-Focused Summarization" (2024)
- Research demonstrates significant improvements in complex query answering through hierarchical graph organization

**Industrial Impact**: Widely adopted in enterprise RAG systems, influencing commercial implementations.

### Neo4j and Graph Database Industry
**Research Focus**: Integration of LLMs with property graph databases for enterprise knowledge management.

**Key Contributions**:
- LLM-powered knowledge graph construction
- Cypher query generation from natural language
- Graph-guided RAG for enterprise search

**Production Systems**: Widespread deployment in customer support, internal knowledge bases, and research applications.

### Academic Research Centers

#### Stanford HAI (Human-Centered AI)
**Research Areas**:
- Multi-modal knowledge graphs combining text, images, and structured data
- Uncertainty quantification in graph-based retrieval
- Evaluation frameworks for graph-enhanced RAG systems

#### MIT CSAIL
**Focus Areas**:
- Causal reasoning with knowledge graphs and LLMs
- Temporal knowledge graph construction and reasoning
- Federated learning approaches for collaborative knowledge graphs

#### CMU Language Technologies Institute
**Contributions**:
- Multi-lingual knowledge graph construction
- Cross-domain knowledge transfer using graph structures
- Evaluation metrics for graph-enhanced generation quality

## Industry Landscape Analysis

### Technology Giants

#### Google (DeepMind/Research)
**Approach**: Integration with Knowledge Graph and BERT-family models
- **Lamda and PaLM integration**: Using internal knowledge graphs to enhance large language models
- **Search applications**: Graph-enhanced search and question answering
- **Research contributions**: Work on reasoning over knowledge graphs with neural models

#### Microsoft (Azure Cognitive Services)
**Product Integration**:
- **Azure Cognitive Search**: Graph-enhanced semantic search capabilities
- **Power Platform**: Knowledge graph integration for business intelligence
- **Research translation**: GraphRAG research integrated into Azure OpenAI Service

#### Amazon (AWS/Alexa)
**Infrastructure Focus**:
- **Neptune + Bedrock integration**: Managed graph database with LLM services
- **Alexa Knowledge Graph**: Conversational AI enhanced with structured knowledge
- **Enterprise solutions**: Graph-based knowledge management for AWS customers

#### OpenAI and Anthropic
**Research Directions**:
- **Retrieval-augmented training**: Using knowledge graphs during model training
- **Tool integration**: APIs enabling LLMs to query knowledge graphs
- **Safety applications**: Using knowledge graphs for fact-checking and alignment

### Enterprise Software Companies

#### Neo4j
**Product Strategy**:
- **GenAI integration**: Native LLM integration in Neo4j 5.x
- **Knowledge graph construction**: LLM-powered entity/relation extraction
- **Industry solutions**: Healthcare, finance, and fraud detection applications

#### Palantir
**Government and Enterprise Focus**:
- **Foundry platform**: Large-scale knowledge graph construction and reasoning
- **Intelligence applications**: Graph-enhanced analysis for government and corporate clients
- **Multi-source integration**: Combining structured and unstructured data in graph format

#### Databricks
**Data Lakehouse Integration**:
- **Graph analytics**: Spark-based graph processing for knowledge construction
- **MLflow integration**: Managing graph+LLM pipelines
- **Enterprise deployment**: Scalable graph-enhanced RAG for large organizations

### Specialized AI Companies

#### Primer (acquired by Palantir)
**Research Contributions**:
- **Scientific knowledge graphs**: Automatic construction from research literature
- **Multi-domain adaptation**: Transfer learning across different knowledge domains
- **Real-time updates**: Streaming knowledge graph construction and maintenance

#### Diffbot
**Web-scale Knowledge Construction**:
- **Knowledge Graph from web**: Automatic extraction from billions of web pages
- **API-driven approach**: Making structured knowledge accessible via APIs
- **LLM enhancement**: Using knowledge graphs to reduce hallucination in generated content

### Healthcare and Life Sciences

#### Epic Systems
**Electronic Health Records**:
- **Patient knowledge graphs**: Comprehensive patient data modeling
- **Clinical decision support**: Graph-enhanced diagnosis and treatment recommendations
- **Integration with medical ontologies**: SNOMED, ICD, UMLS integration

#### Tempus
**Precision Medicine**:
- **Genomic knowledge graphs**: Integrating genomic, clinical, and literature data
- **Drug discovery applications**: Graph-based target identification and validation
- **Clinical trial matching**: Using graphs to identify suitable patients for trials

### Financial Services

#### JPMorgan Chase
**Risk and Compliance**:
- **Regulatory knowledge graphs**: Modeling complex regulatory relationships
- **Fraud detection**: Graph-based pattern recognition with LLM analysis
- **Market intelligence**: News and market data integration with knowledge graphs

#### Goldman Sachs
**Investment Research**:
- **Research knowledge graphs**: Structuring investment research and market data
- **Client relationship modeling**: Graph-based client insight and recommendation systems
- **Risk assessment**: Multi-dimensional risk modeling using graph structures

## Open Source Ecosystem

### LangChain Graph Integration
**Components**:
- **Graph retrievers**: Integration with Neo4j, Amazon Neptune, ArangoDB
- **Chain templates**: Pre-built patterns for graph-enhanced RAG
- **Community contributions**: Active ecosystem of graph-specific extensions

### LlamaIndex Graph Support
**Features**:
- **Knowledge graph index**: Native support for graph-based indexing
- **Multi-modal integration**: Combining graphs with vector indexes
- **Custom retrievers**: Extensible framework for graph retrieval strategies

### Haystack Framework
**Capabilities**:
- **Graph document stores**: Support for graph-based document storage and retrieval
- **Pipeline integration**: Graph components in ML pipelines
- **Enterprise focus**: Production-ready graph+LLM applications

## Research Methodologies and Evaluation

### Benchmark Datasets

#### Complex Question Answering
- **HotpotQA**: Multi-hop reasoning benchmark adapted for graph-enhanced systems
- **ComplexWebQuestions**: Real-world complex queries requiring graph reasoning
- **KGQA benchmarks**: Knowledge graph question answering datasets

#### Domain-Specific Evaluation
- **Medical QA**: Specialized benchmarks for healthcare knowledge graphs
- **Legal reasoning**: Benchmarks for legal knowledge graph applications
- **Scientific literature**: Evaluation on scientific paper analysis and reasoning

### Evaluation Metrics
**Traditional RAG Metrics**:
- Faithfulness, relevance, context utilization
- Extended for graph-specific considerations

**Graph-Specific Metrics**:
- Graph coverage, hop distance accuracy
- Structural coherence of retrieved subgraphs
- Multi-hop reasoning accuracy

**User Experience Metrics**:
- Response time with graph queries
- Explanation quality and trustworthiness
- User satisfaction with graph-enhanced responses

## Emerging Trends and Future Directions

### 2024-2025 Research Priorities

#### Multi-Modal Knowledge Graphs
- Integration of text, images, audio, and structured data
- Cross-modal reasoning and retrieval
- Applications in robotics and autonomous systems

#### Temporal and Dynamic Graphs
- Real-time knowledge graph updates
- Temporal reasoning and prediction
- Event-driven knowledge evolution

#### Federated Knowledge Graphs
- Privacy-preserving graph construction
- Cross-organizational knowledge sharing
- Decentralized graph maintenance and updates

#### Causal Reasoning Enhancement
- Causal knowledge graph construction
- What-if scenario analysis
- Intervention planning and simulation

### Industry Adoption Patterns

#### Current Adoption Stage (2024)
- **Early adopters**: Technology companies, research institutions
- **Pilot programs**: Fortune 500 companies in healthcare, finance, legal
- **Infrastructure maturity**: Cloud providers offering managed graph+LLM services

#### Projected Adoption (2025-2026)
- **Mainstream enterprise adoption**: Knowledge graphs standard in RAG systems
- **Domain-specific solutions**: Specialized graph models for major industries
- **Regulatory frameworks**: Standards and compliance requirements for knowledge graph use

## Key Success Factors

### Technical Requirements
- **Scalability**: Handling enterprise-scale knowledge graphs
- **Performance**: Sub-second response times for complex queries
- **Accuracy**: High precision and recall for critical applications
- **Maintainability**: Automated graph construction and updates

### Organizational Factors
- **Domain expertise**: Understanding of business domain for effective modeling
- **Data governance**: Clear policies for knowledge graph construction and maintenance
- **Cross-functional collaboration**: Integration of data science, engineering, and business teams
- **Change management**: Organizational adaptation to graph-enhanced workflows

## Challenges and Limitations

### Current Research Gaps
- **Evaluation standardization**: Lack of standardized benchmarks across domains
- **Scalability bottlenecks**: Performance issues with very large knowledge graphs
- **Integration complexity**: Challenges in integrating multiple graph data sources
- **Maintenance overhead**: Keeping knowledge graphs current and accurate

### Technical Challenges
- **Query optimization**: Efficient query planning for complex graph patterns
- **Storage efficiency**: Managing large-scale graph data with embeddings
- **Real-time updates**: Maintaining consistency during continuous updates
- **Multi-tenancy**: Supporting multiple users and use cases on shared infrastructure

### Research Opportunities
- **Automated evaluation**: Self-evaluating graph-enhanced RAG systems
- **Transfer learning**: Adapting graph knowledge across domains
- **Explainable AI**: Better explanations for graph-based reasoning
- **Robustness**: Handling incomplete or inconsistent knowledge graphs

## References to Key Literature (141 citations available)

This landscape analysis draws from comprehensive research including:
- Academic papers from top-tier conferences (NeurIPS, ICML, AAAI, ACL)
- Industry research reports from major technology companies
- Open source project documentation and community contributions
- Product announcements and case studies from enterprise deployments
- Government and regulatory guidance on AI and knowledge management

The field continues evolving rapidly, with new research contributions and industry applications emerging monthly. This analysis provides a snapshot of the current state while highlighting the trajectory toward widespread enterprise adoption of graph-enhanced RAG systems."""

async def _get_technology_stacks_content() -> str:
    """Return detailed content on Frameworks & Technology Stacks."""
    return """# Frameworks & Technology Stacks

**Goal**: Survey notable frameworks, platforms, and stacks that enable hybrid graph + vector retrieval for LLMs, providing comprehensive guidance for implementation choices.

## Stack Architecture Overview

Modern GraphRAG systems typically employ a **multi-tier architecture**:

1. **Graph Database Layer**: Storage and querying of structured knowledge
2. **Vector Database Layer**: Semantic search and embedding storage
3. **LLM Integration Layer**: Language model APIs and prompt orchestration
4. **Application Framework Layer**: RAG pipeline orchestration and management
5. **API/Interface Layer**: User-facing APIs and applications

## Graph Database Technologies

### Property Graph Databases

#### Neo4j
**Strengths**:
- Most mature graph database with extensive ecosystem
- Excellent Cypher query language for pattern matching
- Native LLM integrations and GenAI toolkit
- Strong community and enterprise support
- APOC library for advanced procedures

**LLM Integration Features**:
- Built-in vector indexing for hybrid search
- Natural language to Cypher query translation
- Integration with LangChain and LlamaIndex
- Streaming APIs for real-time applications

**Use Cases**: Enterprise knowledge graphs, fraud detection, recommendation systems

**Deployment Options**: Neo4j Desktop, AuraDB (cloud), self-hosted

#### TigerGraph
**Strengths**:
- High-performance parallel processing
- Excellent for large-scale analytics
- GSQL query language optimized for complex patterns
- Strong real-time capabilities

**LLM Integration**:
- GraphStudio for visual development
- REST and streaming APIs
- Integration with cloud ML services
- Custom UDF support for embedding operations

**Use Cases**: Large-scale enterprise analytics, supply chain optimization, financial risk modeling

#### ArangoDB
**Strengths**:
- Multi-model database (graph, document, key-value)
- AQL query language supports complex operations
- Horizontal scaling capabilities
- Flexible data modeling

**LLM Integration**:
- Vector search capabilities
- Foxx microservices for custom logic
- Integration with machine learning pipelines

**Use Cases**: Multi-modal knowledge graphs, content management, IoT applications

#### Amazon Neptune
**Strengths**:
- Fully managed AWS service
- Supports both Property Graph (Gremlin) and RDF (SPARQL)
- Serverless option available
- Integration with AWS ecosystem

**LLM Integration**:
- Direct integration with Amazon Bedrock
- Vector search through OpenSearch integration
- AWS Lambda triggers for real-time processing
- SageMaker integration for ML workflows

**Use Cases**: Cloud-native applications, multi-model requirements, AWS-centric architectures

### RDF/Triple Store Databases

#### Apache Jena (Fuseki)
**Strengths**:
- Open source with strong SPARQL support
- Excellent reasoning capabilities
- Large community and extensive documentation
- ARQ query engine optimization

**LLM Integration**:
- REST APIs for application integration
- Custom functions for embedding operations
- Integration with Java-based ML libraries

**Use Cases**: Academic research, semantic web applications, standards-compliant systems

#### Stardog
**Strengths**:
- Enterprise-grade reasoning and analytics
- Excellent query optimization
- Virtual graph capabilities
- Security and governance features

**LLM Integration**:
- Machine learning integration
- Custom functions and procedures
- REST and GraphQL APIs
- Integration with enterprise ML platforms

**Use Cases**: Enterprise knowledge management, regulatory compliance, data integration

#### GraphDB (Ontotext)
**Strengths**:
- High-performance RDF database
- Excellent reasoning capabilities
- Text mining and NLP integration
- Linked data publishing tools

**LLM Integration**:
- GraphDB-LLM connector
- Text analytics workbench
- REST APIs and SPARQL endpoints
- Integration with NLP pipelines

**Use Cases**: Media and publishing, life sciences, cultural heritage

## Vector Database Technologies

### Specialized Vector Databases

#### Pinecone
**Strengths**:
- Fully managed vector database
- High-performance similarity search
- Easy scaling and management
- Excellent developer experience

**GraphRAG Integration**:
- Hybrid search capabilities
- Metadata filtering for graph constraints
- Real-time updates
- Integration with LLM frameworks

#### Weaviate
**Strengths**:
- Open source with rich feature set
- Built-in vectorization modules
- GraphQL API
- Multi-modal support (text, images)

**GraphRAG Integration**:
- Graph-like relationships between objects
- Hybrid search combining vector and graph traversal
- Custom modules for domain-specific operations
- Integration with popular ML frameworks

#### Qdrant
**Strengths**:
- High-performance Rust implementation
- Rich filtering capabilities
- Clustering and distributed deployment
- Python and REST APIs

**GraphRAG Integration**:
- Payload-based filtering for graph constraints
- Hybrid search implementations
- Integration with embedding frameworks
- Custom scoring functions

### Traditional Databases with Vector Support

#### PostgreSQL with pgvector
**Strengths**:
- Mature relational database with vector extensions
- ACID compliance and strong consistency
- Extensive ecosystem and tooling
- Cost-effective for smaller deployments

**GraphRAG Integration**:
- Combine relational and vector data in single system
- Complex queries using SQL + vector operations
- Integration with graph extensions (Apache AGE)
- Familiar tooling and administration

#### Elasticsearch/OpenSearch
**Strengths**:
- Mature search infrastructure
- Rich text analysis capabilities
- Distributed architecture
- Extensive ecosystem

**GraphRAG Integration**:
- Hybrid text and vector search
- Graph exploration capabilities
- Integration with machine learning features
- Visualization tools (Kibana/OpenSearch Dashboards)

## Application Framework Layer

### LangChain
**Components for GraphRAG**:
- **Graph retrievers**: Neo4j, Neptune, ArangoDB integration
- **Chain templates**: Pre-built graph-enhanced RAG patterns
- **Custom tools**: Graph query tools for agent applications
- **Memory systems**: Conversation memory with graph storage

**Key Features**:
```python
from langchain.graphs import Neo4jGraph
from langchain.chains import GraphCypherQAChain
from langchain.llms import OpenAI

graph = Neo4jGraph(url="bolt://localhost:7687")
chain = GraphCypherQAChain.from_llm(
    OpenAI(temperature=0),
    graph=graph,
    verbose=True
)
```

**Strengths**:
- Extensive integration ecosystem
- Active community development
- Flexible architecture
- Good documentation

### LlamaIndex
**GraphRAG Features**:
- **Knowledge Graph Index**: Native graph indexing and querying
- **Composable indices**: Combine vector and graph indexes
- **Query engines**: Sophisticated graph query orchestration
- **Data connectors**: Integration with multiple data sources

**Key Components**:
```python
from llama_index import KnowledgeGraphIndex, LLMPredictor, ServiceContext

service_context = ServiceContext.from_defaults(
    llm_predictor=LLMPredictor(llm=OpenAI())
)
index = KnowledgeGraphIndex.from_documents(
    documents,
    service_context=service_context
)
```

**Strengths**:
- Native graph support
- Sophisticated indexing strategies
- Enterprise focus
- Good performance optimization

### Haystack
**Graph Capabilities**:
- **Graph Document Stores**: Neo4j and other graph database integration
- **Graph Retrievers**: Specialized retrieval components
- **Pipeline Integration**: Graph components in ML pipelines
- **Custom Nodes**: Extensible architecture for graph operations

**Enterprise Features**:
- Production-ready deployment tools
- Model management and versioning
- Monitoring and analytics
- Security and access control

### Custom Framework Development

#### FastAPI + Graph Database
**Architecture Pattern**:
```python
from fastapi import FastAPI
from neo4j import GraphDatabase
import openai

app = FastAPI()

class GraphRAGService:
    def __init__(self, graph_uri, openai_key):
        self.driver = GraphDatabase.driver(graph_uri)
        openai.api_key = openai_key

    async def query(self, question: str):
        # Graph retrieval
        graph_context = self.retrieve_from_graph(question)

        # LLM generation
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Use the graph context to answer"},
                {"role": "user", "content": f"Context: {graph_context}\n\nQuestion: {question}"}
            ]
        )
        return response.choices[0].message.content
```

**Advantages**:
- Full control over architecture
- Optimized for specific use cases
- Direct database integration
- Custom caching and optimization

## Cloud Platform Integration

### AWS Stack
**Core Services**:
- **Amazon Neptune**: Managed graph database
- **Amazon Bedrock**: LLM services
- **Amazon OpenSearch**: Vector search
- **AWS Lambda**: Serverless processing
- **Amazon SageMaker**: ML model management

**Integration Pattern**:
- Neptune for knowledge graphs
- Bedrock for LLM inference
- OpenSearch for vector similarity
- Lambda for query orchestration
- SageMaker for custom model training

### Azure Stack
**Core Services**:
- **Azure Cosmos DB**: Graph database (Gremlin API)
- **Azure OpenAI Service**: LLM integration
- **Azure AI Search**: Hybrid search capabilities
- **Azure Functions**: Serverless processing
- **Azure Machine Learning**: Model management

**Integration Benefits**:
- Unified identity and access management
- Native Azure OpenAI integration
- Enterprise security and compliance
- Integrated monitoring and analytics

### Google Cloud Stack
**Core Services**:
- **Neo4j on GCP**: Managed Neo4j offering
- **Vertex AI**: LLM and ML services
- **Vector Search**: Managed vector database
- **Cloud Functions**: Serverless processing
- **BigQuery**: Analytics and data warehousing

**Integration Features**:
- BigQuery ML for graph analytics
- Vertex AI pipelines for ML workflows
- Cloud SQL for hybrid architectures
- GKE for containerized deployments

## Deployment Architecture Patterns

### Microservices Architecture
**Components**:
- **Graph Service**: Neo4j/Neptune with query API
- **Vector Service**: Pinecone/Weaviate with search API
- **LLM Service**: OpenAI/Bedrock with generation API
- **Orchestration Service**: LangChain/custom with RAG logic
- **API Gateway**: Request routing and authentication

**Benefits**:
- Independent scaling
- Technology flexibility
- Fault isolation
- Development team autonomy

### Monolithic Architecture
**Components**:
- Single application with embedded databases
- Combined graph and vector storage
- Integrated LLM client
- Unified API endpoint

**Benefits**:
- Simpler deployment
- Lower operational overhead
- Easier debugging and testing
- Suitable for smaller applications

### Serverless Architecture
**Components**:
- AWS Lambda/Azure Functions for compute
- Managed databases (Neptune, Cosmos DB)
- API Gateway for request handling
- Event-driven processing

**Benefits**:
- Pay-per-use pricing
- Automatic scaling
- Reduced operational overhead
- High availability

## Performance Optimization Strategies

### Caching Layers
**Graph Query Caching**:
- Redis for frequent subgraph results
- Application-level caching for common patterns
- CDN for static graph data

**Embedding Caching**:
- Vector cache for expensive computations
- Precomputed embeddings for common entities
- Batch processing for efficiency

### Database Optimization
**Graph Database Tuning**:
- Index optimization for frequent query patterns
- Query plan optimization
- Connection pooling and management
- Read replicas for scaling

**Vector Database Optimization**:
- Index configuration for accuracy/speed tradeoff
- Quantization for memory efficiency
- Sharding strategies for large datasets

## Technology Selection Guidelines

### Choose Neo4j + Pinecone When:
- Need mature, proven technology stack
- Rich graph relationships with fast traversal
- Enterprise support requirements
- Team familiar with property graphs

### Choose Neptune + Bedrock When:
- AWS-centric architecture
- Need both RDF and property graph support
- Serverless/managed service preference
- Integration with AWS AI services

### Choose Custom Stack When:
- Specific performance requirements
- Unique domain constraints
- Budget constraints for managed services
- Need full control over architecture

### Choose Open Source Stack When:
- Cost optimization priority
- On-premises deployment requirements
- Customization needs
- Vendor independence preference

## Development and Operations Tools

### Development Tools
- **Graph visualization**: Neo4j Browser, Cypher Shell
- **Vector analysis**: Jupyter notebooks, Weights & Biases
- **API testing**: Postman, curl, custom test suites
- **Performance profiling**: Application-specific tools

### Monitoring and Operations
- **Database monitoring**: Native monitoring tools, Prometheus
- **Application monitoring**: Datadog, New Relic, custom dashboards
- **Cost monitoring**: Cloud provider cost tools
- **Security monitoring**: SIEM integration, audit logging

## Implementation Roadmap

### Phase 1: Proof of Concept (2-4 weeks)
1. Choose simple stack (Neo4j + OpenAI + LangChain)
2. Implement basic entity extraction and graph construction
3. Build simple query interface
4. Validate concept with domain experts

### Phase 2: MVP Development (1-2 months)
1. Add vector search capabilities
2. Implement hybrid retrieval strategies
3. Add evaluation framework
4. Deploy to staging environment

### Phase 3: Production Deployment (2-3 months)
1. Optimize performance and scaling
2. Add monitoring and alerting
3. Implement security measures
4. Deploy to production with gradual rollout

### Phase 4: Enhancement (Ongoing)
1. Advanced retrieval strategies
2. Domain-specific optimizations
3. User experience improvements
4. Integration with additional data sources

This comprehensive technology stack analysis provides the foundation for making informed decisions about GraphRAG system architecture and implementation approach."""

async def _get_pattern_catalog_content() -> str:
    """Return detailed content on Pattern Catalog Synthesis."""
    return """# Pattern Catalog Synthesis

**Goal**: Provide a consolidated design pattern handbook for LLM-centric graph-augmented retrieval, synthesizing all findings into actionable patterns and implementation guidance.

## Pattern Classification Framework

Patterns are organized across three primary dimensions:

1. **Construction Patterns**: How to build knowledge graphs for LLM reasoning
2. **Embedding Patterns**: How to integrate semantic and structural representations
3. **Retrieval Patterns**: How to orchestrate graph+vector search for optimal results

Each pattern includes:
- **Intent**: What problem does this pattern solve?
- **Motivation**: Why is this pattern needed?
- **Structure**: How is the pattern organized?
- **Implementation**: How to implement this pattern?
- **Consequences**: What are the trade-offs?
- **Related Patterns**: How does this pattern relate to others?

## Construction Pattern Catalog

### Pattern C1: LLM-Assisted Entity-Relation Extraction
**Intent**: Create structured knowledge graphs from unstructured text using LLMs for entity and relation identification.

**Motivation**: Manual knowledge graph construction is time-consuming and doesn't scale. LLMs can automate extraction while maintaining semantic understanding.

**Structure**:
```
Input Text → Entity Extraction → Relation Extraction → Ontology Alignment → Graph Assembly
```

**Implementation**:
1. **Multi-pass extraction**: First pass for entities, second pass for relations
2. **Few-shot prompting**: Use domain-specific examples for consistency
3. **Confidence scoring**: LLM assigns confidence to extracted facts
4. **Human-in-the-loop validation**: Review and correct high-impact extractions

**Consequences**:
- *Advantages*: Scalable, maintains semantic understanding, adaptable to domains
- *Disadvantages*: May introduce LLM biases, requires quality validation

**Related Patterns**: Works with Provenance Layering (C4), enables Hybrid Symbolic-Vector (C6)

### Pattern C2: Event Reification
**Intent**: Represent complex multi-entity events as first-class graph nodes rather than trying to decompose into binary relations.

**Motivation**: Many real-world facts involve more than two entities. Binary relations lose important context and require complex reconstruction.

**Structure**:
```
Event Description → Event Node Creation → Role-based Edge Assignment → Temporal/Contextual Attributes
```

**Implementation**:
1. **Event detection**: Identify text spans describing complex events
2. **Event typing**: Classify events using domain ontologies
3. **Role assignment**: Create typed edges for each participant
4. **Provenance attachment**: Link to source text and extraction confidence

**Consequences**:
- *Advantages*: Preserves complete context, natural for complex domains
- *Disadvantages*: More complex graph structure, requires domain expertise

**Related Patterns**: Often combined with Temporal Modeling (C5), supports Multi-hop Retrieval (R4)

### Pattern C3: Layered Graph Architecture
**Intent**: Organize knowledge graphs in hierarchical layers separating different abstraction levels or data sources.

**Motivation**: Different data sources have different reliability, granularity, and update frequencies. Layered architecture enables appropriate handling of each.

**Structure**:
```
Layer 1: Raw/Source Data → Layer 2: Processed/Normalized → Layer 3: Canonical/Ontological
```

**Implementation**:
1. **Layer design**: Define clear responsibilities for each layer
2. **Cross-layer mapping**: Create links between corresponding entities
3. **Update propagation**: Design mechanisms for layer synchronization
4. **Query routing**: Determine which layers to query for different use cases

**Consequences**:
- *Advantages*: Clean separation of concerns, enables different update strategies
- *Disadvantages*: Added complexity, potential synchronization issues

**Related Patterns**: Enables Global-First Retrieval (R1), supports Technology Stack patterns

### Pattern C4: Provenance and Evidence Layering
**Intent**: Augment graph nodes and edges with detailed provenance information and supporting evidence.

**Motivation**: For critical applications, it's essential to trace where information came from and assess its reliability.

**Structure**:
```
Core Graph + Provenance Metadata + Evidence Nodes + Confidence Scores
```

**Implementation**:
1. **Source tracking**: Record extraction source for every fact
2. **Evidence linking**: Connect claims to supporting evidence nodes
3. **Confidence propagation**: Aggregate confidence across evidence chains
4. **Audit trails**: Maintain complete history of fact updates

**Consequences**:
- *Advantages*: Enables trust and verification, supports fact-checking
- *Disadvantages*: Significantly increases graph complexity and size

**Related Patterns**: Critical for Constraint-Guided Retrieval (R6), enables explainable AI

### Pattern C5: Temporal and Episodic Modeling
**Intent**: Capture time-based relationships and state changes as explicit graph structures.

**Motivation**: Many domains require understanding of how relationships and states change over time.

**Structure**:
```
Temporal Nodes + State Transition Edges + Episode Boundaries + Temporal Constraints
```

**Implementation**:
1. **Time stamping**: Add temporal attributes to nodes and edges
2. **State modeling**: Create nodes for different states of entities
3. **Transition tracking**: Model state changes as explicit edges
4. **Episode segmentation**: Group related temporal events

**Consequences**:
- *Advantages*: Enables temporal reasoning, supports predictive queries
- *Disadvantages*: Complex modeling, challenging query optimization

**Related Patterns**: Enables Temporal Retrieval (R5), works with Event Reification (C2)

### Pattern C6: Hybrid Symbolic-Vector Integration
**Intent**: Integrate neural embedding representations directly into graph structure alongside symbolic relationships.

**Motivation**: Combine the precision of symbolic reasoning with the flexibility of neural representations.

**Structure**:
```
Traditional Graph + Embedding Properties + Vector Similarity Edges + Hybrid Query Interface
```

**Implementation**:
1. **Dual representation**: Store both symbolic and vector representations
2. **Embedding computation**: Generate embeddings for nodes, edges, and subgraphs
3. **Similarity indexing**: Create vector indexes for fast similarity search
4. **Hybrid querying**: Combine structural traversal with vector similarity

**Consequences**:
- *Advantages*: Best of both worlds, handles both precise and fuzzy queries
- *Disadvantages*: High storage overhead, complex query planning

**Related Patterns**: Foundation for all Embedding Patterns (E1-E5), enables Hybrid Retrieval (R3)

## Embedding Pattern Catalog

### Pattern E1: Semantic-Structural Node Fusion
**Intent**: Combine textual semantic embeddings with graph structural embeddings for comprehensive node representation.

**Motivation**: Pure semantic embeddings miss structural context, while pure structural embeddings miss content meaning.

**Structure**:
```
Text Content → Semantic Embedding
Graph Position → Structural Embedding  } → Fused Node Embedding
Domain Features → Feature Embedding
```

**Implementation**:
1. **Multi-encoder approach**: Separate encoders for text, structure, features
2. **Fusion strategies**: Concatenation, weighted averaging, or learned fusion
3. **Dimensionality management**: Balance between expressiveness and efficiency
4. **Update strategies**: Incremental updates vs. batch recomputation

**Consequences**:
- *Advantages*: Rich node representations, supports diverse query types
- *Disadvantages*: Higher computational cost, more complex optimization

**Related Patterns**: Foundation for Local-First Retrieval (R2), enables analogical reasoning

### Pattern E2: Contextual Edge Embeddings
**Intent**: Create embeddings for relationships that incorporate both the relation type and the context of connected entities.

**Motivation**: Generic relation embeddings miss important contextual nuances that affect relationship semantics.

**Structure**:
```
Relation Type + Source Node Context + Target Node Context → Contextual Edge Embedding
```

**Implementation**:
1. **Context aggregation**: Summarize neighborhood information for each node
2. **Relation-specific encoding**: Different encoders for different relation types
3. **Triplet modeling**: Encode entire (subject, predicate, object) as unit
4. **Dynamic updates**: Re-compute embeddings when context changes

**Consequences**:
- *Advantages*: More precise relationship understanding, better fact retrieval
- *Disadvantages*: Expensive computation, storage overhead

**Related Patterns**: Supports Query Decomposition (R4), enables fact verification

### Pattern E3: Multi-hop Path Embeddings
**Intent**: Represent paths and metapaths through the graph as embeddings that capture sequential relationship patterns.

**Motivation**: Many queries require understanding of indirect relationships and connection patterns between entities.

**Structure**:
```
Path Sequence → Sequential Encoding → Path Type Classification → Path Embedding
```

**Implementation**:
1. **Path extraction**: Enumerate meaningful paths up to k hops
2. **Sequential modeling**: Use RNNs, Transformers, or graph neural networks
3. **Path typing**: Classify paths by their semantic meaning
4. **Retrieval indexing**: Index paths for similarity search

**Consequences**:
- *Advantages*: Captures indirect relationships, supports complex reasoning
- *Disadvantages*: Exponential path growth, complex pattern matching

**Related Patterns**: Essential for Multi-hop Retrieval (R4), supports analogical reasoning

### Pattern E4: Subgraph Context Embeddings
**Intent**: Create embeddings for entire subgraphs or communities that capture collective semantic meaning.

**Motivation**: Some queries are best answered by considering entire contexts rather than individual nodes or edges.

**Structure**:
```
Subgraph Identification → Content Aggregation → Community Detection → Subgraph Embedding
```

**Implementation**:
1. **Boundary detection**: Determine meaningful subgraph boundaries
2. **Content aggregation**: Summarize textual content within subgraph
3. **Structural encoding**: Capture internal connectivity patterns
4. **Hierarchical organization**: Embed subgraphs at multiple scales

**Consequences**:
- *Advantages*: Rich contextual understanding, supports evidence bundling
- *Disadvantages*: Computational complexity, boundary sensitivity

**Related Patterns**: Enables Global-First Retrieval (R1), supports evidence-based reasoning

### Pattern E5: Multi-Modal Fusion
**Intent**: Integrate embeddings from different modalities (text, images, structured data) into unified representations.

**Motivation**: Real-world knowledge often spans multiple modalities that need to be reasoned about jointly.

**Structure**:
```
Text Embeddings + Image Embeddings + Structured Features → Multi-Modal Fusion → Unified Embedding
```

**Implementation**:
1. **Modality encoders**: Specialized encoders for each data type
2. **Alignment strategies**: Learn correspondences between modalities
3. **Fusion architectures**: Attention, concatenation, or learned fusion
4. **Cross-modal retrieval**: Enable queries across different modalities

**Consequences**:
- *Advantages*: Comprehensive understanding, supports diverse applications
- *Disadvantages*: High complexity, requires multi-modal training data

**Related Patterns**: Extends all other embedding patterns, enables rich applications

## Retrieval Pattern Catalog

### Pattern R1: Global-First (Top-Down) Retrieval
**Intent**: Start retrieval with high-level context or community-level information before drilling down to specifics.

**Motivation**: Some queries benefit from understanding the broader context before focusing on specific details.

**Structure**:
```
Query → Global Context Identification → Relevant Community Selection → Local Detail Retrieval
```

**Implementation**:
1. **Hierarchical indexing**: Pre-compute hierarchical summaries
2. **Community detection**: Use graph clustering algorithms
3. **Context matching**: Match queries to relevant global contexts
4. **Progressive refinement**: Iteratively narrow focus based on relevance

**Consequences**:
- *Advantages*: Good for exploratory queries, provides context
- *Disadvantages*: May miss specific details, requires good hierarchical organization

**Related Patterns**: Works well with Layered Architecture (C3), complements Local-First (R2)

### Pattern R2: Local-First (Bottom-Up) Retrieval
**Intent**: Begin with specific entities mentioned in query and explore outward through graph connections.

**Motivation**: Many queries are about specific entities and their immediate relationships.

**Structure**:
```
Query → Entity Linking → Seed Node Identification → Neighborhood Expansion → Context Assembly
```

**Implementation**:
1. **Entity recognition**: Extract and link entities from query
2. **Seed selection**: Choose most relevant entities as starting points
3. **Expansion strategies**: BFS, DFS, or relevance-guided exploration
4. **Stopping criteria**: Define when to stop expansion

**Consequences**:
- *Advantages*: Precise and focused, good for specific queries
- *Disadvantages*: May miss broader context, can get trapped in local clusters

**Related Patterns**: Complements Global-First (R1), benefits from Node Embeddings (E1)

### Pattern R3: U-Shaped (Hybrid) Retrieval
**Intent**: Combine global and local approaches in a two-phase process for comprehensive coverage.

**Motivation**: Complex queries often require both broad context and specific details.

**Structure**:
```
Phase 1: Global Context → Phase 2: Local Detail → Integration → Response Generation
```

**Implementation**:
1. **Coarse retrieval**: Get broad context using global methods
2. **Fine retrieval**: Get specific details using local methods
3. **Integration strategies**: Merge results with appropriate weighting
4. **Iterative refinement**: Multiple rounds if initial results insufficient

**Consequences**:
- *Advantages*: Comprehensive coverage, handles complex queries
- *Disadvantages*: Higher latency, more complex orchestration

**Related Patterns**: Combines R1 and R2, works well with Layered Architecture (C3)

### Pattern R4: Query Decomposition and Multi-Hop
**Intent**: Break complex queries into simpler sub-queries that can be executed sequentially or in parallel.

**Motivation**: Complex queries often require multiple retrieval steps with intermediate reasoning.

**Structure**:
```
Complex Query → Sub-query Generation → Parallel/Sequential Execution → Result Integration
```

**Implementation**:
1. **Query analysis**: Parse query to identify multiple requirements
2. **Decomposition strategies**: Use LLM or rule-based approaches
3. **Execution planning**: Determine optimal order and parallelization
4. **Result synthesis**: Combine partial results into final answer

**Consequences**:
- *Advantages*: Handles complex queries, enables parallel processing
- *Disadvantages*: Increased complexity, potential error propagation

**Related Patterns**: Benefits from Path Embeddings (E3), enables sophisticated reasoning

### Pattern R5: Temporal and Predictive Retrieval
**Intent**: Incorporate temporal reasoning and prediction based on historical patterns in the graph.

**Motivation**: Many queries involve time-based reasoning about past, present, or future states.

**Structure**:
```
Temporal Query → Time-based Filtering → Pattern Matching → Prediction/Extrapolation
```

**Implementation**:
1. **Temporal indexing**: Index graph by time dimensions
2. **Pattern recognition**: Identify recurring temporal patterns
3. **Sequence modeling**: Use time-series or sequence models
4. **Confidence estimation**: Provide uncertainty estimates for predictions

**Consequences**:
- *Advantages*: Enables time-based reasoning, supports prediction
- *Disadvantages*: Requires temporal data, complex pattern recognition

**Related Patterns**: Requires Temporal Modeling (C5), benefits from Path Embeddings (E3)

### Pattern R6: Constraint-Guided Hybrid Filtering
**Intent**: Apply explicit constraints to narrow search space before applying neural ranking and selection.

**Motivation**: Combining symbolic constraints with neural retrieval improves precision and reduces hallucination.

**Structure**:
```
Query + Constraints → Symbolic Filtering → Neural Ranking → Constraint Validation → Results
```

**Implementation**:
1. **Constraint extraction**: Identify explicit constraints from query
2. **Symbolic filtering**: Apply hard constraints to reduce candidate set
3. **Neural ranking**: Use embedding similarity for relevance ranking
4. **Post-validation**: Verify results meet all constraints

**Consequences**:
- *Advantages*: High precision, reduced hallucination, handles complex constraints
- *Disadvantages*: Requires constraint modeling, may miss relevant results

**Related Patterns**: Benefits from Provenance Layering (C4), works with all embedding patterns

## Integration and Orchestration Patterns

### Pattern I1: Adaptive Strategy Selection
**Intent**: Dynamically choose the most appropriate retrieval strategy based on query characteristics.

**Implementation**:
- Query classification models
- Strategy performance profiling
- Dynamic routing based on query types
- Fallback mechanisms for strategy failures

### Pattern I2: Multi-Strategy Ensemble
**Intent**: Run multiple retrieval strategies in parallel and combine results for improved coverage and accuracy.

**Implementation**:
- Parallel strategy execution
- Result scoring and ranking
- Diversity-based combination
- Confidence-weighted voting

### Pattern I3: Iterative Refinement
**Intent**: Use initial results to refine queries and improve subsequent retrieval iterations.

**Implementation**:
- Result quality assessment
- Query expansion based on initial results
- Progressive focus narrowing
- Stopping criteria based on improvement

## Domain-Specific Pattern Applications

### Healthcare Domain Specializations
- **Clinical Event Modeling**: Specialized Event Reification for medical procedures
- **Patient Timeline Analysis**: Temporal patterns for disease progression
- **Evidence-Based Medicine**: Provenance patterns for clinical evidence
- **Multi-modal Health Records**: Integration of text, images, and structured data

### Financial Services Specializations
- **Risk Network Modeling**: Graph patterns for interconnected financial risks
- **Regulatory Compliance**: Constraint patterns for regulatory requirements
- **Market Intelligence**: Temporal patterns for market trend analysis
- **Fraud Detection**: Pattern recognition for fraudulent relationship networks

### Enterprise Knowledge Management
- **Organizational Knowledge**: Layered patterns for different knowledge types
- **Project Relationship Modeling**: Complex project interdependency graphs
- **Expertise Discovery**: People and skill relationship modeling
- **Institutional Memory**: Temporal patterns for knowledge evolution

## Pattern Selection Guidelines

### Query Complexity Assessment
- **Simple Entity Queries**: Use Local-First Retrieval (R2) with Node Embeddings (E1)
- **Exploratory Queries**: Use Global-First Retrieval (R1) with Subgraph Embeddings (E4)
- **Complex Multi-hop**: Use Query Decomposition (R4) with Path Embeddings (E3)
- **Time-based Queries**: Use Temporal Retrieval (R5) with Temporal Modeling (C5)
- **Constrained Queries**: Use Constraint-Guided Filtering (R6) with appropriate construction patterns

### Domain Requirements Assessment
- **High Precision Needs**: Emphasize Provenance Layering (C4) and Constraint Filtering (R6)
- **Scalability Requirements**: Use Layered Architecture (C3) with appropriate caching strategies
- **Real-time Updates**: Design for incremental updates with Hybrid Integration (C6)
- **Explainability Needs**: Implement Provenance patterns and evidence tracking

### Technology Constraint Assessment
- **Limited Resources**: Focus on simpler patterns with proven implementations
- **High Performance Needs**: Use optimized embedding strategies and caching patterns
- **Integration Requirements**: Choose patterns compatible with existing technology stack
- **Maintenance Considerations**: Select patterns matching team expertise and operational capabilities

## Implementation Roadmap

### Phase 1: Foundation (Weeks 1-4)
1. Choose core construction pattern (typically C1: LLM-Assisted Extraction)
2. Implement basic retrieval pattern (R2: Local-First)
3. Add simple embedding strategy (E1: Node Embeddings)
4. Validate with domain experts

### Phase 2: Enhancement (Weeks 5-12)
1. Add complementary retrieval strategy (R1 or R3)
2. Implement additional embedding patterns based on query types
3. Add basic provenance tracking (C4)
4. Optimize performance and add caching

### Phase 3: Sophistication (Weeks 13-24)
1. Implement advanced patterns based on specific needs
2. Add multi-strategy orchestration
3. Implement domain-specific specializations
4. Add comprehensive evaluation and monitoring

### Phase 4: Production Optimization (Ongoing)
1. Performance tuning and scaling optimization
2. Advanced pattern combinations
3. User experience refinements
4. Continuous improvement based on usage patterns

This pattern catalog provides a comprehensive framework for designing, implementing, and evolving GraphRAG systems. Each pattern can be implemented independently and combined with others to create sophisticated knowledge retrieval systems tailored to specific domains and requirements."""

async def _get_construction_pattern_detail(uri: str) -> str:
    pattern_map = {
        "graphrag://patterns/llm-assisted-extraction": "# LLM-Assisted Entity & Relation Graphs\n\n[Detailed pattern implementation...]",
        "graphrag://patterns/event-reification": "# Event Reification Pattern\n\n[Detailed n-ary relations implementation...]",
        "graphrag://patterns/layered-graphs": "# Layered Graphs Pattern\n\n[Detailed multi-tier integration...]",
        "graphrag://patterns/provenance-evidence": "# Provenance & Evidence Layering\n\n[Detailed provenance tracking...]",
        "graphrag://patterns/temporal-episodic": "# Temporal & Episodic Graphs\n\n[Detailed temporal modeling...]",
        "graphrag://patterns/hybrid-symbolic-vector": "# Hybrid Symbolic-Vector Graphs\n\n[Detailed hybrid integration...]",
    }
    return pattern_map.get(uri, f"Pattern detail not found for {uri}")

async def _get_embedding_strategy_detail(uri: str) -> str:
    strategy_map = {
        "graphrag://embeddings/node-embeddings": "# Node Embeddings: Semantic + Structural\n\n[Detailed node embedding strategy...]",
        "graphrag://embeddings/edge-relation-embeddings": "# Edge and Relation Embeddings\n\n[Detailed edge embedding strategy...]",
        "graphrag://embeddings/path-metapath-embeddings": "# Path and Metapath Embeddings\n\n[Detailed path embedding strategy...]",
        "graphrag://embeddings/subgraph-community-embeddings": "# Subgraph or Community Embeddings\n\n[Detailed subgraph embedding strategy...]",
        "graphrag://embeddings/joint-representation-fusion": "# Joint Representation & Fusion Techniques\n\n[Detailed fusion strategy...]",
    }
    return strategy_map.get(uri, f"Embedding strategy detail not found for {uri}")

async def _get_retrieval_strategy_detail(uri: str) -> str:
    retrieval_map = {
        "graphrag://retrieval/global-first": "# Global-First Retrieval (Top-Down Overview)\n\n[Detailed global-first implementation...]",
        "graphrag://retrieval/local-first": "# Local-First Retrieval (Bottom-Up Expansion)\n\n[Detailed local-first implementation...]",
        "graphrag://retrieval/u-shaped-hybrid": "# Hybrid or U-shaped Retrieval\n\n[Detailed U-shaped implementation...]",
        "graphrag://retrieval/query-rewriting-decomposition": "# Query Rewriting & Decomposition\n\n[Detailed decomposition implementation...]",
        "graphrag://retrieval/temporal-predictive": "# Temporal and Predictive Retrieval\n\n[Detailed temporal implementation...]",
        "graphrag://retrieval/constraint-guided-filtering": "# Constraint-Guided Filtering\n\n[Detailed constraint filtering implementation...]",
    }
    return retrieval_map.get(uri, f"Retrieval strategy detail not found for {uri}")


@server.list_prompts()
async def handle_list_prompts() -> list[types.Prompt]:
    """List available GraphRAG prompts for different use cases."""
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


@server.get_prompt()
async def handle_get_prompt(name: str, arguments: dict[str, str]) -> types.GetPromptResult:
    """Generate prompts for GraphRAG analysis and implementation."""

    if name == "analyze-graphrag-pattern":
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

    elif name == "design-knowledge-graph":
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

    elif name == "implement-retrieval-strategy":
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

    elif name == "compare-architectures":
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

    else:
        raise ValueError(f"Unknown prompt: {name}")


async def main():
    # Run the server using stdin/stdout streams
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="graphrag-mcp",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())