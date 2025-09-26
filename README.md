# GraphRAG MCP Server

A comprehensive Model Context Protocol (MCP) server providing structured access to knowledge about **Knowledge Graph Construction & Retrieval Strategies for LLM Reasoning**. This server enables AI agents to access detailed research findings, implementation patterns, and best practices for building graph-enhanced retrieval-augmented generation systems.

## 🎯 What This Server Provides

This MCP server offers hierarchical access to 59 pages of comprehensive research covering:

- **7 Knowledge Graph Construction Patterns** for LLM reasoning
- **5 Embedding Fusion Strategies** combining semantic and structural representations
- **6 Retrieval & Search Strategies** for graph+vector hybrid systems
- **Architectural Trade-offs** analysis (LPG, RDF/OWL, hypergraphs, factor graphs)
- **Recent Research & Industry Landscape** (2022-present)
- **Technology Stacks & Frameworks** survey
- **Consolidated Pattern Catalog** with implementation guidance

The server organizes knowledge into **3 hierarchical levels**:
1. **Overview** - High-level summaries and abstracts
2. **Main Knowledge Areas** - Detailed coverage of each topic
3. **Specific Techniques** - Implementation details for individual patterns

## 📁 Project Structure

```
graphragmcp/
├── README.md                    # This file
├── requirements.txt            # Python dependencies
├── environment.yml            # Conda environment specification
├── setup.py                   # Python package setup
├── .gitignore                # Git ignore rules
├── src/
│   ├── main.py              # Main entry point (new modular architecture)
│   ├── server.py            # Legacy monolithic server (for compatibility)
│   └── graphrag_mcp/        # Modular architecture package
│       ├── __init__.py      # Package exports
│       ├── server.py        # Main server class
│       ├── config.py        # Configuration management
│       ├── resources/       # Resource management
│       │   ├── __init__.py
│       │   ├── definitions.py  # Resource definitions
│       │   └── registry.py     # Resource registry
│       ├── prompts/         # Prompt management
│       │   ├── __init__.py
│       │   ├── definitions.py  # Prompt definitions
│       │   ├── registry.py     # Prompt registry
│       │   └── generators.py   # Prompt generators
│       ├── content/         # Content generation
│       │   ├── __init__.py
│       │   └── loader.py       # Content loader from original
│       └── utils/           # Utilities and exceptions
│           ├── __init__.py
│           └── exceptions.py   # Custom exceptions
├── agents/
│   └── graphrag_specialist.md  # Specialized GraphRAG agent for Claude Code
├── docs/
│   └── Knowledge Graph Construction & Retrieval Strategies for LLM Reasoning.pdf
├── examples/
│   ├── test_client.py        # Test client to verify server functionality
│   ├── claude_desktop_config.json  # Configuration for Claude Desktop
│   └── .claude/agents/      # Example Claude Code project structure
│       └── graphrag_specialist.md  # Agent configuration example
└── tests/                    # Future test files
```

## 🚀 Quick Start

### Option 1: Using uv (Recommended - Modern Python)

1. **Install uv** (if not already installed):
   ```bash
   # macOS/Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Windows
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

   # Or with pip
   pip install uv
   ```

2. **Install and run the server**:
   ```bash
   cd graphragmcp

   # Install dependencies and run (uv handles everything)
   uv run src/main.py

   # Or install as a package and run
   uv pip install -e .
   uv run graphrag-mcp
   ```

### Option 2: Using Conda

1. **Install Conda** (if not already installed):
   - Download from [conda.io](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)
   - Or install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) for a minimal installation

2. **Create and activate the environment**:
   ```bash
   cd graphragmcp
   conda env create -f environment.yml
   conda activate graphragmcp
   ```

3. **Run the server**:
   ```bash
   # New modular architecture (recommended)
   python src/main.py

   # Or legacy server (for compatibility)
   python src/server.py
   ```

### Option 3: Using pip + venv

1. **Create a virtual environment**:
   ```bash
   cd graphragmcp
   python -m venv venv

   # Activate on macOS/Linux:
   source venv/bin/activate

   # Activate on Windows:
   venv\\Scripts\\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   # Or install as editable package
   pip install -e .
   ```

