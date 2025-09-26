#!/usr/bin/env python3
"""
Comprehensive test client for GraphRAG MCP Server functionality.

This script demonstrates all MCP capabilities:
- Resources: 25 hierarchical knowledge resources
- Tools: 10 MCP tools for agent access (primary testing focus)
- Prompts: 4 specialized analysis prompts

Tests the actual functionality that Claude Code agents use.
"""

import asyncio
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

            # Test MCP tools (these work correctly and are what agents use)
            print("=== Testing MCP Tools ===")

            # Test generic resource query tool
            print("--- Testing query_graphrag_resource tool ---")
            try:
                result = await session.call_tool("query_graphrag_resource", {
                    "resource_uri": "graphrag://overview"
                })
                content = result.content[0].text if hasattr(result, 'content') else str(result)
                print(f"✅ query_graphrag_resource: {len(content)} chars")
                print(content[:200] + "..." if len(content) > 200 else content)
                print()
            except Exception as e:
                print(f"❌ Error with query_graphrag_resource: {e}")
                print()

            # Test direct knowledge access tools
            print("--- Testing direct knowledge access tools ---")
            direct_tools = [
                "get_construction_patterns",
                "get_embedding_strategies",
                "get_retrieval_strategies",
                "get_architectural_tradeoffs",
                "get_technology_stacks"
            ]

            for tool_name in direct_tools:
                try:
                    result = await session.call_tool(tool_name, {})
                    content = result.content[0].text if hasattr(result, 'content') else str(result)
                    print(f"✅ {tool_name}: {len(content)} chars")
                    print(content[:150] + "..." if len(content) > 150 else content)
                    print()
                except Exception as e:
                    print(f"❌ Error with {tool_name}: {e}")
                    print()

            # Test specialized analysis tools
            print("--- Testing specialized analysis tools ---")
            try:
                result = await session.call_tool("analyze_graphrag_pattern", {
                    "use_case": "healthcare patient records",
                    "requirements": "HIPAA compliance",
                    "data_types": "clinical notes, lab results"
                })
                content = result.content[0].text if hasattr(result, 'content') else str(result)
                print(f"✅ analyze_graphrag_pattern: {len(content)} chars")
                print(content[:200] + "..." if len(content) > 200 else content)
                print()
            except Exception as e:
                print(f"❌ Error with analyze_graphrag_pattern: {e}")
                print()

            try:
                result = await session.call_tool("compare_architectures", {
                    "use_case": "financial compliance knowledge graph",
                    "scale": "50M entities",
                    "performance_requirements": "real-time queries"
                })
                content = result.content[0].text if hasattr(result, 'content') else str(result)
                print(f"✅ compare_architectures: {len(content)} chars")
                print(content[:200] + "..." if len(content) > 200 else content)
                print()
            except Exception as e:
                print(f"❌ Error with compare_architectures: {e}")
                print()

            # List available tools
            print("=== Available Tools ===")
            tools_result = await session.list_tools()

            # Handle different response formats
            if hasattr(tools_result, 'tools'):
                tools = tools_result.tools
            elif isinstance(tools_result, (list, tuple)):
                tools = tools_result
            else:
                tools = [tools_result]

            for tool in tools:
                # Handle both tuple and object formats
                if hasattr(tool, 'name'):
                    print(f"- {tool.name}")
                    print(f"  {tool.description}")
                elif isinstance(tool, tuple) and len(tool) >= 2:
                    print(f"- {tool[0]}")
                    print(f"  {tool[1]}")
                else:
                    print(f"- {tool}")
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