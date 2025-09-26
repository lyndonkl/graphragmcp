"""
Tool registry for GraphRAG MCP Server.

Manages tool registration and execution, delegating to existing resource and prompt handlers.
"""

import logging
from typing import Dict, Any, Callable, Awaitable, List
import mcp.types as types
from ..utils.exceptions import ToolNotFoundError, ToolExecutionError


logger = logging.getLogger(__name__)


class ToolRegistry:
    """Registry for MCP tools that delegate to existing resource/prompt handlers."""

    def __init__(self):
        self._tool_handlers: Dict[str, Callable[[Dict[str, Any]], Awaitable[str]]] = {}
        self._resource_handler: Callable[[str], Awaitable[str]] = None
        self._prompt_handler: Callable[[str, Dict[str, str]], Awaitable[types.GetPromptResult]] = None

    def set_resource_handler(self, handler: Callable[[str], Awaitable[str]]) -> None:
        """Set the resource handler function."""
        self._resource_handler = handler

    def set_prompt_handler(self, handler: Callable[[str, Dict[str, str]], Awaitable[types.GetPromptResult]]) -> None:
        """Set the prompt handler function."""
        self._prompt_handler = handler

    def register_tool(self, name: str, handler: Callable[[Dict[str, Any]], Awaitable[str]]) -> None:
        """Register a tool handler."""
        self._tool_handlers[name] = handler
        logger.debug(f"Registered tool: {name}")

    def register_all_tools(self) -> None:
        """Register all GraphRAG tools with their handlers."""

        # Generic resource query tool
        self.register_tool("query_graphrag_resource", self._handle_query_resource)

        # Specific resource tools
        self.register_tool("get_construction_patterns", self._handle_get_construction_patterns)
        self.register_tool("get_embedding_strategies", self._handle_get_embedding_strategies)
        self.register_tool("get_retrieval_strategies", self._handle_get_retrieval_strategies)
        self.register_tool("get_architectural_tradeoffs", self._handle_get_architectural_tradeoffs)
        self.register_tool("get_technology_stacks", self._handle_get_technology_stacks)

        # Prompt execution tools
        self.register_tool("analyze_graphrag_pattern", self._handle_analyze_pattern)
        self.register_tool("compare_architectures", self._handle_compare_architectures)
        self.register_tool("design_knowledge_graph", self._handle_design_knowledge_graph)
        self.register_tool("implement_retrieval_strategy", self._handle_implement_retrieval_strategy)

    async def execute_tool(self, name: str, arguments: Dict[str, Any]) -> str:
        """Execute a tool by name with given arguments."""
        if name not in self._tool_handlers:
            raise ToolNotFoundError(name)

        try:
            result = await self._tool_handlers[name](arguments)
            return result
        except Exception as e:
            logger.error(f"Error executing tool {name}: {e}")
            raise ToolExecutionError(name, str(e))

    def list_tools(self) -> List[str]:
        """Get list of registered tool names."""
        return list(self._tool_handlers.keys())

    # Tool handler implementations

    async def _handle_query_resource(self, arguments: Dict[str, Any]) -> str:
        """Handle generic resource query."""
        if not self._resource_handler:
            raise ToolExecutionError("query_graphrag_resource", "Resource handler not configured")

        resource_uri = arguments.get("resource_uri", "")
        if not resource_uri:
            raise ToolExecutionError("query_graphrag_resource", "resource_uri is required")

        return await self._resource_handler(resource_uri)

    async def _handle_get_construction_patterns(self, arguments: Dict[str, Any]) -> str:
        """Handle construction patterns query."""
        _ = arguments  # Arguments not used for this tool
        if not self._resource_handler:
            raise ToolExecutionError("get_construction_patterns", "Resource handler not configured")
        return await self._resource_handler("graphrag://construction-patterns")

    async def _handle_get_embedding_strategies(self, arguments: Dict[str, Any]) -> str:
        """Handle embedding strategies query."""
        _ = arguments  # Arguments not used for this tool
        if not self._resource_handler:
            raise ToolExecutionError("get_embedding_strategies", "Resource handler not configured")
        return await self._resource_handler("graphrag://embedding-strategies")

    async def _handle_get_retrieval_strategies(self, arguments: Dict[str, Any]) -> str:
        """Handle retrieval strategies query."""
        _ = arguments  # Arguments not used for this tool
        if not self._resource_handler:
            raise ToolExecutionError("get_retrieval_strategies", "Resource handler not configured")
        return await self._resource_handler("graphrag://retrieval-strategies")

    async def _handle_get_architectural_tradeoffs(self, arguments: Dict[str, Any]) -> str:
        """Handle architectural tradeoffs query."""
        _ = arguments  # Arguments not used for this tool
        if not self._resource_handler:
            raise ToolExecutionError("get_architectural_tradeoffs", "Resource handler not configured")
        return await self._resource_handler("graphrag://architectural-tradeoffs")

    async def _handle_get_technology_stacks(self, arguments: Dict[str, Any]) -> str:
        """Handle technology stacks query."""
        _ = arguments  # Arguments not used for this tool
        if not self._resource_handler:
            raise ToolExecutionError("get_technology_stacks", "Resource handler not configured")
        return await self._resource_handler("graphrag://technology-stacks")

    # Prompt execution handlers

    async def _handle_analyze_pattern(self, arguments: Dict[str, Any]) -> str:
        """Handle pattern analysis prompt execution."""
        if not self._prompt_handler:
            raise ToolExecutionError("analyze_graphrag_pattern", "Prompt handler not configured")

        use_case = arguments.get("use_case", "")
        if not use_case:
            raise ToolExecutionError("analyze_graphrag_pattern", "use_case is required")

        prompt_args = {
            "use_case": use_case,
            "requirements": arguments.get("requirements", ""),
            "data_types": arguments.get("data_types", "")
        }

        result = await self._prompt_handler("analyze-graphrag-pattern", prompt_args)
        return result.messages[0].content.text if result.messages else "No response generated"

    async def _handle_compare_architectures(self, arguments: Dict[str, Any]) -> str:
        """Handle architecture comparison prompt execution."""
        if not self._prompt_handler:
            raise ToolExecutionError("compare_architectures", "Prompt handler not configured")

        use_case = arguments.get("use_case", "")
        if not use_case:
            raise ToolExecutionError("compare_architectures", "use_case is required")

        prompt_args = {
            "use_case": use_case,
            "scale": arguments.get("scale", ""),
            "performance_requirements": arguments.get("performance_requirements", "")
        }

        result = await self._prompt_handler("compare-architectures", prompt_args)
        return result.messages[0].content.text if result.messages else "No response generated"

    async def _handle_design_knowledge_graph(self, arguments: Dict[str, Any]) -> str:
        """Handle knowledge graph design prompt execution."""
        if not self._prompt_handler:
            raise ToolExecutionError("design_knowledge_graph", "Prompt handler not configured")

        domain = arguments.get("domain", "")
        if not domain:
            raise ToolExecutionError("design_knowledge_graph", "domain is required")

        prompt_args = {
            "domain": domain,
            "data_sources": arguments.get("data_sources", ""),
            "integration_requirements": arguments.get("integration_requirements", "")
        }

        result = await self._prompt_handler("design-knowledge-graph", prompt_args)
        return result.messages[0].content.text if result.messages else "No response generated"

    async def _handle_implement_retrieval_strategy(self, arguments: Dict[str, Any]) -> str:
        """Handle retrieval strategy implementation prompt execution."""
        if not self._prompt_handler:
            raise ToolExecutionError("implement_retrieval_strategy", "Prompt handler not configured")

        strategy = arguments.get("strategy", "")
        if not strategy:
            raise ToolExecutionError("implement_retrieval_strategy", "strategy is required")

        prompt_args = {
            "strategy": strategy,
            "technology_stack": arguments.get("technology_stack", ""),
            "use_case": arguments.get("use_case", "")
        }

        result = await self._prompt_handler("implement-retrieval-strategy", prompt_args)
        return result.messages[0].content.text if result.messages else "No response generated"