3. **Run the server**:
   ```bash
   # New modular architecture (recommended)
   python src/main.py

   # Or as installed package
   graphrag-mcp

   # Or legacy server (for compatibility)
   python src/server.py
   ```

## 🔧 Configuration

### For Claude Desktop

1. **Locate your Claude Desktop config file**:
   - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows**: `%APPDATA%\\Claude\\claude_desktop_config.json`

2. **Choose your configuration method**:

   #### Option A: Using uv (Recommended - Best compatibility)
   ```json
   {
     "mcpServers": {
       "graphrag-mcp": {
         "command": "uv",
         "args": [
           "--directory",
           "/ABSOLUTE/PATH/TO/graphragmcp",
           "run",
           "src/main.py"
         ]
       }
     }
   }
   ```

   #### Option B: Using uv with installed package
   ```json
   {
     "mcpServers": {
       "graphrag-mcp": {
         "command": "uv",
         "args": [
           "--directory",
           "/ABSOLUTE/PATH/TO/graphragmcp",
           "run",
           "graphrag-mcp"
         ]
       }
     }
   }
   ```

   #### Option C: Using Python directly
   ```json
   {
     "mcpServers": {
       "graphrag-mcp": {
         "command": "python",
         "args": ["/ABSOLUTE/PATH/TO/graphragmcp/src/main.py"]
       }
     }
   }
   ```

   #### Option D: Using Conda environment
   ```json
   {
     "mcpServers": {
       "graphrag-mcp": {
         "command": "conda",
         "args": [
           "run",
           "-n",
           "graphragmcp",
           "python",
           "/ABSOLUTE/PATH/TO/graphragmcp/src/main.py"
         ]
       }
     }
   }
   ```

   **⚠️ Important**:
   - Replace `/ABSOLUTE/PATH/TO/graphragmcp` with your actual project path
   - Use **absolute paths only** - relative paths will not work
   - For Windows, use forward slashes or escaped backslashes in paths

3. **Restart Claude Desktop** to load the server.

4. **Verify the server is working**:
   - Look for GraphRAG resources in Claude Desktop
   - Check that you can ask GraphRAG-related questions
   - If issues occur, check Claude Desktop's logs

### For Claude Code Integration

Once configured in Claude Desktop, you can import the server into Claude Code:

1. **Import from Claude Desktop** (macOS/WSL only):
   ```bash
   claude mcp add-from-claude-desktop
   ```
   Then select the `graphrag-mcp` server when prompted.

2. **Verify the import**:
   ```bash
   claude mcp list
   ```
   You should see `graphrag-mcp` in the list.

