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
        args=["src/main.py"],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize
            await session.initialize()

            # List available resources
            print("=== Available Resources ===")
            resources_result = await session.list_resources()

            # Handle different response formats
            if hasattr(resources_result, 'resources'):
                resources = resources_result.resources
            elif isinstance(resources_result, (list, tuple)):
                resources = resources_result
            else:
                resources = [resources_result]

            for resource in resources:
                # Handle both tuple and object formats
                if hasattr(resource, 'name'):
                    print(f"- {resource.name} ({resource.uri})")
                    print(f"  {resource.description}")
                elif isinstance(resource, tuple) and len(resource) >= 3:
                    print(f"- {resource[0]} ({resource[1]})")
                    print(f"  {resource[2]}")
                else:
                    print(f"- {resource}")
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
                    result = await session.read_resource(uri)
                    # Extract content from ReadResourceResult
                    content = result.contents[0].text if hasattr(result, 'contents') and result.contents else str(result)
                    # Show first 200 characters
                    print(content[:200] + "..." if len(content) > 200 else content)
                    print()
                except Exception as e:
                    print(f"Error reading {uri}: {e}")
                    print()

            # List available prompts
            print("=== Available Prompts ===")
            prompts_result = await session.list_prompts()

            # Handle different response formats
            if hasattr(prompts_result, 'prompts'):
                prompts = prompts_result.prompts
            elif isinstance(prompts_result, (list, tuple)):
                prompts = prompts_result
            else:
                prompts = [prompts_result]

            for prompt in prompts:
                # Handle both tuple and object formats
                if hasattr(prompt, 'name'):
                    print(f"- {prompt.name}")
                    print(f"  {prompt.description}")
                elif isinstance(prompt, tuple) and len(prompt) >= 2:
                    print(f"- {prompt[0]}")
                    print(f"  {prompt[1]}")
                else:
                    print(f"- {prompt}")
                print()


if __name__ == "__main__":
    asyncio.run(test_server())