#!/usr/bin/env python3
"""
Simple test client to demonstrate GraphRAG MCP Server functionality.

This script shows how to interact with the server and retrieve various
types of knowledge resources.
"""

import asyncio
import json
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def test_server():
    """Test the GraphRAG MCP server functionality."""

    # Connect to the server
    server_params = StdioServerParameters(
        command="python",
        args=["../src/server.py"],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize
            await session.initialize()

            # List available resources
            print("=== Available Resources ===")
            resources = await session.list_resources()
            for resource in resources:
                print(f"- {resource.name} ({resource.uri})")
                print(f"  {resource.description}")
                print()

            # Test reading a few key resources
            test_resources = [
                "graphrag://overview",
                "graphrag://construction-patterns",
                "graphrag://architectural-tradeoffs",
            ]

            for uri in test_resources:
                print(f"=== Reading {uri} ===")
                try:
                    content = await session.read_resource(uri)
                    # Show first 200 characters
                    print(content[:200] + "..." if len(content) > 200 else content)
                    print()
                except Exception as e:
                    print(f"Error reading {uri}: {e}")
                    print()

            # List available prompts
            print("=== Available Prompts ===")
            prompts = await session.list_prompts()
            for prompt in prompts:
                print(f"- {prompt.name}")
                print(f"  {prompt.description}")
                print()


if __name__ == "__main__":
    asyncio.run(test_server())