"""
Main GraphRAG MCP Server implementation.

A modular, well-architected Model Context Protocol server providing comprehensive
knowledge about Knowledge Graph Construction & Retrieval Strategies for LLM Reasoning.
"""

import logging
from typing import List, Dict

import mcp.types as types
from mcp.server import NotificationOptions, Server
from mcp.server.models import InitializationOptions
import mcp.server.stdio

from .config import ServerConfig, setup_logging
from .resources import ResourceRegistry, GRAPHRAG_RESOURCES
from .prompts import PromptRegistry, GRAPHRAG_PROMPTS
from .prompts.generators import (
    generate_analyze_pattern_prompt,
    generate_design_knowledge_graph_prompt,
    generate_implement_retrieval_strategy_prompt,
    generate_compare_architectures_prompt,
)
from .content import (
    get_overview_content,
    get_construction_patterns_content,
    get_embedding_strategies_content,
    get_retrieval_strategies_content,
    get_architectural_tradeoffs_content,
    get_literature_landscape_content,
    get_technology_stacks_content,
    get_pattern_catalog_content,
    get_construction_pattern_detail,
    get_embedding_strategy_detail,
    get_retrieval_strategy_detail,
)
from .utils.exceptions import GraphRAGError


class GraphRAGMCPServer:
    """
    GraphRAG MCP Server providing comprehensive knowledge about Knowledge Graph
    Construction & Retrieval Strategies for LLM Reasoning.
    """

    def __init__(self, config: ServerConfig = None):
        """Initialize the GraphRAG MCP Server."""
        self.config = config or ServerConfig()
        self.logger = setup_logging(self.config)

        # Initialize MCP server
        self.server = Server(self.config.server_name)

        # Initialize registries
        self.resource_registry = ResourceRegistry(self.logger)
        self.prompt_registry = PromptRegistry(self.logger)

        # Set up server handlers
        self._setup_resources()
        self._setup_prompts()
        self._setup_handlers()

        self.logger.info(f"GraphRAG MCP Server initialized (v{self.config.server_version})")

    def _setup_resources(self) -> None:
        """Set up all resources with their content generators."""
        self.logger.debug("Setting up resources...")

        # Register main resources
        content_generators = {
            "graphrag://overview": get_overview_content,
            "graphrag://construction-patterns": get_construction_patterns_content,
            "graphrag://embedding-strategies": get_embedding_strategies_content,
            "graphrag://retrieval-strategies": get_retrieval_strategies_content,
            "graphrag://architectural-tradeoffs": get_architectural_tradeoffs_content,
            "graphrag://literature-landscape": get_literature_landscape_content,
            "graphrag://technology-stacks": get_technology_stacks_content,
            "graphrag://pattern-catalog": get_pattern_catalog_content,
        }

        # Register all resources
        for resource in GRAPHRAG_RESOURCES:
            if resource.uri in content_generators:
                self.resource_registry.register_resource(
                    resource, content_generators[resource.uri]
                )
            elif str(resource.uri).startswith("graphrag://patterns/"):
                def make_pattern_generator(uri):
                    async def generator():
                        return await get_construction_pattern_detail(str(uri))
                    return generator
                self.resource_registry.register_resource(
                    resource, make_pattern_generator(resource.uri)
                )
            elif str(resource.uri).startswith("graphrag://embeddings/"):
                def make_embedding_generator(uri):
                    async def generator():
                        return await get_embedding_strategy_detail(str(uri))
                    return generator
                self.resource_registry.register_resource(
                    resource, make_embedding_generator(resource.uri)
                )
            elif str(resource.uri).startswith("graphrag://retrieval/"):
                def make_retrieval_generator(uri):
                    async def generator():
                        return await get_retrieval_strategy_detail(str(uri))
                    return generator
                self.resource_registry.register_resource(
                    resource, make_retrieval_generator(resource.uri)
                )

        self.logger.info(f"Registered {len(GRAPHRAG_RESOURCES)} resources")

    def _setup_prompts(self) -> None:
        """Set up all prompts with their generators."""
        self.logger.debug("Setting up prompts...")

        prompt_generators = {
            "analyze-graphrag-pattern": generate_analyze_pattern_prompt,
            "design-knowledge-graph": generate_design_knowledge_graph_prompt,
            "implement-retrieval-strategy": generate_implement_retrieval_strategy_prompt,
            "compare-architectures": generate_compare_architectures_prompt,
        }

        for prompt in GRAPHRAG_PROMPTS:
            if prompt.name in prompt_generators:
                self.prompt_registry.register_prompt(
                    prompt, prompt_generators[prompt.name]
                )

        self.logger.info(f"Registered {len(GRAPHRAG_PROMPTS)} prompts")

    def _setup_handlers(self) -> None:
        """Set up MCP server handlers."""

        @self.server.list_resources()
        async def handle_list_resources() -> List[types.Resource]:
            """List available GraphRAG knowledge resources."""
            try:
                resources = self.resource_registry.get_resources()
                self.logger.debug(f"Listed {len(resources)} resources")
                return resources
            except Exception as e:
                self.logger.error(f"Error listing resources: {e}")
                raise

        @self.server.read_resource()
        async def handle_read_resource(uri: str) -> str:
            """Read and return content for the specified GraphRAG resource."""
            try:
                self.logger.debug(f"Reading resource: {uri}")
                content = await self.resource_registry.get_content(uri)

                # Apply content length limit if configured
                if len(content) > self.config.max_content_length:
                    self.logger.warning(
                        f"Content for {uri} exceeds limit ({len(content)} > {self.config.max_content_length})"
                    )
                    content = content[:self.config.max_content_length] + "\n\n[Content truncated due to length limit]"

                return content
            except GraphRAGError:
                raise  # Re-raise our custom exceptions
            except Exception as e:
                self.logger.error(f"Unexpected error reading resource {uri}: {e}")
                raise

        @self.server.list_prompts()
        async def handle_list_prompts() -> List[types.Prompt]:
            """List available GraphRAG prompts."""
            try:
                prompts = self.prompt_registry.get_prompts()
                self.logger.debug(f"Listed {len(prompts)} prompts")
                return prompts
            except Exception as e:
                self.logger.error(f"Error listing prompts: {e}")
                raise

        @self.server.get_prompt()
        async def handle_get_prompt(name: str, arguments: Dict[str, str]) -> types.GetPromptResult:
            """Generate prompts for GraphRAG analysis and implementation."""
            try:
                self.logger.debug(f"Generating prompt: {name} with args: {list(arguments.keys())}")
                result = await self.prompt_registry.generate_prompt(name, arguments)
                return result
            except GraphRAGError:
                raise  # Re-raise our custom exceptions
            except Exception as e:
                self.logger.error(f"Unexpected error generating prompt {name}: {e}")
                raise

    async def run(self) -> None:
        """Run the GraphRAG MCP server."""
        self.logger.info("Starting GraphRAG MCP Server...")

        try:
            async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
                await self.server.run(
                    read_stream,
                    write_stream,
                    InitializationOptions(
                        server_name=self.config.server_name,
                        server_version=self.config.server_version,
                        capabilities=self.server.get_capabilities(
                            notification_options=NotificationOptions(),
                            experimental_capabilities={},
                        ),
                    ),
                )
        except KeyboardInterrupt:
            self.logger.info("Server shutdown requested")
        except Exception as e:
            self.logger.error(f"Server error: {e}")
            raise
        finally:
            self.logger.info("GraphRAG MCP Server stopped")


def create_server(config: ServerConfig = None) -> GraphRAGMCPServer:
    """Factory function to create a GraphRAG MCP Server instance."""
    return GraphRAGMCPServer(config)


async def main() -> None:
    """Main entry point for the GraphRAG MCP Server."""
    server = create_server()
    await server.run()


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())