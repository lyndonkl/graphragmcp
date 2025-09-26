"""
Tools module for GraphRAG MCP Server.

This module provides MCP tools that wrap existing resource and prompt functionality,
enabling Claude Code agents to access the knowledge base through tool calls.
"""

from .definitions import GRAPHRAG_TOOLS
from .registry import ToolRegistry

__all__ = ["GRAPHRAG_TOOLS", "ToolRegistry"]