3. **Manual configuration** (if automatic import doesn't work):
   Add to your Claude Code configuration:
   ```bash
   claude mcp add graphrag-mcp --command python --args "/ABSOLUTE/PATH/TO/graphragmcp/src/main.py"
   ```

### For Other MCP Clients

The server follows the MCP standard and should work with any compatible client. Use:
- **Command**: `python`
- **Args**: `["/path/to/graphragmcp/src/main.py"]` (recommended) or `["/path/to/graphragmcp/src/server.py"]` (legacy)

## 🤖 GraphRAG Specialist Agent Integration

This project includes a **specialized GraphRAG agent** designed to work with Claude Code, providing expert-level assistance with Knowledge Graph Construction & Retrieval strategies.

### 🎯 Agent Capabilities

The GraphRAG Specialist Agent provides:

- **🗂️ Knowledge Graph Construction**: Expert guidance on LLM-assisted entity extraction, event reification, layered architectures, provenance tracking, temporal modeling, and hybrid symbolic-vector integration
- **🔗 Embedding & Representation Strategies**: Advanced techniques for node, edge, path, and subgraph embeddings with multi-modal fusion
- **🔍 Retrieval & Search Orchestration**: Implementation guidance for global-first, local-first, U-shaped hybrid, query decomposition, temporal, and constraint-guided retrieval strategies
- **🏗️ Architecture & Technology Stacks**: Comprehensive knowledge of graph databases, vector databases, frameworks, and cloud platform optimization
- **🛠️ Implementation Guidance**: Step-by-step roadmaps, code examples, performance optimization, and production deployment strategies

### 📋 Setup Instructions

#### Option 1: Using Claude Code with MCP Integration (Recommended)

1. **Configure the MCP server in Claude Desktop** (see configuration section above)

2. **Import the MCP server into Claude Code**:
   ```bash
   # Import from Claude Desktop (macOS/WSL only)
   claude mcp add-from-claude-desktop
   # Select graphrag-mcp when prompted

   # Or add manually
   claude mcp add graphrag-mcp --command python --args "/ABSOLUTE/PATH/TO/graphragmcp/src/main.py"
   ```

3. **Verify MCP server is available**:
   ```bash
   claude mcp list
   # Should show graphrag-mcp in the list
   ```

4. **Add the GraphRAG Specialist Agent**:
   ```bash
   # Create the agents directory in your project
   mkdir -p .claude/agents

   # Copy the agent configuration
   cp agents/graphrag_specialist.md .claude/agents/
   ```

   Or manually place `graphrag_specialist.md` in your project's `.claude/agents/` directory.

5. **Start using the integrated system**:
   - The agent will be automatically available in Claude Code
   - Reference it with `@graphrag-specialist` or by asking GraphRAG-related questions
   - The agent will automatically use the MCP server to provide comprehensive, research-backed answers
   - Claude Code will have direct access to all 25 GraphRAG resources and 4 specialized prompts

#### Option 2: Global Agent Installation

To make the agent available across all Claude Code projects:

1. **Install globally**:
   ```bash
   # Create global agents directory
   mkdir -p ~/.claude/agents

   # Copy the agent configuration
   cp agents/graphrag_specialist.md ~/.claude/agents/
   ```

2. **The agent will be available in all Claude Code projects**

#### Option 3: Custom Agent Configuration

If you want to customize the agent:

1. **Copy and modify the agent file**:
   ```bash
   cp agents/graphrag_specialist.md .claude/agents/my-custom-graphrag-agent.md
   ```

2. **Edit the YAML frontmatter**:
   - Change the `name` field to your custom name
   - Modify the `description` for different specialization
   - Adjust the system prompt as needed

3. **Ensure MCP server accessibility**:
   - The agent relies on the GraphRAG MCP server for detailed knowledge
   - Make sure the server is running and accessible

### 🚀 Using the GraphRAG Agent

Once configured, you can interact with the GraphRAG Specialist Agent for:

#### 🎯 Use Case Analysis
```
@graphrag-specialist I need to build a knowledge graph for a healthcare application that processes patient records and medical literature. What GraphRAG patterns should I use?
```

#### 🛠️ Implementation Guidance
```
@graphrag-specialist How do I implement a U-shaped hybrid retrieval strategy using Neo4j and Pinecone?
```

#### 📊 Architecture Decisions
```
@graphrag-specialist Should I use LPG or RDF for a financial compliance knowledge graph with 50M entities?
```

#### 🔧 Technology Stack Recommendations
```
@graphrag-specialist What's the best technology stack for a scalable GraphRAG system on AWS?
```

#### 📈 Performance Optimization
```
@graphrag-specialist How can I optimize my GraphRAG system's query performance for real-time applications?
```

### 🔄 Agent + MCP Server Workflow

The agent follows this workflow:

1. **Analyzes your question** to understand GraphRAG requirements
2. **Queries the MCP server** for relevant research and patterns
3. **Uses specialized prompts** for structured analysis
4. **Provides comprehensive recommendations** with implementation details
5. **Includes code examples** and architectural guidance
6. **Suggests evaluation metrics** and optimization strategies

### 💡 Example Interaction

**User**: "I need to implement GraphRAG for a legal document analysis system. The system needs to handle complex multi-party contracts and regulatory relationships."

**GraphRAG Agent Response**:
1. **Queries MCP server** for construction patterns and legal domain examples
2. **Uses "analyze-graphrag-pattern" prompt** with legal domain context
3. **Recommends Event Reification pattern** for multi-party relationships
4. **Suggests Neo4j + Pinecone stack** with reasoning
5. **Provides implementation roadmap** with specific phases
6. **Includes code examples** for entity extraction and relationship modeling
7. **Recommends evaluation metrics** for legal document accuracy

### 🛡️ Best Practices

- **Start with requirements analysis**: The agent will help you identify the best patterns
- **Ask for implementation details**: Get specific code examples and architectural guidance
- **Request performance considerations**: Understand scaling and optimization strategies
- **Validate recommendations**: The agent provides research-backed suggestions you can verify

## 🧪 Testing the Server

### Basic Functionality Test

Run the included test client to verify everything works:

```bash
cd examples
python test_client.py
```

This will:
- Connect to the server
- List available resources
- Read sample content from key resources
- Display available prompts

### Manual Testing

You can also test the server manually using MCP tools or by examining the server output when it starts.

## 📊 Available Resources

The server provides **27 knowledge resources** organized hierarchically:

### Level 1: Overview
- `graphrag://overview` - Comprehensive overview of GraphRAG research

### Level 2: Main Knowledge Areas
- `graphrag://construction-patterns` - 7 key construction patterns
- `graphrag://embedding-strategies` - 5 embedding fusion strategies
- `graphrag://retrieval-strategies` - 6 retrieval orchestration strategies
- `graphrag://architectural-tradeoffs` - Graph model architecture analysis
- `graphrag://literature-landscape` - Recent research & industry practice
- `graphrag://technology-stacks` - Frameworks & technology survey
- `graphrag://pattern-catalog` - Consolidated design patterns

### Level 3: Detailed Techniques
- **Construction Patterns**: LLM-assisted extraction, event reification, layered graphs, provenance layering, temporal modeling, hybrid symbolic-vector
- **Embedding Strategies**: Node embeddings, edge embeddings, path embeddings, subgraph embeddings, joint representation fusion
- **Retrieval Strategies**: Global-first, local-first, U-shaped hybrid, query decomposition, temporal retrieval, constraint-guided filtering

## 🤖 Available Prompts

The server includes **4 specialized prompts** for GraphRAG analysis:

1. **`analyze-graphrag-pattern`** - Analyze best patterns for specific use cases
2. **`design-knowledge-graph`** - Get design guidance for knowledge graphs
3. **`implement-retrieval-strategy`** - Implementation guidance for retrieval strategies
4. **`compare-architectures`** - Compare different graph architectures

## 💡 Usage Examples

### With Claude Desktop

Once configured, you can ask Claude questions like:

- "What are the main GraphRAG construction patterns and when should I use each?"
- "Compare LPG vs RDF for healthcare knowledge graphs"
- "Show me the technology stack options for implementing GraphRAG"
- "What are the recent developments in GraphRAG research?"

### Programmatic Access

```python
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def query_graphrag():
    server_params = StdioServerParameters(
        command="python",
        args=["src/server.py"]
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # Get overview
            content = await session.read_resource("graphrag://overview")
            print(content)

            # Use a prompt
            result = await session.get_prompt(
                "analyze-graphrag-pattern",
                {"use_case": "Healthcare patient records analysis"}
            )
            print(result.messages[0].content.text)

asyncio.run(query_graphrag())
```

## 🏗️ Architecture Highlights

This project features a **distinguished engineer-ready** modular architecture:

### 🔧 Modular Design
- **Separation of Concerns**: Resources, prompts, content, and configuration are cleanly separated
- **Resource Registry**: Centralized management of all knowledge resources
- **Prompt Registry**: Structured prompt management with generators
- **Content Factory**: Efficient content generation and caching
- **Configuration Management**: Centralized configuration with logging setup

### 🛡️ Robust Error Handling
- **Custom Exception Hierarchy**: Specific exceptions for different error types
- **Comprehensive Logging**: Detailed logging throughout all components
- **Graceful Degradation**: Fallback mechanisms when content loading fails
- **Input Validation**: Proper validation of resource URIs and prompt arguments

### ⚡ Performance Optimizations
- **Lazy Loading**: Content generated on-demand for efficiency
- **Registry Pattern**: Fast resource and prompt lookup
- **Content Length Limits**: Configurable limits to prevent memory issues
- **Efficient Imports**: Modular imports reduce startup time

## 🔍 Key Features

- **📚 Comprehensive Knowledge Base**: 59 pages of research distilled into structured resources
- **🏗️ Hierarchical Organization**: 3-level structure for different detail needs
- **🧠 AI-Optimized**: Designed specifically for AI agent consumption
- **⚡ Fast Access**: Efficient resource retrieval with minimal latency
- **🔄 Standard Compliant**: Full MCP protocol compliance
- **🎯 Specialized Prompts**: Domain-specific prompts for GraphRAG analysis
- **📖 Complete Fidelity**: 100% faithful to original research content
- **🔧 Enterprise-Ready**: Modular, maintainable, and extensible architecture
- **🤖 Specialized Agent**: Pre-configured GraphRAG expert agent for Claude Code integration

## 🛠️ Development

### Adding New Resources

To extend the server with additional resources:

1. **Add resource definition** in `handle_list_resources()`
2. **Implement content function** following the pattern `async def _get_content()`
3. **Add URI handling** in `handle_read_resource()`

### Testing

```bash
# Install development dependencies
pip install pytest pytest-asyncio black mypy

# Run basic server test
python examples/test_client.py

# Format code
black src/

# Type checking
mypy src/
```

## 📋 Requirements

- **Python**: 3.11+
- **Core Dependency**: `mcp>=1.0.0`
- **Optional**: Development and testing tools

## 🤝 Contributing

This server is based on comprehensive GraphRAG research. When making changes:

1. **Maintain Fidelity**: Keep content faithful to original research
2. **Follow MCP Standards**: Ensure compatibility with MCP protocol
3. **Test Thoroughly**: Verify all resources and prompts work correctly
4. **Document Changes**: Update README for any new features

## 📄 License

This project packages and structures existing research for MCP access. Please refer to the original research document for licensing and attribution requirements.

## 🆘 Troubleshooting

### Common Issues

**"Server not found" in Claude Desktop**:
- Verify the full path in your config is correct
- Ensure Python is in your PATH
- Try using absolute path to Python executable

**Import errors**:
- Ensure you've activated the correct conda environment or virtual environment
- Verify all dependencies are installed: `pip list` or `conda list`

**Server won't start**:
- Check Python version: `python --version` (should be 3.11+)
- Try running directly: `python src/main.py` or `python src/server.py`
- Check for any error messages in the terminal

**Claude Desktop not showing resources**:
- Restart Claude Desktop after config changes
- Check Claude Desktop's logs for connection errors
- Verify the server starts without errors

**Agent not working with MCP server**:
- Ensure the MCP server is running and accessible
- Verify the agent configuration file is in the correct location
- Check that Claude Code can access the MCP server configuration
- Test the MCP server independently before using with the agent

**Agent not providing detailed responses**:
- Verify the MCP server is properly configured and responding
- Check that the agent has access to all 27 knowledge resources
- Ensure the specialized prompts are working (test with MCP client)
- Try asking more specific questions about GraphRAG patterns

### Getting Help

1. **Check Error Messages**: Run the server directly to see detailed error output
2. **Test with Example Client**: Use `python examples/test_client.py` to isolate issues
3. **Verify Dependencies**: Ensure all required packages are installed
4. **Check File Paths**: Ensure all paths in configs are correct and accessible
5. **Test Agent Separately**: Try the MCP server directly before integrating with the agent

## 📈 Performance Notes

- **Resource Loading**: Resources are generated on-demand for efficiency
- **Memory Usage**: Approximately 10-20MB for the full knowledge base
- **Response Time**: Typical response times under 100ms for resource access
- **Scalability**: Designed to handle multiple concurrent client connections

---

**Built with ❤️ for the GraphRAG community**