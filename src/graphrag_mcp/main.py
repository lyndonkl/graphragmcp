#!/usr/bin/env python3
"""
Main entry point for the GraphRAG MCP Server.

This module provides the main function that can be used as a console script
entry point for the GraphRAG MCP server package.
"""

import asyncio
import sys
from pathlib import Path

# Add the parent directory to the path so we can import from graphrag_mcp
sys.path.insert(0, str(Path(__file__).parent.parent))

from graphrag_mcp.server import GraphRAGMCPServer
from graphrag_mcp.config import ServerConfig


def main() -> None:
    """Main entry point for the GraphRAG MCP Server."""
    asyncio.run(run_server())


async def run_server() -> None:
    """Run the GraphRAG MCP Server."""
    config = ServerConfig(
        server_name="graphrag-mcp",
        server_version="0.1.0"
    )

    server = GraphRAGMCPServer(config)
    await server.run()


if __name__ == "__main__":
    main()