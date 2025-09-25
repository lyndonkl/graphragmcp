#!/usr/bin/env python3
"""
Main entry point for the GraphRAG MCP Server.

This is a clean entry point that uses the new modular architecture.
"""

import asyncio
import sys
import os

# Add the current directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from graphrag_mcp.server import GraphRAGMCPServer
from graphrag_mcp.config import ServerConfig


async def main():
    """Main entry point."""
    # Create configuration (could be loaded from environment or config file)
    config = ServerConfig(
        server_name="graphrag-mcp",
        server_version="0.1.0",
        log_level="INFO",
        enable_debug=False
    )

    # Create and run server
    server = GraphRAGMCPServer(config)
    await server.run()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Server shutdown requested")
        sys.exit(0)
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)