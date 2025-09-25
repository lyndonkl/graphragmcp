"""
Configuration management for GraphRAG MCP Server.
"""

import logging
from dataclasses import dataclass
from typing import Optional


@dataclass
class ServerConfig:
    """Configuration for the GraphRAG MCP Server."""

    server_name: str = "graphrag-mcp"
    server_version: str = "0.1.0"
    log_level: str = "INFO"
    max_content_length: int = 1000000  # 1MB limit for content responses
    enable_debug: bool = False


def setup_logging(config: ServerConfig) -> logging.Logger:
    """Set up logging configuration."""
    logging.basicConfig(
        level=getattr(logging, config.log_level.upper()),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    logger = logging.getLogger(config.server_name)

    if config.enable_debug:
        logger.setLevel(logging.DEBUG)

    return logger


# Default configuration instance
DEFAULT_CONFIG = ServerConfig()