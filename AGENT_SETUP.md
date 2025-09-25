# GraphRAG Specialist Agent - Quick Setup Guide

This guide helps you quickly set up the GraphRAG Specialist Agent with Claude Code and the MCP server.

## 🚀 Quick Setup (5 minutes)

### Step 1: Start the MCP Server
```bash
# Navigate to project directory
cd /path/to/graphragmcp

# Activate environment
conda activate graphragmcp  # or source venv/bin/activate

# Start the server
python src/main.py
```

### Step 2: Configure Claude Code MCP Integration

Add this to your Claude Code MCP configuration:

```json
{
  "mcpServers": {
    "graphrag-mcp": {
      "command": "python",
      "args": ["/FULL/PATH/TO/graphragmcp/src/main.py"],
      "env": {}
    }
  }
}
```

**Replace `/FULL/PATH/TO/graphragmcp` with your actual project path!**

### Step 3: Add the GraphRAG Agent

Copy the agent configuration to your Claude Code project:
```bash
# For project-specific agent
mkdir -p .claude/agents
cp agents/graphrag_specialist.md .claude/agents/

# OR for global agent (available in all projects)
mkdir -p ~/.claude/agents
cp agents/graphrag_specialist.md ~/.claude/agents/
```

### Step 4: Test the Integration

Ask the agent a GraphRAG question in Claude Code:
```
@graphrag-specialist What GraphRAG pattern should I use for a healthcare knowledge graph with patient records and medical literature?
```

The agent should:
1. ✅ Query the MCP server for relevant research
2. ✅ Use specialized prompts for analysis
3. ✅ Provide detailed recommendations with implementation guidance
4. ✅ Include specific technology stack suggestions

## 🔍 Verification Checklist

- [ ] MCP server starts without errors
- [ ] Claude Code can connect to the MCP server
- [ ] Agent file is accessible in Claude Code
- [ ] Agent provides detailed, research-backed responses
- [ ] Agent uses MCP server resources and prompts

## ❗ Common Issues

**Agent gives generic responses**: MCP server isn't connected properly
**"Resource not found" errors**: Check MCP server configuration path
**Agent not found**: Verify agent file is in the correct location

## 🎯 Example Agent Interactions

### Use Case Analysis
**You**: `@graphrag-specialist I need to build a financial compliance knowledge graph. What patterns should I use?`

**Agent**: *Queries MCP server → Provides detailed pattern analysis → Recommends specific implementation approach*

### Implementation Guidance
**You**: `@graphrag-specialist How do I implement hybrid retrieval with Neo4j and Weaviate?`

**Agent**: *Uses specialized prompts → Provides step-by-step implementation → Includes code examples*

### Architecture Decisions
**You**: `@graphrag-specialist LPG vs RDF for 10M entity pharmaceutical knowledge graph?`

**Agent**: *Accesses architectural tradeoffs research → Compares options → Recommends specific approach with reasoning*

## 📚 What the Agent Knows

The agent has expert-level knowledge in:
- ✅ 7 Knowledge Graph Construction Patterns
- ✅ 5 Embedding Fusion Strategies
- ✅ 6 Retrieval & Search Strategies
- ✅ Architectural Trade-offs (LPG, RDF, Hypergraphs, Factor Graphs)
- ✅ Technology Stacks (Neo4j, Pinecone, LangChain, etc.)
- ✅ Recent Research & Industry Practice (2022-present)
- ✅ Complete Pattern Catalog with Implementation Guidance

**Total Knowledge Base**: 59 pages of research → 27 structured resources → 4 specialized prompts

🎉 **You now have a world-class GraphRAG expert at your fingertips!**