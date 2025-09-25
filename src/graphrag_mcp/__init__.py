"""
GraphRAG MCP Server Package

A modular Model Context Protocol server providing comprehensive knowledge about
Knowledge Graph Construction & Retrieval Strategies for LLM Reasoning.
"""

__version__ = "0.1.0"
__author__ = "AI Assistant"
__description__ = "GraphRAG MCP Server for Knowledge Graph Construction & Retrieval Strategies"

from .server import GraphRAGMCPServer

__all__ = ["GraphRAGMCPServer"]